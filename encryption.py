"""
Simple reversible cipher.

How it works:
- The message is reversed, then each character's Unicode code point
  is transformed using two random keys: ((ord(c) / 2) + key1 - key2) / 2
- Decryption reverses that formula, then reverses the string back.

Note: this is a toy cipher for learning purposes, not a secure
encryption scheme. Don't use it to protect anything sensitive.
"""

import random


def generate_keys() -> tuple[int, int]:
    """Generate a random pair of encryption keys."""
    key1 = random.randint(5000, 9999)
    key2 = random.randint(200, 4000)
    return key1, key2


def encrypt(message: str, key1: int, key2: int) -> str:
    """Encrypt a message using the two given keys."""
    reversed_msg = message[::-1]
    values = [str((ord(ch) / 2 + key1 - key2) / 2) for ch in reversed_msg]
    return " ".join(values)


def decrypt(cipher: str, key1: int, key2: int) -> str:
    """Decrypt a cipher string produced by encrypt(), using the same keys."""
    tokens = cipher.split()
    chars = [chr(int((float(tok) * 2 - key1 + key2) * 2)) for tok in tokens]
    return "".join(reversed(chars))


def get_operation() -> int:
    """Ask the user whether they want to encrypt or decrypt."""
    while True:
        choice = input("Encrypt [1] | Decrypt [2]: ").strip()
        if choice in ("1", "2"):
            return int(choice)
        print("Please enter 1 or 2.")


def get_int(prompt: str) -> int:
    """Ask the user for an integer, re-prompting until they give one."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid whole number.")


def run_encrypt() -> None:
    message = input("Enter your message to encrypt: ")
    key1, key2 = generate_keys()
    cipher = encrypt(message, key1, key2)
    print(f"\nEncrypted message: {cipher}")
    print(f"Keys — key1: {key1} | key2: {key2}")
    print("Keep these keys safe, you'll need them to decrypt!\n")


def run_decrypt() -> None:
    cipher = input("Enter the encrypted message: ")
    key1 = get_int("key 1: ")
    key2 = get_int("key 2: ")
    try:
        message = decrypt(cipher, key1, key2)
        print(f"\nDecrypted message: {message}\n")
    except (ValueError, IndexError):
        print("\nCouldn't decrypt that — check the message and keys and try again.\n")


def main() -> None:
    while True:
        op = get_operation()
        if op == 1:
            run_encrypt()
        else:
            run_decrypt()

        again = input("Encrypt/decrypt another message? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
