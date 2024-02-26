alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher(text, shift_key, operation):
    """Caesar Cipher function for encryption and decryption"""
    result_text = ""
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            if operation == 'encrypt':
                new_position = (position + shift_key) % 26
            elif operation == 'decrypt':
                new_position = (position - shift_key) % 26
            result_text += alphabet[new_position]
        else:
            result_text += char
    return result_text

wanna_end = False
while not wanna_end:
    what_to_do = input("Type 'encrypt' for encryption, type 'decrypt' for decryption\n")
    text = input("Type your message\n").lower()
    shift = int(input("Enter shift key:\n"))
    
    result = caesar_cipher(text, shift, what_to_do)
    
    if what_to_do == "encrypt":
        print(f"Here's the text after encryption: {result}")
    elif what_to_do == "decrypt":
        print(f"Here's the text after decryption: {result}")
    
    play_again = input("Type 'yes' to continue, type 'no' to exit\n")
    if play_again == 'no':
        wanna_end = True
        print("Bye!")
