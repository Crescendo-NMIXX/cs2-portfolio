# 1.Student Name - Presence Validation
#This asks for the student's name.
studentname = str(input("Please input your name:"))
if not studentname:
  print("Student name is required")
  raise SystemExit

# 2. Age - Data Type + Range Validation

else:
   #This asks the student to enter their age, but the age should be from 11 to 18.
    try:
        age = int(input("Please input your age: "))
        
        if age < 11 or age > 18:
            print("Age must be from 11 to 18.")
            raise SystemExit
    #This is what will be displayed if the student puts a word or
    except ValueError:
        print("Age must be a number.")
        raise SystemExit

# 3. Grade Level - Acceptable Value Validation
try:
    #This asks the student for their grade level, and it has to be from grade 7 to 12.
    gradelevel = int(input("Please input your grade level: "))
    
   
    if gradelevel < 7 or gradelevel > 12:
        print("Invalid grade level.")
        raise SystemExit
      
except ValueError:
    #This is what will be shown when the student inputs a grade that is not in the given range.
    print("Invalid grade level. Please enter a number.")
    raise SystemExit
  
  # 4. Email - Simple Pattern Validation

email = input("Please input your email: ")

#This asks the student to enter their email and it must contain "@" and "." or else it's invalid.
if "@" in email and "." in email:
    pass 
else:
    print("Invalid.")
    raise SystemExit
      

 # 5. Registration Code - Length Validation
#This asks the student to enter their registration code and it must be only 6 characters long.
try:
  registrationcode = str(input("Please input your registration code: "))
  if len(registrationcode) != 6:
    print("The registration code must contain exactly 6 characters.")
    raise SystemExit
    
#This is what will be displayed when the entered registration code is less than or more than 6 characters.
except ValueError:
  print("The registration code must contain exactly 6 characters.")
  raise SystemExit
 
print ("---------------------")
print ("REGISTRATION COMPLETE")
print ("---------------------")
print("Name: ", studentname)
print("Age: ", age)
print("Grade level: ", gradelevel)
print("Email: ", email)
print("registration code: ", registrationcode)
