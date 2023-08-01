import random
import string

def generate_password(length):
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password using the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        # Prompt the user to specify the desired length of the password
        desired_length = int(input("Enter the desired length of the password: "))

        # Generate the password
        password = generate_password(desired_length)

        # Display the generated password
        print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
