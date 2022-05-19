import numpy as np
from utils import convert_list_to_dict
from dialogue_config import all_intents, all_slots
import copy

class StateTracker:
    def __init__(self, constants):
        self.intents_dict = convert_list_to_dict(all_intents)
        self.num_intents = len(all_intents)
        self.slots_dict = convert_list_to_dict(all_slots)
        self.num_slots = len(all_slots)
        self.max_round_num = constants['run']['max_round_num']
        self.none_state = np.zeros(self.get_state_size())
        self.reset()


    def get_state_size(self):
        return self.num_intents + self.num_slots
        # return 2 * self.num_intents + 7 * self.num_slots + 3 + self.max_round_num

    
    def reset(self):
        """Resets current_informs, history and round_num."""

        self.current_informs = {}
        # A list of the dialogues (dicts) by the agent and user so far in the conversation
        self.history = []
        self.round_num = 0

    
    def get_state(self, done=False):
        if done:
            return self.none_state

        user_action = self.history[-1]
        last_agent_action = self.history[-2] if len(self.history) > 1 else None

        # Create one-hot of intents to represent the current user action
        user_action_representation = np.zeros((self.num_intents,))
        user_action_representation[self.intents_dict[user_action['intent']]] = 1.0

        # Create bag of inform slots representation to represent the current user action
        # user_inform_slots_representation = np.zeros((self.num_slots,))
        # for key in user_action['inform_slots'].keys():
        #     user_inform_slots_representation[self.slots_dict[key]] = 1.0


        # Create bag of inform slots representation to represent the current user action
        user_request_slots_representation = np.zeros((self.num_slots,))
        for key in user_action['request_slots'].keys():
            user_request_slots_representation[self.slots_dict[key]] = 1.0


        state_representation = np.hstack(
            [user_action_representation, user_request_slots_representation]
        )

        print("State rep = " , state_representation)
        return state_representation


    def update_state_user(self, user_action):
        self.history.append(user_action)
        self.round_num += 1

    
    def update_state_agent(self, agent_action):
        self.history.append(agent_action)
        