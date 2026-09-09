# Input Validation and Output Verification

 **Activity:** PSHS Workshop Registration Validator\
 **Name:** Yrrah Gaile A . Villarino\
 **Section:** Your Section\
 **Quarter:** 1

---

 ## Activity Overview

 In this activity, I created a program that validates information entered into a PSHS workshop registration system.

 The program checks whether user input satisfies specific requirements before accepting the registration. The program validates:

 - student name
- age
- grade level
- email address
- registration code

---

 # Part A - Validation Requirements

 | Data Captured | Expected Input | Validation Type | Invalid Input Example | Validation Rule | Error Message |
| --- | --- | --- | --- | --- | --- |
| Student Name | A non-blank name | Presence Validation | `""` | The student name must not be blank. | `Student name is required` |
| Age | A whole number from 11 to 18 | Data Type + Range Validation | `fourteen`, `10`, `19` | The age must be a number and must be between 11 and 18. | `Age must be a number.` / `Age must be from 11 to 18.` |
| Grade Level | A whole number from 7 to 12 | Acceptable Value Validation | `13` | The grade level must be between 7 and 12. | `Invalid grade level.` / `Invalid grade level. Please enter a number.` |
| Email Address | An email containing `@` and `.` | Pattern Validation | `studentpshs.edu.ph` | The email must contain both `@` and `.`. | `Invalid.` |
| Registration Code | Exactly 6 characters | Length Validation | `ABC` | The registration code must contain exactly 6 characters. | `The registration code must contain exactly 6 characters.` |

---

 ## Validation Questions

 ### 1\. Why should the student name not be blank?

 The student name should not be blank because the registration system needs to know who is registering and a blank would result into an invalid input.

 ### 2\. Why should age be checked for both data type and range?

 Age should be checked for data type to make sure the user enters a number instead of a word and the number is in the range of 11 to 18.

 ### 3\. Why should grade level only accept specific values?

 Grade level should only accept values from 7 to 12 because these are the grade levels allowed by the registration system.

 ### 4\. What format requirements did you use for the email address?

 I required the email address to contain both an `@` symbol and a period (`.`). If either one is missing, the email is considered invalid.

 ### 5\. What length requirement did you use for the registration code?

 The registration code must contain exactly 6 characters, codes with less than or more than 6 characters are rejected.

---

 # Part B - Program Design

 ## Pseudocode

```
START

Ask the user to enter their name.

IF the name is blank:
    Display "Student name is required"
    STOP

Ask the user to enter their age.

TRY to convert the age to an integer.
IF the age is not a number:
    Display "Age must be a number."
    STOP

IF age is less than 11 OR greater than 18:
    Display "Age must be from 11 to 18."
    STOP

Ask the user to enter their grade level.

TRY to convert the grade level to an integer.
IF the grade level is not a number:
    Display "Invalid grade level. Please enter a number."
    STOP

IF grade level is less than 7 OR greater than 12:
    Display "Invalid grade level."
    STOP

Ask the user to enter their email.

IF the email does not contain "@" OR ".":
    Display "Invalid."
    STOP

Ask the user to enter their registration code.

IF the registration code does not contain exactly 6 characters:
    Display "The registration code must contain exactly 6 characters."
    STOP

Display "REGISTRATION COMPLETE"

Display the student's name, age, grade level, email,
and registration code.

END
```

---

 # Part C - Program Implementation

 ## Programming Language

 Python

 ## Source Code File

 `workshop_validator.py`

 ## Final Code

```
# 1. Student Name - Presence Validation
# This asks for the student's name.
studentname = str(input("Please input your name:"))
if not studentname:
    print("Student name is required")
    raise SystemExit

# 2. Age - Data Type + Range Validation

else:
    # This asks the student to enter their age,
    # but the age should be from 11 to 18.
    try:
        age = int(input("Please input your age: "))

        if age < 11 or age > 18:
            print("Age must be from 11 to 18.")
            raise SystemExit

    # This will be displayed if the student puts a word.
    except ValueError:
        print("Age must be a number.")
        raise SystemExit

# 3. Grade Level - Acceptable Value Validation
try:
    # This asks the student for their grade level,
    # and it has to be from grade 7 to 12.
    gradelevel = int(input("Please input your grade level: "))

    if gradelevel < 7 or gradelevel > 12:
        print("Invalid grade level.")
        raise SystemExit

except ValueError:
    # This will be shown when the student inputs
    # a grade that is not a number.
    print("Invalid grade level. Please enter a number.")
    raise SystemExit

# 4. Email - Simple Pattern Validation

email = input("Please input your email: ")

# This asks the student to enter their email.
# It must contain "@" and "." or else it is invalid.
if "@" in email and "." in email:
    pass
else:
    print("Invalid.")
    raise SystemExit

# 5. Registration Code - Length Validation
# This asks the student to enter their registration code
# and it must be only 6 characters long.
try:
    registrationcode = str(input("Please input your registration code: "))

    if len(registrationcode) != 6:
        print("The registration code must contain exactly 6 characters.")
        raise SystemExit

# This will be displayed when the entered registration code
# is less than or more than 6 characters.
except ValueError:
    print("The registration code must contain exactly 6 characters.")
    raise SystemExit

print("---------------------")
print("REGISTRATION COMPLETE")
print("---------------------")
print("Name: ", studentname)
print("Age: ", age)
print("Grade level: ", gradelevel)
print("Email: ", email)
print("registration code: ", registrationcode)
```

