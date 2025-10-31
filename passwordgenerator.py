import random

base_list_lowercase = list("abcdefghijklmnopqrstuvwxyz")
base_list_uppercase = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
base_list_numbers = list("0123456789")
base_list_characters = list("!@#$%^&*().")

# def generate_password(length=12):
#     all_characters = base_list_lowercase + base_list_uppercase + base_list_numbers + base_list_characters
#     password = "".join(random.choice(all_characters) for _ in range(length))
#     return password

# # def generate_password(length=12):
# #     part_one = "".join((random.choice(base_list_uppercase) for _ in range(length // 4)))
# #     part_two = "".join((random.choice(base_list_numbers) for _ in range(length // 4)))
# #     part_three ="".join((random.choice(base_list_characters) for _ in range(length // 4)))
# #     part_four = "".join((random.choice(base_list_lowercase) for _ in range(length // 4)))
# #     return part_one+part_two+part_three+part_four
    11

# base_list_lowercase = list("abcdefghijklmnopqrstuvwxyz")
# base_list_uppercase = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
# base_list_numbers = list("0123456789")
# base_list_characters = list("!@#$%^&*().")

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length must be at least 4 to include all character types")
    
    # Ensure one character from each list
    password = [
        random.choice(base_list_lowercase),
        random.choice(base_list_uppercase),
        random.choice(base_list_numbers),
        random.choice(base_list_characters)
    ]
    
    # Fill the rest of the password
    all_characters = base_list_lowercase + base_list_uppercase + base_list_numbers + base_list_characters
    remaining_length = length - 4
    password.extend(random.choice(all_characters) for _ in range(remaining_length))
    
    # Shuffle the password to make it more random
    random.shuffle(password)
    return "".join(password)

if __name__ == "__main__":
    print("Generated Password:", generate_password(16))

# if __name__ == "__main__":
#     print("Generated Password:", generate_password(16))
# 1