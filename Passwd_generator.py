import random
import string

def generate_password():
    print("Password Generator")
    
    # Input: Password length
    try:
        length = int(input("Enter the desired password length: "))
        if length < 1:
            print("Password length must be greater than 0.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Input: Password complexity
    print("Select the complexity level:")
    print("1. Letters only (lowercase and uppercase)")
    print("2. Letters and digits")
    print("3. Letters, digits, and special characters")
    complexity = input("Enter your choice (1/2/3): ")

    # Define character sets based on complexity choice
    if complexity == '1':
        chars = string.ascii_letters
    elif complexity == '2':
        chars = string.ascii_letters + string.digits
    elif complexity == '3':
        chars = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid complexity choice. Please try again.")
        return

    # Generate password
    password = ''.join(random.choice(chars) for _ in range(length))
    print(f"Generated password: {password}")

# Run the password generator
generate_password()
