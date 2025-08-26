import random
import string

def generate_password():
    """
    Generates a random 8-character password with:
    - 2 uppercase letters
    - 2 lowercase letters
    - 2 digits
    - 2 special characters
    """
    
    # Define the character sets to choose from
    upper_letters = string.ascii_uppercase
    lower_letters = string.ascii_lowercase
    numbers = string.digits
    special_chars = string.punctuation

    # Choose 2 random characters from each set
    pass_upper = [random.choice(upper_letters) for _ in range(2)]
    pass_lower = [random.choice(lower_letters) for _ in range(2)]
    pass_num = [random.choice(numbers) for _ in range(2)]
    pass_char = [random.choice(special_chars) for _ in range(2)]

    # Combine all the chosen characters into a single list
    password_list = pass_upper + pass_lower + pass_num + pass_char

    # Shuffle the list to mix up the character order
    random.shuffle(password_list)

    # Join the list of characters into a single string
    final_password = "".join(password_list)
    
    return final_password

# --- Main part of the script ---
if __name__ == "__main__":
    # Generate a new password by calling the function
    new_password = generate_password()
    
    # Print the generated password
    print(f"Your new password is: {new_password}")