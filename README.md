# AES Encryption and Decryption Tool

This Python script provides a simple command-line interface for encrypting and decrypting text using the Advanced Encryption Standard (AES). Users can choose to encrypt a message, generate a random encryption key, and then decrypt the message using the provided key. The tool ensures ease of use with robust input validation and an interactive loop for continuous use.

## Features

- **Encrypt Text**: Users can input any text to be encrypted with AES.
- **Generate Random Key**: A random encryption key of user-specified length (up to 16 characters) is generated for the encryption process.
- **Decrypt Text**: Users can decrypt the encrypted text using the provided key.
- **Input Validation**: The program validates user inputs for encryption, decryption, and key length to ensure proper functionality.
- **Interactive Loop**: The tool allows continuous use without terminating on invalid inputs, and includes an option to quit.

## Requirements

- Python 3.x
- PyCryptodome library

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/AnonymousI0I/AES-Encryption-Decryption.git
    cd AES-Encryption-Decryption
    ```

2. **Install the required libraries**:

    ```bash
    pip install pycryptodome
    ```

## Usage

1. **Run the script**:

    ```bash
    python Encyption Decription Text.py
    ```

2. **Follow the on-screen prompts to encrypt or decrypt text**.

### Example Usage

#### Encrypting Text

- You will be prompted to enter the text you want to encrypt and the desired length of the encryption key (up to 16 characters).

    Example:

    ```
    Do you want to encrypt or decrypt? (E/D or Q to quit): E
    Enter the text you want to encrypt: Hello, world!
    Enter the desired length of the encryption key (max 16): 8
    Encrypted Text: bV1s8nZ2aFdFYXlJdVp2dA==
    Encryption Key: aBcD1234
    ```

#### Decrypting Text

- You will be prompted to enter the encrypted text and the encryption key.

    Example:

    ```
    Do you want to encrypt or decrypt? (E/D or Q to quit): D
    Enter the text you want to decrypt: bV1s8nZ2aFdFYXlJdVp2dA==
    Enter the encryption key: aBcD1234
    Decrypted Text: Hello, world!
    ```

## Code Overview

### Function Descriptions

#### `generate_random_key(length)`

Generates a random key of the specified length using letters and digits.

- **Parameters**:
  - `length` (int): The desired length of the key.
- **Returns**:
  - `str`: The generated random key.

#### `encrypt_aes(plain_text, key)`

Encrypts the given plain text using AES encryption with the provided key.

- **Parameters**:
  - `plain_text` (str): The text to be encrypted.
  - `key` (str): The encryption key.
- **Returns**:
  - `str`: The encrypted text encoded in base64.

#### `decrypt_aes(cipher_text, key)`

Decrypts the given cipher text using AES encryption with the provided key.

- **Parameters**:
  - `cipher_text` (str): The text to be decrypted.
  - `key` (str): The encryption key.
- **Returns**:
  - `str`: The decrypted text.

### Main Function

The `main()` function orchestrates the workflow by prompting the user for inputs, calling the respective functions to perform encryption or decryption, and displaying the results.

## Contribution

Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request.
