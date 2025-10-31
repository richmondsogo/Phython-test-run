import random
from colorama import init, Fore, Style  # For colored terminal output

# Initialize colorama for Windows terminal colors
init()

# Character sets for password generation
base_list_lowercase = list("abcdefghijklmnopqrstuvwxyz")
base_list_uppercase = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
base_list_numbers = list("0123456789")
base_list_characters = list("!@#$%^&*().")

def generate_password(length: int = 12) -> str:
    """
    Generates a secure password with at least one character from each character set.
    
    Args:
        length (int): Desired length of password (minimum 4)
    
    Returns:
        str: Generated password meeting security requirements
    
    Raises:
        ValueError: If length is less than 4
    """
    # Validate minimum length requirement
    if length < 4:
        raise ValueError(
            f"{Fore.RED}Password length must be at least 4 to include all character types{Style.RESET_ALL}"
        )
    
    # Ensure one character from each character set
    password = [
        random.choice(base_list_lowercase),   # Lowercase
        random.choice(base_list_uppercase),   # Uppercase
        random.choice(base_list_numbers),     # Number
        random.choice(base_list_characters)   # Special character
    ]
    
    # Combine all character sets for remaining characters
    all_characters = base_list_lowercase + base_list_uppercase + base_list_numbers + base_list_characters
    
    # Fill remaining length with random characters
    remaining_length = length - 4
    password.extend(random.choice(all_characters) for _ in range(remaining_length))
    
    # Shuffle password to randomize character positions
    random.shuffle(password)
    
    # Join characters into final password string
    return "".join(password)

def print_password_info(password: str) -> None:
    """
    Prints password information with formatting.
    
    Args:
        password (str): Generated password to display
    """
    print("\n" + "="*50)
    print(f"{Fore.CYAN}Generated Password:{Style.RESET_ALL} {Fore.GREEN}{password}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Password Length:{Style.RESET_ALL} {len(password)}")
    print("="*50 + "\n")

if __name__ == "__main__":
    try:
        password = generate_password(16)
        print_password_info(password)
    except ValueError as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")