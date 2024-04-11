def caesar_cipher(text, shift, mode):
    encrypted_text = ''
    for char in text:
        if char.isalpha():  # Check if the character is an alphabet
            if char.islower():
                encrypted_text += chr((ord(char) - 97 + shift if mode == 'encrypt' else ord(char) - 97 - shift) % 26 + 97)
            else:
                encrypted_text += chr((ord(char) - 65 + shift if mode == 'encrypt' else ord(char) - 65 - shift) % 26 + 65)
        else:
            encrypted_text += char
    return encrypted_text

def main():
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (a number between 1 and 25): "))
    mode = input("Enter 'encrypt' or 'decrypt': ").lower()

    if mode == 'encrypt' or mode == 'decrypt':
        encrypted_message = caesar_cipher(message, shift, mode)
        print(f"Your {'encrypted' if mode == 'encrypt' else 'decrypted'} message is: {encrypted_message}")
    else:
        print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
