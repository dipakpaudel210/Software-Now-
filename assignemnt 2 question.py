# Text Encryption and Decryption Program

def encrypt_text(text, shift1, shift2):
    result = ""
    
    for char in text:
        # Handle lowercase letters (a-z)
        if char >= 'a' and char <= 'z':
            pos = ord(char) - ord('a')
            
            if pos <= 12:  # first half (a-m)
                new_pos = (pos + shift1 * shift2) % 26
                # Add marker to remember this was first half
                result += chr(new_pos + ord('a')) + '\x00'  # null character as marker
            else:  # second half (n-z)
                new_pos = (pos - (shift1 + shift2)) % 26
                # Add different marker for second half
                result += chr(new_pos + ord('a')) + '\x01'
            
        # Handle uppercase letters (A-Z)
        elif char >= 'A' and char <= 'Z':
            pos = ord(char) - ord('A')
            
            if pos <= 12:  # first half (A-M)
                new_pos = (pos - shift1) % 26
                result += chr(new_pos + ord('A')) + '\x00'
            else:  # second half (N-Z)
                new_pos = (pos + shift2 * shift2) % 26
                result += chr(new_pos + ord('A')) + '\x01'
            
        # Keep other characters as they are
        else:
            result += char
    
    return result

def decrypt_text(encrypted_text, shift1, shift2):
    result = ""
    i = 0
    
    while i < len(encrypted_text):
        char = encrypted_text[i]
        
        # Handle lowercase letters (a-z)
        if char >= 'a' and char <= 'z':
            # Check the marker to know which rule was used
            if i + 1 < len(encrypted_text) and encrypted_text[i + 1] == '\x00':
                # Was first half originally, reverse the first half rule
                pos = ord(char) - ord('a')
                original_pos = (pos - shift1 * shift2) % 26
                result += chr(original_pos + ord('a'))
                i += 2  # Skip the marker
            elif i + 1 < len(encrypted_text) and encrypted_text[i + 1] == '\x01':
                # Was second half originally, reverse the second half rule
                pos = ord(char) - ord('a')
                original_pos = (pos + (shift1 + shift2)) % 26
                result += chr(original_pos + ord('a'))
                i += 2  # Skip the marker
            else:
                result += char
                i += 1
                
        # Handle uppercase letters (A-Z)
        elif char >= 'A' and char <= 'Z':
            if i + 1 < len(encrypted_text) and encrypted_text[i + 1] == '\x00':
                # Was first half originally
                pos = ord(char) - ord('A')
                original_pos = (pos + shift1) % 26
                result += chr(original_pos + ord('A'))
                i += 2
            elif i + 1 < len(encrypted_text) and encrypted_text[i + 1] == '\x01':
                # Was second half originally
                pos = ord(char) - ord('A')
                original_pos = (pos - shift2 * shift2) % 26
                result += chr(original_pos + ord('A'))
                i += 2
            else:
                result += char
                i += 1
                
        # Keep other characters as they are
        else:
            result += char
            i += 1
    
    return result

def encryption_function(shift1, shift2):
    try:
        with open(r'C:\Users\dipak\Desktop\Software now\raw_text.txt', 'r') as file:
            content = file.read()
        
        encrypted_content = encrypt_text(content, shift1, shift2)
        
        with open(r'C:\Users\dipak\Desktop\Software now\encrypted_text.txt', 'w', encoding='utf-8') as file:
            file.write(encrypted_content)
        
        print("Encryption completed!")
        
    except FileNotFoundError:
        print("Error: raw_text.txt not found!")
    except Exception as e:
        print(f"Encryption error: {e}")

def decryption_function(shift1, shift2):
    try:
        with open(r'C:\Users\dipak\Desktop\Software now\encrypted_text.txt', 'r', encoding='utf-8') as file:
            encrypted_content = file.read()
        
        decrypted_content = decrypt_text(encrypted_content, shift1, shift2)
        
        with open(r'C:\Users\dipak\Desktop\Software now\decrypted_text.txt', 'w', encoding='utf-8') as file:
            file.write(decrypted_content)
        
        print("Decryption completed!")
        
    except FileNotFoundError:
        print("Error: encrypted_text.txt not found!")
    except Exception as e:
        print(f"Decryption error: {e}")

def verification_function():
    try:
        with open(r'C:\Users\dipak\Desktop\Software now\raw_text.txt', 'r', encoding='utf-8') as file:
            original_content = file.read()
        
        with open(r'C:\Users\dipak\Desktop\Software now\decrypted_text.txt', 'r', encoding='utf-8') as file:
            decrypted_content = file.read()
        
        if original_content == decrypted_content:
            print("Verification: SUCCESS - files match!")
        else:
            print("Verification: FAILED - files don't match!")
            print(f"Original: {len(original_content)} characters")
            print(f"Decrypted: {len(decrypted_content)} characters")
            
    except FileNotFoundError:
        print("Error: files not found for verification!")
    except Exception as e:
        print(f"Verification error: {e}")

# Main program
if __name__ == "__main__":
    print("Text Encryption Program")
    print("=" * 25)
    
    try:
        shift1 = int(input("Enter shift1: "))
        shift2 = int(input("Enter shift2: "))
    except ValueError:
        print("Please enter valid numbers!")
        exit()
    
    print(f"Using shifts: {shift1}, {shift2}")
    
    encryption_function(shift1, shift2)
    decryption_function(shift1, shift2)
    verification_function()
    
    print("Done!")