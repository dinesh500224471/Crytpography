import random
import string
import time

def generate_random_text(length=20):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def caesar_cipher(text, shift):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            shifted_index = (ord(char) - ord('a' if char.islower() else 'A') + shift) % 26
            encrypted_text += chr(ord('a' if char.islower() else 'A') + shifted_index)
        else:
            encrypted_text += char
    return encrypted_text

def encrypt_decrypt_animation(text, shift):
    print("Original Text:", text)
    print("Shift:", shift)
    print("Encrypting...", end='\r')
    time.sleep(1)
    encrypted_text = caesar_cipher(text, shift)
    print(" " * 20, end='\r')
    print("Encrypted Text:", encrypted_text)
    print("Decrypting...", end='\r')
    time.sleep(1)
    decrypted_text = caesar_cipher(encrypted_text, -shift)
    print(" " * 20, end='\r')
    print("Decrypted Text:", decrypted_text)

def main():
    random_text = generate_random_text()
    shift = int(input("Enter the shift value: "))
    encrypt_decrypt_animation(random_text, shift)

if __name__ == "__main__":
    main()
