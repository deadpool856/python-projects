def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    
    if mode == "decrypt":
        shift = -shift

    for char in text:
        # Check if the character is an uppercase letter
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Check if the character is a lowercase letter
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Non-alphabetical characters remain unchanged
            result += char

    return result


# Example usage
if __name__ == "__main__":
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value: "))
    mode = input("Enter mode (encrypt/decrypt): ").lower()
    
    result = caesar_cipher(text, shift, mode)
    print(f"Result: {result}")
