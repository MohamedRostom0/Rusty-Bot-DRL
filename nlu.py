# import gensim.downloader as api
from dialogue_config import all_slots


class NLU:
    def __init__(self):
        pass
        # self.model = api.load('glove-wiki-gigaword-50')


    def getSemanticFrame(self, userInput):
        response = {'intent': "", 'request_slots': {}, 'inform_slots':{}}

        # For now, I only support intents = ['request']
        intent = 'request'
        response["intent"] = intent

        request_slots = self.getRequestSlots(userInput)

        for slot in request_slots:
            response['request_slots'][slot] = 'UNK'

        return response


    def getIntent(self, userInput):
        pass


    def getRequestSlots(self, userInput):
        slots = []

        words = userInput.lower().split()
        if "summer" in words:
            if 'attendance' in words or "absence" in words or "absent" in words:
                slots.append("summer_attendance")
            elif 'courses' in words:
                slots.append("summer_courses")
            elif 'grades' in words or "grading" in words:
                slots.append('summer_grading')
            else:
                slots.append("summer_general")

        elif "study" in words:
            if "midterm" in words or "midterms" in words:
                slots.append("study_guide_exams")
            elif "final" in words or "finals" in words:
                slots.append("study_guide_exams")
            elif 'textbook' in words:
                slots.append("study_guide_textbooks")
            else:
                slots.append("study_guide_general")

        elif "regulations" in words or "policy" in words or "guc" in words:
            if "clothes" in words or "clothing" in words:
                slots.append("guc_regulations_clothing")
            elif "attendance" in words:
                slots.append("guc_regulations_attendance")
            elif 'berlin' in words:
                slots.append('guc_regulations_berlin')
            else:
                slots.append("guc_regulations_general")

        elif "advising" in words:
            slots.append("advising_general_info")

        elif "probation" in words:
            if 'tips' in words or 'help' in words:
                slots.append('probation_tips_to_getout')
            else:
                slots.append('probation')

        return slots


	#Check if word is number by numerical value or high similarity to the word number
    def isNumber(self, word):
        pass