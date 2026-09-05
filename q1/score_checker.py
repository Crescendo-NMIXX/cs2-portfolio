# This asks the user to enter the student's score
student_score = int(input("Enter student score: "))

# The score is only in the range of 0 to 100
if student_score < 0 or student_score > 100:
    print("Invalid Score.")

# This classifies the student's score as either of the categories
elif student_score >= 90:
    print("Outstanding")
elif student_score >= 80:
    print("Very Satisfactory")
elif student_score >= 75:
    print("Satisfactory")
else:
    print("Needs Improvement")
