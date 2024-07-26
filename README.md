# AES Encryption and Decryption Tool

This Python project provides a simple command-line interface for encrypting and decrypting text using the Advanced Encryption Standard (AES). Users can choose to encrypt a message, generate a random encryption key, and then decrypt the message using the provided key. The tool ensures ease of use with robust input validation and an interactive loop for continuous use.

## Features

- **Encrypt Text**: Users can input any text to be encrypted with AES.
- **Generate Random Key**: A random encryption key of user-specified length (up to 16 characters) is generated for the encryption process.
- **Decrypt Text**: Users can decrypt the encrypted text using the provided key.
- **Input Validation**: The program validates user inputs for encryption, decryption, and key length to ensure proper functionality.
- **Interactive Loop**: The tool allows continuous use without terminating on invalid inputs, and includes an option to quit.

## Installation

Clone the repository:
```bash
git clone https://github.com/your-username/aes-encryption-decryption-tool.git
cd aes-encryption-decryption-tool
Install the required library:

bash
Copy code
pip install pycryptodome
Usage
Run the script using Python:

bash
Copy code
python encryption_decryption.py
Follow the on-screen prompts to encrypt or decrypt text.

Example
plaintext
Copy code
Do you want to encrypt or decrypt? (E/D or Q to quit): E
Enter the text you want to encrypt: Hello, world!
Enter the desired length of the encryption key (max 16): 8
Encrypted Text: W2cYEVkr1pvLZcdRWbKmnQ==
Encryption Key: aBcD1234

Do you want to encrypt or decrypt? (E/D or Q to quit): D
Enter the text you want to decrypt: W2cYEVkr1pvLZcdRWbKmnQ==
Enter the encryption key: aBcD1234
Decrypted Text: Hello, world!

Do you want to encrypt or decrypt? (E/D or Q to quit): Q
Exiting the program. Goodbye!

Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.
