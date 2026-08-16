import math

# Get coordinates from the user and convert inputs into floating-point numbers
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Calculate the squared differences using math.pow()
x_diff_squared = math.pow(x2 - x1, 2)
y_diff_squared = math.pow(y2 - y1, 2)

# Calculate the Euclidean distance using math.sqrt()
distance = math.sqrt(x_diff_squared + y_diff_squared)

# Display the distance rounded to 2 decimal places
print(f"The distance between ({x1}, {y1}) and ({x2}, {y2}) is {distance:.2f}")

# REFLECTION

# Through this activity, I learned how to use Python's math library functions like math.sqrt() and math.pow() to solve mathematical formulas in code.
# Breaking down the Euclidean distance formula into smaller steps helped me convert user inputs into numbers and calculate the correct result smoothly.

#Using built-in libraries like Python's math module saves time, prevents bugs, and keeps code clean and readable. 

# How did the math library simplify your program?
# Instead of writing long, complex algorithms to calculate exponents or roots, 
# importing math gave immediate access to pre-tested, highly accurate functions.
#
# How did sqrt() and pow() help you?
# They handled the mathematical lifting directly. math.pow() calculated the squared differences, while math.sqrt() calculated the final square root to complete the Euclidean distance formula smoothly.

# What would you need to do if these functions were not available?
# Without these functions, custom algorithms would be required. 
#For example, finding a square root without math.sqrt() requires writing an iterative method like Newton's method using loops, making the code much longer and prone to errors.
