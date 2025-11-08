import random
import string

def generate_password(length):
    """
    Generates a random and strong password of the specified length.
    """
    # Define Character Sets
    lower_letters = string.ascii_lowercase
    upper_letters = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation
    
    # Create the entire pool
    character_pool = lower_letters + upper_letters + numbers + special_characters

    if length < 4:
        print("Warning: Password length should be at least 4.")
        return None
    
    # Make Random Selection
    password_list = random.sample(character_pool, length)
    
    # Join the Password
    password = "".join(password_list)
    
    return password

if __name__ == "__main__":
    print("✨ PYTHON STRONG PASSWORD GENERATOR (EN) ✨")
    
    try:
        desired_length = int(input("Enter the desired password length (Ex: 12): "))
        
        new_password = generate_password(desired_length)
        
        if new_password:
            print("\n-------------------------------------")
            print(f"Generated Strong Password: **{new_password}**")
            print("-------------------------------------")
            
    except ValueError:
        print("\nERROR: Please enter a valid number.")