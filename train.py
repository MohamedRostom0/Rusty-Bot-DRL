import random
from user_simulator import UserSimulator
from dqn_agent import DQNAgent
from state_tracker import StateTracker
import pickle, argparse, json, math
from utils import remove_empty_slots
from user import User

import os

os.system('color')

if __name__ == '__main__':
    # Can provide constants file path in args OR run it as is and change 'CONSTANTS_FILE_PATH' below
    # 1) In terminal: python train.py --constants_path "constants.json"
    # 2) Run this file as is
    parser = argparse.ArgumentParser()
    parser.add_argument('--constants_path', dest='constants_path', type=str, default='')
    args = parser.parse_args()
    params = vars(args)

    # Load constants json into dict
    CONSTANTS_FILE_PATH = 'constants.json'
    if len(params['constants_path']) > 0:
        constants_file = params['constants_path']
    else:
        constants_file = CONSTANTS_FILE_PATH

    with open(constants_file) as f:
        constants = json.load(f)

    # Load run constants
    run_dict = constants['run']
    USE_USERSIM = run_dict['usersim']
    WARMUP_MEM = run_dict['warmup_mem']
    NUM_EP_TRAIN = run_dict['num_ep_run']
    TRAIN_FREQ = run_dict['train_freq']
    MAX_ROUND_NUM = run_dict['max_round_num']
    SUCCESS_RATE_THRESHOLD = run_dict['success_rate_threshold']
    EMC_ENABLED = run_dict['emc_enabled']



    # Init Objects
    if USE_USERSIM:
        user = UserSimulator(constants)
    else:
        user = User(constants)

    state_tracker = StateTracker(constants)
    dqn_agent = DQNAgent(state_tracker.get_state_size(), constants['agent'])


def run_round(state, warmup=False):
    # 1) Agent takes action given state tracker's representation of dialogue (state)
    agent_action_index, agent_action = dqn_agent.get_action(state, use_rule=warmup)

    # 2) Update state tracker with the agent's action
    state_tracker.update_state_agent(agent_action)

    # 3) User takes action given agent action
    user_action, reward, done, success = user.step(agent_action)

    # 5) Update state tracker with user action
    state_tracker.update_state_user(user_action)
    # 6) Get next state and add experience
    next_state = state_tracker.get_state(done)
    dqn_agent.add_experience(state, agent_action_index, reward, next_state, done)

    print("Agent action: ", agent_action)
    print("reward: ", reward)
    return next_state, reward, done, success


def warmup_run():
    print('warmup started...')
    total_step = 0
    while total_step != WARMUP_MEM and not dqn_agent.memory_is_full():
        print("-----------------")
        print(f"Warmup epsisode: {total_step}")
        episode_reset()
        done = False
        # Get initial state from state tracker
        state = state_tracker.get_state()
        while not done:
            next_state, _, done, _ = run_round(state, warmup=True)
            total_step += 1
            state = next_state
        
    print('...warmup ended')


def train_run():
    print("training started...")
    training_history = []

    episode = 0
    period_reward_total = 0
    period_success_total = 0
    success_rate_best = 0.0
    while episode < NUM_EP_TRAIN:
        print("-----------------")
        print(f'Training episode: {episode}')
        episode_reset()
        episode += 1
        done = False
        state = state_tracker.get_state()
        while not done:
            if EMC_ENABLED:
                # Add error to state for more robustness
                randIdx = random.randint(0, len(state)-1)
                randtemp = random.random()
                if randtemp <= 0.10:
                    state[randIdx] = 1 if state[randIdx] == 0 else 0
                    print('\033[91m' + f"state after error = {state}" + '\033[0m')

            next_state, reward, done, success = run_round(state)
            period_reward_total += reward
            state = next_state

        period_success_total += success

        # Record every 1000 eoisode results in history
        if episode % 1000 == 0:
            training_history.append(f"Episode {episode} => Best success rate = {success_rate_best}")

        # Train
        if episode % TRAIN_FREQ == 0:
            # Check success rate
            success_rate = period_success_total / TRAIN_FREQ
            avg_reward = period_reward_total / TRAIN_FREQ
            # Flush
            if success_rate >= success_rate_best and success_rate >= SUCCESS_RATE_THRESHOLD:
                dqn_agent.empty_memory()
            # Update current best success rate
            if success_rate > success_rate_best:
                print('Episode: {} NEW BEST SUCCESS RATE: {} Avg Reward: {}' .format(episode, success_rate, avg_reward))
                success_rate_best = success_rate
                dqn_agent.save_weights()
            period_success_total = 0
            period_reward_total = 0
            # Copy
            dqn_agent.copy()
            # Train
            dqn_agent.train()
            print(f"Avg reward: {avg_reward}")

    print("=================")
    print("Best success rate: ", success_rate_best)
    print("##################")
    print(f"training_history = {training_history}")
    print('...Training Ended')


def episode_reset():
    state_tracker.reset()
    user_action = user.reset()

    state_tracker.update_state_user(user_action)

    dqn_agent.reset()


warmup_run()
train_run()