import os

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def main():
    if os.path.isfile('.env'):
        print("There already exists a .env file.")
        print("Delete your .env file to generate a new one")
    else:
        key = get_random_bytes(32)
        iv = get_random_bytes(16)

        keyHex = key.hex()
        ivHex = iv.hex()

        with open(".env","w") as file:
            file.write('MASTER_FILE_NAME="encryptedMasterFile"\n')
            file.write(f'KEY={keyHex}\n')
            file.write(f'IV={ivHex}\n')
            file.write(f'MASTER_PASSWORD="default"\n')

if __name__ == "__main__":
    main()
