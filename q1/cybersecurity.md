# Fundamentals of Cybersecurity and Data Privacy

**Activity:** PSHS Secure Club Registration System
**Name:** Your Name
**Section:** Your Section
**Quarter:** 1

---

Activity Overview

In this activity, I analyzed a cybersecurity threat and developed secure data-capture rules for a simple
PSHS Club Registration System.
The goal is to create a program that collects only necessary information and accepts only correct,
expected, and appropriate input.

---

# Part A - Cybersecurity Threat Analysis
##Assigned Case
**Case 1**
**Fake Login Alert**

>The student receives a message claiming that their account will be disabled. The message asks the student to click a link and enter their username and password. This is a phishing attempt designed to trick the user into giving away their account information.

### 1. What cybersecurity threat is shown?

>The threat shown is phishing. The attacker uses a fake message to trick the student into providing their username and password.

### 2. What warning signs make the situation suspicious?

>The situation is suspicious because the message creates a sense of urgency by saying that the account will be disabled. It also asks the student to click an unfamiliar link and provide their login information. Legitimate organizations should not require users to enter sensitive information through suspicious links.

###3. What may be affected?

The following may be affected:

Data

Account

Application

Device

Network

>The student's account could be accessed if the username and password are stolen. Personal information stored in the account could also be exposed or misused.

### 4. What information could be exposed or misused?

>The student's username, password, school account, personal information, school files, messages, and other information connected to the account could potentially be exposed or misused.

### 5. What should the user do to reduce the risk?

>The user should not click the suspicious link or enter their username and password. They should verify the message through an official school website or contact the school or teacher directly. If the student already entered their password, they should report the incident and change their password through the official account system.

---

# Part B - Data Privacy and Secure Data Capture

A proposed Club Registration System wants to collect the following information. Determine whether each item is really necessary.

| Data | Collect / Do Not Collect | Reason |
|---|---|---|
| Student Name | COLLECT | Needed to identify the student who registered. |
| Section | COLLECT | Needed to identify the student's section. |
| Club Choice | COLLECT | Needed to know which club the student selected. |
| School Email | COLLECT | Needed for school-related identification or communication. |
| Attendance Status | COLLECT | Required for the registration record. |
| Password | DO NOT COLLECT | Unnecessary for a simple club registration system. |
| OTP | DO NOT COLLECT | Unnecessary because the system does not require account verification. |
| Home Address | DO NOT COLLECT | Unnecessary and is private personal information. |
| Parent Bank Account | DO NOT COLLECT | Unnecessary and highly sensitive financial information. |


## Privacy Question

Why is it safer to collect only information that the program actually needs?

>It is safer to collect only necessary information because collecting extra personal information increases the amount of data that could be exposed or misused. Data minimization helps protect privacy and reduces the possible impact of a security incident. A club registration system only needs information related to the registration, so passwords, OTPs, home addresses, and banking information should not be collected.

---

# Part C - Security-Focused Validation Rules

| Data Captured | Expected Input | Possible Risk | Invalid Input Example | Validation Rule | Error Message |
|---------------|---|---|---|---|
| Student Name  | Student's name | Missing or incomplete information | `[blank]` | Must not be blank. | Error: Student name is required. |
| Section | One of the accepted sections | Incorrect section information | `Gaming` | Must match one of the accepted sections. | Error: Please choose a valid section. |
| Club Choice | Robotics, Science, Mathematics, Programming | Invalid club selection | `Gaming` | Must match one of the accepted clubs. | Error: Please choose a valid club. |
| School Email | School email containing `@` and `.` | Incorrect email format | `studentpshs.edu.ph` | Must contain both `@` and `.`. | Error: Please enter a valid school email. |
| Attendance Status | Present, Absent, Late | Incorrect attendance information | `Maybe` | Must match one of the accepted attendance statuses. | Error: Please enter a valid attendance status. |


## Secure Data Capture Questions

### 1. What should your program accept?

>The program should accept a non-blank student name, one of the approved sections, one of the approved clubs, a school email containing @ and ., and one of the approved attendance statuses: Present, Absent, or Late.

### 2. What should your program reject?

>The program should reject blank names, sections that are not on the approved list, clubs that are not on the approved list, emails without @ or ., and attendance statuses that are not Present, Absent, or Late.

### 3. How do your validation rules help reduce incorrect or unsafe input?

>Validation rules help prevent incorrect information from being accepted by the program. They make sure that required fields are filled in and that choices match the values expected by the system. This improves data quality and reduces errors.

---

# Part D - Secure Program Implementation
## Program

The program collects only:

Student Name

Section

Club Choice

School Email

Attendance Status

It does not request passwords, OTPs, banking information, home addresses, or other unnecessary personal information.

##Source Code File

[`secure_registration.py`](secure_registration.py)

## Final Code
# These are the accepted values
VALID_SECTIONS = [
    "Diamond", "Emerald", "Jade", "Sapphire", "Dahlia",
    "Ilang-Ilang", "Rosal", "Sampaguita", "Berrylium",
    "Magnesium", "Platinum", "Silicon", "Electron", "Gluon",
    "Graviton", "Photon", "Biology", "Chemistry", "Physics",
    "Bio-Chemistry"
]

VALID_CLUBS = ["Robotics", "Science", "Mathematics", "Programming"]

VALID_ATTENDANCE = ["Present", "Absent", "Late"]


# This asks for your name
student_name = input("Student Name: ").strip()

