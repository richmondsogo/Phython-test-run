import random

base_list = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()")

def generate_password(length=12):
    return ''.join(random.choice(base_list) for _ in range(length))

if __name__ == "__main__":
    print("Generated Password:", generate_password(16))
    
    
