from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(filename):
    key = load_key()
    f = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()

    encrypted_data = f.encrypt(data)

    with open(filename + ".enc", "wb") as file:
        file.write(encrypted_data)

    print("File encrypted successfully!")

def decrypt_file(filename):
    key = load_key()
    f = Fernet(key)

    with open(filename, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)

    with open(filename.replace(".enc", ""), "wb") as file:
        file.write(decrypted_data)

    print("File decrypted successfully!")

print("""
1. Generate Key
2. Encrypt File
3. Decrypt File
""")

choice = input("Select option: ")

if choice == "1":
    generate_key()
    print("Key generated and saved as secret.key")

elif choice == "2":
    file = input("Enter file name to encrypt: ")
    encrypt_file(file)

elif choice == "3":
    file = input("Enter file name to decrypt: ")
    decrypt_file(file)

else:
    print("Invalid option")
