from dialogue_config import FAIL, SUCCESS, usersim_intents, all_slots
from utils import reward_function
from nlu import NLU

class User:
    def __init__(self, constants):
        self.max_round = constants['run']['max_round_num']
        self.use_rasa = constants['run']['use_rasa']
        self.nlu = NLU()

    
    def reset(self):
        self.user_last_response = None
        return self._use_nlu()
        # return self._return_response()

    
    def _use_nlu(self):
        while True:
            input_string = input("\x1b[93m" + "User input ==> " + "\x1b[0m")

            if self.use_rasa:
                semanticFrame = self.nlu.use_rasa(input_string)
            else:
                semanticFrame =  self.nlu.getSemanticFrame(input_string)
            
            print("\x1b[93m" + f"User semantic frame: {semanticFrame}" + "\x1b[0m")
            self.user_last_response = semanticFrame
            return semanticFrame


    def _return_response(self):
        response = {'intent': '', 'inform_slots': {}, 'request_slots': {}}
        while True:
            input_string = input("Response: ")
            chunks = input_string.split('/')

            # print(chunks)

            intent_correct = True
            if chunks[0] not in usersim_intents:
                intent_correct = False
            response['intent'] = chunks[0]

            informs_correct = True
            if len(chunks[1]) > 0:
                inform_items_list = chunks[1].split(', ')
                for inf in inform_items_list:
                    inf = inf.split(': ')
                    if inf[0] not in all_slots:
                        informs_correct = False
                        break
                    response['inform_slots'][inf[0]] = "PLACEHOLDER"

            requests_correct = True
            if len(chunks[2]) > 0:
                requests_key_list = chunks[2].split(', ')
                for req in requests_key_list:
                    if req not in all_slots:
                        requests_correct = False
                        break
                    response['request_slots'][req] = 'UNK'
                    

            if intent_correct and informs_correct and requests_correct:
                break

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
        # reward = self._return_success()

        return user_response, reward, True, True if reward == SUCCESS else False