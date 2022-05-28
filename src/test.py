from user_simulator import UserSimulator
from dqn_agent import DQNAgent
from state_tracker import StateTracker
import pickle, argparse, json, math
from utils import remove_empty_slots
from user import User
from dialogue_config import all_responses
import os
import random

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
    NUM_EP_TEST= run_dict['num_ep_run']
    MAX_ROUND_NUM = run_dict['max_round_num']
    EMC_ENABLED = run_dict['emc_enabled']


    # Init Objects
    if USE_USERSIM:
        user = UserSimulator(constants)
    else:
        user = User(constants)

    state_tracker = StateTracker(constants)
    dqn_agent = DQNAgent(state_tracker.get_state_size(), constants['agent'])


def test_run():
    print('Testing Started...')
    episode = 0
    fail_counter = 0
    while episode < NUM_EP_TEST:
        episode_reset()
        episode += 1
        ep_reward = 0
        done = False

        state = state_tracker.get_state()
        while not done:

            if EMC_ENABLED:
                # Add error to state for more robustness
                randIdx = random.randint(0, len(state)-1)
                randtemp = random.random()
                if randtemp <= 0.15:
                    state[randIdx] = 1 if state[randIdx] == 0 else 0
                    print('\033[91m' + f"state after error = {state}" + '\033[0m')

            agent_action_index, agent_action = dqn_agent.get_action(state)
            state_tracker.update_state_agent(agent_action)
            user_action, reward, done, success = user.step(agent_action)

            if reward == -1:
                fail_counter += 1
            
            ep_reward += reward

            state_tracker.update_state_user(user_action)

            state = state_tracker.get_state(done)

            print('\x1b[6;30;42m' + f"Agent action: {agent_action}" + '\x1b[0m')
            print('\x1b[6;30;42m' + f"Agent Response ==> {all_responses[agent_action_index]}" + '\x1b[0m')

        print('Episode: {} Success: {} Reward: {}'.format(episode, success, ep_reward))
    
    print("=====================")
    avg_reward = ((NUM_EP_TEST - fail_counter) / NUM_EP_TEST) * 100
    print(f"Average reward for {NUM_EP_TEST} testing episodes = {avg_reward}%")
    print(f"Failed episodes count = {fail_counter}")
    print('...Testing Ended')


def episode_reset():
    state_tracker.reset()
    user_action = user.reset()

    state_tracker.update_state_user(user_action)

    dqn_agent.reset()


test_run()