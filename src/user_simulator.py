import random
from dialogue_config import FAIL, SUCCESS, usersim_intents, all_slots
from utils import reward_function

class UserSimulator:
    def __init__(self, constants):
        self.max_round = constants['run']['max_round_num']

    
    def reset(self):
        self.user_last_response = None
        return self._return_response()

    
    def _return_response(self):
        response = {'intent': 'request', 'inform_slots': {}, 'request_slots': {}}

        request_slot = random.choice(all_slots)
        response['request_slots'][request_slot] = "UNK"

        print("User input = " ,response)
        self.user_last_response = response
        return response


    def _return_success(self):
        """
        Ask the user in console to input success (-1, 0 or 1) for (loss, neither loss nor win, win).

        Returns:
            int: Success: -1, 0 or 1
        """

        success = -2
        while success not in (-1, 0, 1):
            success = int(input('Success?: '))
        return success


    def step(self, agent_action):
        user_response = {'intent': '', 'request_slots': {}, 'inform_slots': {}}
        reward = 0

        agent_informs = agent_action['inform_slots']
        informed_key = list(agent_informs.keys())[0]

        if self.user_last_response:
            if self.user_last_response['intent'] == 'request':
                key = list(self.user_last_response['request_slots'].keys())[0]
                if informed_key == key:
                    reward = SUCCESS
                else:
                    reward = FAIL

        return user_response, reward, True, True if reward == SUCCESS else False