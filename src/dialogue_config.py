#################################
# Usersim config
#################################
# Used in EMC for intent error (and in user)
usersim_intents = ['request']

#################################
# Agent config
#################################

# Possible inform slots

agent_inform_slots = ['nlu_fallback', 'cv_preparation', 'side_pjojects_importance', 'plagirism_policy', 'grades_schema','finding_internships', 'internships_obligatory_or_not', 'internships_duration_required','internship_submission','guc_regulations_attendance', "guc_regulations_berlin", 'study_guide_exams', 'study_guide_general','advising_general_info','probation_tips_to_getout', 'probation', 'summer_attendance', "summer_courses", "summer_grading", 'summer_general']
# agent_inform_slots = ['guc_regulations_clothing', 'guc_regulations_general','guc_regulations_attendance', "guc_regulations_berlin", 'study_guide_exams', "study_guide_textbooks", 'study_guide_general','advising_general_info','probation_tips_to_getout', 'probation', 'summer_attendance', "summer_courses", "summer_grading", 'summer_general']


# Possible actions for agent
agent_actions = []

for slot in agent_inform_slots:
    agent_actions.append({'intent': 'inform', 'inform_slots': {slot: 'PLACEHOLDER'}, 'request_slots': {}})

# Rule based policy request list
rule_requests = ['nlu_fallback','cv_preparation', 'side_pjojects_importance', 'plagirism_policy', 'grades_schema','finding_internships', 'internships_obligatory_or_not', 'internships_duration_required','internship_submission','guc_regulations_attendance', "guc_regulations_berlin", 'study_guide_exams', 'study_guide_general','advising_general_info','probation_tips_to_getout', 'probation', 'summer_attendance', "summer_courses", "summer_grading", 'summer_general']
# rule_requests = ['guc_regulations_clothing', 'guc_regulations_general','guc_regulations_attendance', "guc_regulations_berlin", 'study_guide_exams', "study_guide_textbooks", 'study_guide_general','advising_general_info','probation_tips_to_getout', 'probation', 'summer_attendance', "summer_courses", "summer_grading", 'summer_general']


#############################
# Global config
#############################
FAIL = -1
NO_OUTCOME = 0
SUCCESS = 1

# All possible intents
all_intents = ['inform', 'request']

# All slots
all_slots = ['nlu_fallback', 'cv_preparation', 'side_pjojects_importance', 'plagirism_policy', 'grades_schema','finding_internships', 'internships_obligatory_or_not', 'internships_duration_required','internship_submission','guc_regulations_attendance', "guc_regulations_berlin", 'study_guide_exams', 'study_guide_general','advising_general_info','probation_tips_to_getout', 'probation', 'summer_attendance', "summer_courses", "summer_grading", 'summer_general']


all_responses = [
'\nSorry, can you repeat your question ?',
'\nCV preparation tips',
"\nHaving extra side projects for yourself definitely gives you a bonus while applying for jobs, but it's not a necessity.",
"\nYou are not allowed to copy anything without explicit acknowledgement of the sources.\nStudents always have to acknowledge the source through: Quoting, Paraphrasing, General Indebtedness. Please note that copying the work of another student is no different from plagiarizing published sources.\nStudents who plagiarise work and students who knowingly allow their work to be plagiarised will be subject to penalties.\nPlease note that plagiarism seriously damages ability to pass exams and may result in serious cases in suspension or dismissal.",
'\nA+ : 0.7\nA : 1.0\nA- : 1.3\nB+ : 1.7\nB : 2\nB- : 2.3\nC+ : 2.7\nC : 3.0\nC- : 3.3\nD+ : 3.7\nD : 4.0\nF : 5.0',
"\nThe SCAD office sends an email with the available internships every year, and organizes a startup fair and an employment fair every year, which gives you a chance to explore the market.",
'\nYes, internships are obligatory for all faculties in the GUC.',
'\nEngineering, Applied Arts & Pharmacy: 3 months\nManagement, BI & Law: 1.5 Months',
'\n1- Print out the internship form from Intranet, LINK.\n2- Have that form filled out, and signed by your internship supervisor.\n3- Either stamp the form, get a stamped certificate, or get an email from the domain of the company confirming your participation in an internship there.\n4- Write the report and zip it with the form and other documents, and submit them HERE.',
'\nIn Spring and winter semesters, you must attend 75% of your Tutorials, Lecture does not have attendance.',
"\nA minimum of 25 students are needed to open a group in Berlin.\n-Check Berlin Semester abroad time plan for admission and fees, LINK.",
'\nSolve previous years Exams made by the SAME Dr.\nFocus on content that you did not get examed in (Quizzes, midterm, assignments).',
'\n1-Read lecture slides on the same day of the lecture. \n2-Every weekend, just have a look on the PAs of the next week. \n 3- Solve the PAs yourself just before te quiz.\n If you follow the above steps, you will only solve PAs once, and acheive a decent grade.',
'\nadvising_general_info',
'\nFocus on high credit hours courses. \n- Overload on Credit hours as mush as you can, to be able to graduate with your colleagues.',
'\nEach student under probation has an advisor to help them graduate as early as possible.\n A student is under probation if their GPA is greater than 3.7, to get out of it they need to improve their GPA which depends on their current situation.',
'\nIn summer, you must attend 75% of your Lectures and Tutorials',
"\nA course is offered in summer if it has at least 25 students who want to take it.\n-You can apply for a summer course here #LINK#",
"\nIn summer a course has exactly the same grade distribution (quizzes, assignments, project), but has only one final exam with a weight equals to (midterm + final)",
'\nThere are 2 rounds in the summer semester. \n- Each round you can take a maximum of 10 Credit hours. \n- A summer round is 3 weeks, and the final is in the 4th week.\n- Checkout the rest of summer guidelines. LINK'
]