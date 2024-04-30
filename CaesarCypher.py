import sys

def caesar_cipher(text, shift):
    encrypted_text = []
    
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            # Shift the character within 'A' to 'Z' range
            shifted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            encrypted_text.append(shifted_char)
    
    return ''.join(encrypted_text)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 mycipher.py <shift_amount>")
        sys.exit(1)
    
    try:
        shift = int(sys.argv[1]) % 26  # Ensure shift is between 0 and 25
    except ValueError:
        print("Shift amount must be an integer.")
        sys.exit(1)
    
    input_text = sys.stdin.read().strip().upper()  # Read input and convert to uppercase
    
    encrypted_message = caesar_cipher(input_text, shift)
    
    # Print the encrypted message in blocks of five letters, ten blocks per line
    block_size = 5
    for i in range(0, len(encrypted_message), block_size):
        print(encrypted_message[i:i+block_size], end=' ')
        if (i+1) % (block_size * 10) == 0:
            print()  # Start a new line after 10 blocks

