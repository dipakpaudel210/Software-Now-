# Text Encryption and Decryption Program

def encrypt(text, shift1, shift2):
    result = ""
    for ch in text:
        if 'a' <= ch <= 'z':   # lowercase
            pos = ord(ch) - ord('a')
            if pos <= 12:      # a-m
                new_pos = (pos + shift1 * shift2) % 26
                result += chr(new_pos + ord('a')) + '\x00'   # marker for first half
            else:              # n-z
                new_pos = (pos - (shift1 + shift2)) % 26
                result += chr(new_pos + ord('a')) + '\x01'   # marker for second half

        elif 'A' <= ch <= 'Z':  # uppercase
            pos = ord(ch) - ord('A')
            if pos <= 12:       # A-M
                new_pos = (pos - shift1) % 26
                result += chr(new_pos + ord('A')) + '\x00'
            else:               # N-Z
                new_pos = (pos + (shift2 ** 2)) % 26
                result += chr(new_pos + ord('A')) + '\x01'

        else:   # keep other characters
            result += ch

    return result


def decrypt(text, shift1, shift2):
    result = ""
    i = 0
    while i < len(text):
        ch = text[i]

        if 'a' <= ch <= 'z':   # lowercase
            if i + 1 < len(text) and text[i+1] == '\x00':   # first half originally
                pos = ord(ch) - ord('a')
                new_pos = (pos - shift1 * shift2) % 26
                result += chr(new_pos + ord('a'))
                i += 2
            elif i + 1 < len(text) and text[i+1] == '\x01': # second half originally
                pos = ord(ch) - ord('a')
                new_pos = (pos + (shift1 + shift2)) % 26
                result += chr(new_pos + ord('a'))
                i += 2
            else:
                result += ch
                i += 1

        elif 'A' <= ch <= 'Z':  # uppercase
            if i + 1 < len(text) and text[i+1] == '\x00':   # first half originally
                pos = ord(ch) - ord('A')
                new_pos = (pos + shift1) % 26
                result += chr(new_pos + ord('A'))
                i += 2
            elif i + 1 < len(text) and text[i+1] == '\x01': # second half originally
                pos = ord(ch) - ord('A')
                new_pos = (pos - (shift2 ** 2)) % 26
                result += chr(new_pos + ord('A'))
                i += 2
            else:
                result += ch
                i += 1

        else:
            result += ch
            i += 1

    return result


def encrypt_file(shift1, shift2):
    try:
        with open(r'C:\Users\dipak\Desktop\Software now\raw_text.txt', 'r', encoding='utf-8') as f:
            text = f.read()

        encrypted = encrypt(text, shift1, shift2)

        with open(r'C:\Users\dipak\Desktop\Software now\encrypted_text.txt', 'w', encoding='utf-8') as f:
            f.write(encrypted)

        print("Encryption completed!")

    except FileNotFoundError:
        print("raw_text.txt not found.")
    except Exception as e:
        print("Error during encryption:", e)


def decrypt_file(shift1, shift2):
    try:
        with open(r'C:\Users\dipak\Desktop\Software now\encrypted_text.txt', 'r', encoding='utf-8') as f:
            encrypted = f.read()

        decrypted = decrypt(encrypted, shift1, shift2)

        with open(r'C:\Users\dipak\Desktop\Software now\decrypted_text.txt', 'w', encoding='utf-8') as f:
            f.write(decrypted)

        print("Decryption completed!")

    except FileNotFoundError:
        print("encrypted_text.txt not found.")
    except Exception as e:
        print("Error during decryption:", e)


def verify():
    try:
        with open(r'C:\Users\dipak\Desktop\Software now\raw_text.txt', 'r', encoding='utf-8') as f:
            original = f.read()

        with open(r'C:\Users\dipak\Desktop\Software now\decrypted_text.txt', 'r', encoding='utf-8') as f:
            decrypted = f.read()

        if original == decrypted:
            print("Verification: SUCCESS - files match!")
        else:
            print("Verification: FAILED - files do not match.")
            print("Original length:", len(original))
            print("Decrypted length:", len(decrypted))

    except FileNotFoundError:
        print("Files not found for verification.")
    except Exception as e:
        print("Error during verification:", e)


if __name__ == "__main__":
    print("Text Encryption Program")
    print("=======================")

    try:
        shift1 = int(input("Enter shift1: "))
        shift2 = int(input("Enter shift2: "))
    except ValueError:
        print("Please enter numbers only.")
        exit()

    print("Using shifts:", shift1, ",", shift2)

    encrypt_file(shift1, shift2)
    decrypt_file(shift1, shift2)
    verify()

    print("Done!")
