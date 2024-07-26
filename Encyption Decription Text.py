from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64
import random
import string

def generate_random_key(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def encrypt_aes(plain_text, key):
    key = key.ljust(16)[:16].encode('utf-8')
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_text = pad(plain_text.encode('utf-8'), AES.block_size)
    cipher_text = cipher.encrypt(padded_text)
    return base64.b64encode(iv + cipher_text).decode('utf-8')

def decrypt_aes(cipher_text, key):
    key = key.ljust(16)[:16].encode('utf-8')
    cipher_text = base64.b64decode(cipher_text.encode('utf-8'))
    iv = cipher_text[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    actual_cipher_text = cipher_text[16:]
    padded_plain_text = cipher.decrypt(actual_cipher_text)
    return unpad(padded_plain_text, AES.block_size).decode('utf-8')

if __name__ == "__main__":
    while True:
        choice = input("Do you want to encrypt or decrypt? (E/D or Q to quit): ").strip().upper()

        if choice == 'E':
            plain_text = input("Enter the text you want to encrypt: ").strip()
            try:
                key_length = int(input("Enter the desired length of the encryption key (max 16): ").strip())
                key_length = min(16, max(1, key_length))  # Ensure key length is between 1 and 16
                key = generate_random_key(key_length)
                encrypted_text = encrypt_aes(plain_text, key)
                print(f"Encrypted Text: {encrypted_text}")
                print(f"Encryption Key: {key}")
            except ValueError:
                print("Invalid key length. Please enter an integer value between 1 and 16.")

        elif choice == 'D':
            encrypted_text = input("Enter the text you want to decrypt: ").strip()
            key = input("Enter the encryption key: ").strip()
            try:
                decrypted_text = decrypt_aes(encrypted_text, key)
                print(f"Decrypted Text: {decrypted_text}")
            except Exception as e:
                print("Decryption failed. The key might be incorrect or the data may be corrupted.")
        
        elif choice == 'Q':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 'E' for encryption, 'D' for decryption, or 'Q' to quit.")
