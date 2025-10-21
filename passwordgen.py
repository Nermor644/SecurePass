import random
import string

def generate_password(length=12, use_symbols=True):
    chars = string.ascii_letters + string.digits
    if use_symbols:
        chars += string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def main():
    print("Welcome to Password Generator! 🔐")
    length = input("Enter password length (default 12): ")
    length = int(length) if length.isdigit() else 12

    symbols = input("Include symbols? (y/n, default y): ").lower()
    use_symbols = False if symbols == 'n' else True

    password = generate_password(length, use_symbols)
    print(f"\nYour generated password: {password}")

if __name__ == "__main__":
    main()
