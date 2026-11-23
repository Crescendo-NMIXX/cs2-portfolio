# this is a list containing five travel destinations
destinations = ["Cebu", "Manila", "Davao", "Baguio", "Palawan"]

# Display all destinations using a for loop
print("Travel Destinations:")
for place in destinations:
    print(place)

# I used slicing to display items from index 1 up to index 4
print("\nDestinations from index 1 to 3:")
print(destinations[1:4])

# this asks the user to enter a destination to search for
search = input("\nEnter a destination to search: ")

# this checks if the entered destination exists in the list
if search in destinations:
    print(search, "exists in the list.")
else:
    print(search, "does not exist in the list.")

# replaces the item at index 2 with Iloilo 
destinations[2] = "Iloilo"

# this displays the updated list of destinations 
print("\nUpdated Travel Destinations:")
print(destinations)
