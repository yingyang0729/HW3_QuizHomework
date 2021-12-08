from components.QuizQuestions import questions
from components import vars,quizTally
from colorama import Fore, Back
from emoji import emojize

print("\033[2;33;40m====================== Psychological Quiz ======================")
import emoji
print(emoji.emojize('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    :evergreen_tree: :deciduous_tree: :four_leaf_clover: :seedling: :herb: :palm_tree:    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'))

print(Back.BLUE + Fore.WHITE + '=====================================Start========================================')

answer1 = questions["q1"][input(questions["q1"]["question"])]
print(answer1)

vars.quizTotal += answer1
print("========================Good!==========================")

answer2 = questions["q2"][input(questions["q2"]["question"])]
print(answer2)

vars.quizTotal += answer2
print("========================Great!==========================")

answer3 = questions["q3"][input(questions["q3"]["question"])]
print(answer3)

vars.quizTotal += answer3
print("=========================Nice!=========================")

answer4 = questions["q4"][input(questions["q4"]["question"])]
print(answer4)

vars.quizTotal += answer4
print("=========================Wonderful!=========================")

answer5 = questions["q5"][input(questions["q5"]["question"])]
print(answer5)

vars.quizTotal += answer5
print("=========================Awesome!=========================")

answer6 = questions["q6"][input(questions["q6"]["question"])]
print(answer6)

vars.quizTotal += answer6
print("=========================Fantastic!=========================")

quizTally.total(vars.quizTotal)  

print("total so far:"+ str(vars.quizTotal)+"\n")
print("============================================== Have a nice day! =======================================================")
import emoji
print(emoji.emojize('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    :sun_with_face:   :crescent_moon:   :sun_with_face:   :crescent_moon:   :sun_with_face:   :crescent_moon:    xxxxxxxxxxxxxxxxxxxxxxxxxxxx'))