if student_name == "":
    print("Error: Student name is required.")
    exit()


# This asks for your section which should only be within
# the accepted list of sections
section = input("Section: ").strip()

if section not in VALID_SECTIONS:
    print("Error: Please choose a valid section.")
    exit()


# This asks for your club and only accepts valid clubs
club = input("Club Choice: ").strip()

if club not in VALID_CLUBS:
    print("Error: Please choose a valid club.")
    exit()


# This asks for your email which needs to have
# both an @ and a .
email = input("School Email: ").strip()

if "@" not in email or "." not in email:
    print("Error: Please enter a valid school email.")
    exit()


# This is for checking your attendance status
attendance = input("Attendance Status: ").strip()

if attendance not in VALID_ATTENDANCE:
    print("Error: Please enter a valid attendance status.")
    exit()


# If this appears then that means you filled it out correctly
print("--------------------------------")
print("REGISTRATION ACCEPTED")
print("--------------------------------")
print(f"Student: {student_name}")
print(f"Section: {section}")
print(f"Club: {club}")
print(f"Email: {email}")
print(f"Attendance: {attendance}")

Security Practices Applied
Required Input

I used .strip() to remove unnecessary spaces and checked whether the student name was blank. If the name is blank, the program rejects the input and displays an error message.

Allowed Values

Section, club choice, and attendance status use predefined lists. The program checks whether the user's input is included in the accepted values before continuing.

Format Check

The school email is checked to make sure it contains both @ and .. If either character is missing, the program rejects the email.

Error Messages

Clear error messages tell the user what information is incorrect. This makes the program easier to understand and helps the user correct their input.

Data Minimization

I intentionally did not collect passwords, OTPs, home addresses, or banking information because they are unnecessary for a simple club registration system. Collecting only necessary information helps reduce privacy and security risks.

# Part E - Testing and Reflection
## Testing
| Test | Input Situation | Expected Output | Actual Output | Result |
|---:|---|---|---|---|
| 1 | All data valid | Registration accepted | Registration accepted | PASS |
| 2 | Blank student name | Student name is rejected | Error: Student name is required. | PASS |
| 3 | Invalid section | Section is rejected | Error: Please choose a valid section. | PASS |
| 4 | Invalid club choice | Club choice is rejected | Error: Please choose a valid club. | PASS |
| 5 | Email missing `@` | Email is rejected | Error: Please enter a valid school email. | PASS |
| 6 | Email missing `.` | Email is rejected | Error: Please enter a valid school email. | PASS |
| 7 | Invalid attendance status | Attendance status is rejected | Error: Please enter a valid attendance status. | PASS |
| 8 | Different valid inputs | Registration accepted | Registration accepted | PASS |


Test 1 – All fields valid

Student Name: Ana Cruz
Section: Dahlia
Club Choice: Programming
School Email: ana@pshs.edu.ph
Attendance Status: Present


Expected:

--------------------------------
REGISTRATION ACCEPTED
--------------------------------
Student: Ana Cruz
Section: Dahlia
Club: Programming
Email: ana@pshs.edu.ph
Attendance: Present


Test 2 – Blank name

Student Name:


Expected:

Error: Student name is required.


Test 3 – Invalid section

Section: Gaming


Expected:

Error: Please choose a valid section.


Test 4 – Invalid club

Club Choice: Gaming


Expected:

Error: Please choose a valid club.


Test 5 – Email missing @

School Email: studentpshs.edu.ph


Expected:

Error: Please enter a valid school email.


Test 6 – Email missing .

School Email: student@pshseduph


Expected:

Error: Please enter a valid school email.


Test 7 – Invalid attendance

Attendance Status: Maybe


Expected:

Error: Please enter a valid attendance status.


Test 8 – Different valid inputs

Student Name: Juan Dela Cruz
Section: Physics
Club Choice: Science
School Email: juan@pshs.edu.ph
Attendance Status: Late


Expected:

--------------------------------
REGISTRATION ACCEPTED
--------------------------------
Student: Juan Dela Cruz
Section: Physics
Club: Science
Email: juan@pshs.edu.ph
Attendance: Late

# Reflection
### 1. What is one cybersecurity threat that can affect an application or user?

>One cybersecurity threat that can affect an application or user is phishing. Phishing uses fake messages or websites to trick users into giving away information such as usernames, passwords, or other personal data.

### 2. How can users reduce the risk of phishing or suspicious messages?

>Users can reduce the risk by avoiding suspicious links and attachments, checking the sender, looking for unusual requests, and verifying messages through official sources. Users should also avoid entering passwords or other sensitive information into unfamiliar websites.

### 3. How can validation rules improve the security of user input?

>Validation rules make sure that the program accepts only expected information. They can prevent blank, incorrect, or unexpected values from being processed and help maintain accurate data.

### 4. Why should a program avoid collecting unnecessary personal information?

>A program should avoid collecting unnecessary personal information because extra data creates additional privacy and security risks. If the information is not needed, there is no reason for the system to store it.

### 5. How did SG7's input validation concepts become security practices in SG8?

>The input validation concepts from SG7 became security practices in SG8 by using rules to control what information the program accepts. Instead of simply making the program work, I also considered data privacy, data minimization, acceptable values, format checking, and clear error handling. These practices help make the program safer and more reliable.

Files for This Activity

[`secure_registration.py`](secure_registration.py)

cybersecurity.md

← Back to Main Portfolio