---

 ## Validation Techniques Used

 ### Presence Validation

 I used presence validation for the student name. The program checks whether the `studentname` variable is empty using `if not studentname`. If the user does not enter a name, the program displays `Student name is required` and stops.

 ### Data Type Validation

 I used data type validation for the age and grade level. The program uses `int()` to convert the user's input into a whole number. A `try` and `except ValueError` block prevents the program from continuing when the user enters text instead of a number.

 ### Range Validation

 I used range validation for the student's age. The program only accepts ages from 11 to 18. If the age is below 11 or above 18, the program displays `Age must be from 11 to 18.`

 ### Acceptable Value Validation

 I used acceptable value validation for the grade level. The program accepts grade levels from 7 through 12. Any value below 7 or above 12 is rejected.

 ### Pattern Validation

 I used a simple pattern validation for the email address. The program checks whether the email contains both `@` and `.`. If either character is missing, the program displays `Invalid.`

 ### Length Validation

 I used length validation for the registration code. The program uses `len()` to check whether the code contains exactly 6 characters. If it does not, the program displays `The registration code must contain exactly 6 characters.`

---

 # Part D - Testing

 Test the program using both valid and invalid inputs.

| Test|      Input / Condition       | Validation Being Tested |                         Expected Output                             | Actual Output                                                       |Result|
| --- | ---                          | ---                     | ---                                                                 | ---                                                                 | ---  |
|  1  | All inputs valid             | Normal case             | Registration is completed and the entered information is displayed. | Registration is completed and the entered information is displayed. | PASS |
|  2  | Blank student name           | Presence                | `Student name is required`                                          | `Student name is required`                                          | PASS |
|  3  | Age = `fourteen`             | Data type               | `Age must be a number.`                                             | `Age must be a number.`                                             | PASS |
|  4  | Age = `11`                   | Minimum boundary        | Registration continues to the next input.                           | Registration continues to the next input.                           | PASS |
|  5  | Age = `18`                   | Maximum boundary        | Registration continues to the next input.                           | Registration continues to the next input.                           | PASS |
|  6  | Age = `10`                   | Range                   | `Age must be from 11 to 18.`                                        | `Age must be from 11 to 18.`                                        | PASS |
|  7  | Grade Level = `13`           | Acceptable value        | `Invalid grade level.`                                              | `Invalid grade level.`                                              | PASS |
|  8  | Email = `studentpshs.edu.ph` | Pattern                 | `Invalid.`                                                          | `Invalid.`                                                          | PASS |
|  9  | Registration Code = `ABC`    | Length                  | `The registration code must contain exactly 6 characters.`          | `The registration code must contain exactly 6 characters.`          | PASS |
|  10 | Registration Code = `CS2026` | Valid length            | Registration is completed and the entered information is displayed. | Registration is completed and the entered information is displayed. | PASS |

---

 # Part E - Output Verification

 Choose any three tests from Part D.

 ## Verification Test 1

 **Input:**

```
Name: Yrrah Gaile A. Villarino
Age: 13
Grade Level: 8
Email: ygavillarino@brc.pshs.edu.ph
Registration Code: CS2026
```

 **Expected Output:**

```
---------------------
REGISTRATION COMPLETE
---------------------
Name:  Yrrah Gaile A. Villarino
Age:  13
Grade level:  8
Email:  ygavillarino@brc.pshs.edu.ph
registration code:  CS2026
```

 **Actual Output:**

```
---------------------
REGISTRATION COMPLETE
---------------------
Name:  Yrrah Gaile A. Villarino
Age:  13
Grade level: 8
Email:   ygavillarino@brc.pshs.edu.ph
registration code:  CS2026
```

 **Result:** PASS

 **Explanation:**

 The actual output matches the expected output because all of the entered information meets the validation requirements, the name is not blank, the age is within the required range, the grade level is valid, the email contains `@` and `.`, and the registration code has exactly 6 characters.

---

 ## Verification Test 2

 **Input:**

```
Name: Yrrah Gaile A. Villarino
Age: thirteen
```

 **Expected Output:**

```
Age must be a number.
```

 **Actual Output:**

```
Age must be a number.
```

 **Result:** PASS

 **Explanation:**

 The actual output matches the expected output because `thirteen` is not a valid integer. The program catches the `ValueError` and displays the correct error message before stopping.

---

 ## Verification Test 3

 **Input:**

```
Name: Yrrah Gaile A. Villarino
Age: 13
Grade Level: 8
Email: studentpshs.edu.ph
```

 **Expected Output:**

```
Invalid.
```

 **Actual Output:**

```
Invalid.
```

 **Result:** PASS

 **Explanation:**

 The actual output matches the expected output because the email address does not contain the required `@` symbol. The program detects that the email does not meet its pattern requirement and stops the registration.

---

 # Reflection

 ### 1\. Why should a program validate input before processing it?

 A program should validate input before processing it to prevent incorrect or unexpected data from causing problems. It also makes sure that the information follows the requirements of the system.

 ### 2\. What is the difference between input validation and output verification?

 Input validation checks whether the information entered by the user is acceptable. Output verification checks whether the program produces the expected result after processing the input.

 ### 3\. Which validation technique was easiest for you to implement? Why?

 Presence validation was the easiest for me to implement because I only needed to check whether the student name was empty.

 ### 4\. Which validation technique was most challenging? Why?

 Data type validation was the most challenging because the program needs to handle situations where the user enters text instead of a number. I used `try` and `except ValueError` to handle this situation.

 ### 5\. How did testing invalid inputs help you improve your program?

 Testing invalid inputs helped me make sure that the program does not accept incorrect information. It also helped me check whether the correct error messages appear when users enter invalid data.

---

 # Files for This Activity

 - `workshop_validator.py`
- `input_validation.md`
- `workshop_validator_flowchart.png` if a flowchart was used

---

 ← Back to Main Portfolio
