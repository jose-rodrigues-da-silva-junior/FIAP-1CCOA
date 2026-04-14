""" 
Exercise 1: 
Write a program that displays a menu of options to the user. 
The user can choose an option by entering a number. 
The program should then display a message based on the user's choice.
"""

print(f"""
0 - EXIT
1 - REGISTER USER
2 - CONSULT USER
3 - EDIT USER
4 - DEACTIVATE USER
""")

# variable to store the user's choice
choice = int(input("Enter your choice: "))

if choice == 0:
    print("Exiting the program...\n")
elif choice == 1:
    print("You chose to register a user.\n")
elif choice == 2:
    print("You chose to consult a user.\n")
elif choice == 3:           
    print("You chose to edit a user.\n")
elif choice == 4:
    print("You chose to deactivate a user.\n")
else:
    print("Invalid choice. Please enter a number between 0 and 4.\n")