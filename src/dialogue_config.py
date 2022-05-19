#################################
# Usersim config
#################################
# Used in EMC for intent error (and in user)
usersim_intents = ['request']

#################################
# Agent config
#################################

# Possible inform slots
# agent_inform_slots = ['guc_regulations_clothing', 'guc_regulations_general','guc_regulations_attendance',  'study_guide_midterm', 'study_guide_finals', 'study_guide_general', 'advising_general_info','advising_tips_to_getout', 'probation', 'summer_attendance', 'summer_general']
agent_inform_slots = ['guc_regulations_clothing', 'guc_regulations_general','guc_regulations_attendance', "guc_regulations_berlin", 'study_guide_exams', "study_guide_textbooks", 'study_guide_general','advising_general_info','probation_tips_to_getout', 'probation', 'summer_attendance', "summer_courses", "summer_grading", 'summer_general']


# Possible actions for agent
agent_actions = []

for slot in agent_inform_slots:
    agent_actions.append({'intent': 'inform', 'inform_slots': {slot: 'PLACEHOLDER'}, 'request_slots': {}})

# Rule based policy request list
# rule_requests = ['guc_regulations', 'study_guide', 'advising', 'probation', 'summer']
# rule_requests = ['guc_regulations_clothing', 'guc_regulations_general','guc_regulations_attendance',  'study_guide_midterm', 'study_guide_finals', 'study_guide_general', 'advising_general_info','advising_tips_to_getout', 'probation', 'summer_attendance', 'summer_general']
rule_requests = ['guc_regulations_clothing', 'guc_regulations_general','guc_regulations_attendance', "guc_regulations_berlin", 'study_guide_exams', "study_guide_textbooks", 'study_guide_general','advising_general_info','probation_tips_to_getout', 'probation', 'summer_attendance', "summer_courses", "summer_grading", 'summer_general']


#############################
# Global config
#############################
FAIL = -1
NO_OUTCOME = 0
SUCCESS = 1

# All possible intents
all_intents = ['inform', 'request']

# All slots
# all_slots = ['guc_regulations_clothing', 'guc_regulations_general','guc_regulations_attendance',  'study_guide_midterm', 'study_guide_finals', 'study_guide_general', 'advising_general_info','advising_tips_to_getout', 'probation', 'summer_attendance', 'summer_general']
all_slots = ['guc_regulations_clothing', 'guc_regulations_general','guc_regulations_attendance', "guc_regulations_berlin", 'study_guide_exams', "study_guide_textbooks", 'study_guide_general','advising_general_info','probation_tips_to_getout', 'probation', 'summer_attendance', "summer_courses", "summer_grading", 'summer_general']


# Agent responses
all_responses = ['\nAll normal clothes are allowed, ex: Any clothes you can wear to a mall are allowed; ripped jeans, shorts, sun dresses, crop tops, ...',
'\n- Smoking indoors is prohibted.\n - Trashing common areas shared with other GUCians is prohibited.\n- Couples must not be intimate and respect others boundarys.\n-You cannot verbally or physically assault anyone on GUC premises. Check all the GUC regulations, LINK',
"\nIn Spring and winter semesters, you must attend 75% of your Tutorials, Lecture does not have attendance.",
"\n- A minimum of 25 students are needed to open a group in Berlin.\n-Check Berlin Semester abroad time plan for admission and fees, LINK.",
'\n1- Solve previous years Exams made by the SAME Dr. \n2-Focus on content that you did not get examed in (Quizzes, midterm, assignments).',
"\n-Honestly, only students who aim for A+ and A need to. Otherwise you can work around with slides and sheets.",
'\n1- Read lecture slides on the same day of the lecture. \n2-Every weekend, just have a look on the PAs of the next week. \n 3- Solve the PAs yourself just before te quiz.\n If you follow the above steps, you will only solve PAs once, and acheive a decent grade.',
'\nAdvising general information and rules, LINK',
'\n- Focus on high credit hours courses. \n- Overload on Credit hours as mush as you can, to be able to graduate with your colleagues.',
'\nEach student under probation has an advisor to help them get out of it.\n A student is under probation if their GPA is greater than 3.7, to get out of it they need to improve their GPA which depends on their current situation.',
'\nIn summer, you must attend 75% of your Lectures and Tutorials',
'\n-A course is offered in summer if it has at least 25 students who want to take it.\n-You can apply for a summer course here #LINK#',
'\nIn summer a course has exactly the same grade distribution (quizzes, assignments, project), but has only one final exam with a weight equals to (midterm + final)',
'\n- There are 2 rounds in the summer semester. \n- Each round you can take a maximum of 10 Credit hours. \n- A summer round is 3 weeks, and the final is in the 4th week. \n- Every 2 CH in a course have 4 slots weekly; ex. A 4 CH course has 8 slots per week.\n- Checkout the rest of summer guidelines. LINK']