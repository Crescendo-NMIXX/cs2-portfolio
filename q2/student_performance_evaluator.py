def calculate_average(score1, score2, score3):
    return (score1 + score2 + score3) / 3


def get_performance(average):
    if average >= 85:
        return "Mastery"
    elif average >= 70:
        return "Developing"
    else:
        return "Needs Review"


def is_eligible(average, completed_tasks):
    return average >= 85 and completed_tasks >= 3


# Ask the user to enter three scores
score1 = float(input("Enter Score 1: "))
score2 = float(input("Enter Score 2: "))
score3 = float(input("Enter Score 3: "))

# Ask for the number of completed tasks
completed_tasks = int(input("Completed Tasks: "))

# Calculate the average
average = calculate_average(score1, score2, score3)

# Determine the performance category
performance = get_performance(average)

# Check eligibility for the practice challenge
eligible = is_eligible(average, completed_tasks)

# Display the results
print(f"\nAverage: {average:.2f}")
print(f"Performance: {performance}")
print(f"Eligible for Challenge: {eligible}")

#Documentation Questions

#1.Which function returns a number, which returns a string, and which returns a Boolean?
#calculate_average() returns a number, get_performance() returns a string, and is_eligible() returns a Boolean (True or False).

#2.Explain how the average moves from calculate_average() into get_performance().
#The calculate_average() function calculates and returns the average score. This returned value is then passed as an argument to get_performance() to determine the student's performance category.

#3.What happens when a student has a high average but has completed fewer than three tasks?
#The student is not eligible for the practice challenge because they must have an average of at least 85 and have completed at least three tasks.

#4.Why is return more appropriate than simply printing the result inside each function?
#Using return allows the result to be stored in a variable and used by other functions. Printing only displays the result and does not allow other functions to use it directly.
