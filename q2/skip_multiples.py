# I used a for loop to display numbers from 1 to 15
for i in range(1, 16):

    # This checks if the number is divisible by 3 using the % operator
    if i % 3 == 0:
        continue  # Skip the number if it is a multiple of 3

    # This displays the number if it is not a multiple of 3
    print(i)
