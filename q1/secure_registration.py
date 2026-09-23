# These are the accepted values
VALID_SECTIONS = [ "Diamond", "Emerald", "Jade", "Sapphire", "Dahlia", "Ilang-Ilang", "Rosal", "Sampaguita", "Berrylium","Magnesium", "Platinum", "Silicon", "Electron", "Gluon","Graviton", "Photon", "Biology", "Chemistry", "Physics","Bio-Chemistry"]

VALID_CLUBS = ["Robotics","Science","Mathematics", "Programming"]

VALID_ATTENDANCE = ["Present","Absent","Late"]


# This asks for your name
student_name = input("Student Name: ").strip()

if student_name == "":
    print("Error: Student name is required.")
    exit()


# This asks for your section which should only be within the accepted list of sections
section = input("Section: ").strip()

if section not in VALID_SECTIONS:
    print("Error: Please choose a valid section.")
    exit()


# This asks for your club and only accepts valid clubs
club = input("Club Choice: ").strip()

if club not in VALID_CLUBS:
    print("Error: Please choose a valid club.")
    exit()


# This asks for your email which needs to have an @
email = input("School Email: ").strip()

if "@" not in email:
    print("Error: Please enter a valid school email.")
    exit()


# This is for checking your attendance status
attendance = input("Attendance Status: ").strip()

if attendance not in VALID_ATTENDANCE:
    print("Error: Please enter a valid attendance status.")
    exit()


# If this appears then that means you filled it out correctly yaey
print("--------------------------------")
print("REGISTRATION ACCEPTED")
print("--------------------------------")
print(f"Student: {student_name}")
print(f"Section: {section}")
print(f"Club: {club}")
print(f"Email: {email}")
print(f"Attendance: {attendance}")
