import random
import string

def generate_cipher():
    """Generates a random substitution cipher mapping and its reverse."""
    letters = list(string.ascii_uppercase)
    shuffled = letters[:]
    random.shuffle(shuffled)
    encrypt_map = dict(zip(letters, shuffled))
    decrypt_map = {v: k for k, v in encrypt_map.items()}
    return encrypt_map, decrypt_map

def transform(text, cipher_map):
    """Encrypts or decrypts the text based on the provided cipher map."""
    text = text.upper()
    result = ''
    for char in text:
        if char in cipher_map:
            result += cipher_map[char]
        else:
            result += char  # preserve non-alphabetic characters
    return result

def main():
    encrypt_map, decrypt_map = generate_cipher()

    print("Random Cipher Mapping:")
    for k, v in encrypt_map.items():
        print(f"{k} -> {v}")

    message = input("\nEnter the message to encrypt: ")
    encrypted = transform(message, encrypt_map)
    print(f"\nEncrypted Message:\n{encrypted}")

    decrypted = transform(encrypted, decrypt_map)
    print(f"\nDecrypted Message:\n{decrypted}")

if __name__ == "__main__":
    main()
