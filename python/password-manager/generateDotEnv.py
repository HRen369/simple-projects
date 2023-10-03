from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def main():
    key = get_random_bytes(32)
    iv = get_random_bytes(16)

    print(key.hex())
    print(iv.hex())


if __name__ == "__main__":
    main()
