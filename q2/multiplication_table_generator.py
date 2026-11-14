# ok so I created a function to display the multiplication table
def show_table(number):

    # Use a for loop to multiply the number from 1 to 10
    for i in range(1, 11):

        # Multiply the given number by the current value of i
        result = number * i

        # Display the multiplication and its answer
        print(number, "x", i, "=", result)


# Then, this asks the user to enter a number
num = int(input("Enter a number: "))

# This displays the multiplication table using the number entered by the user
show_table(num)
