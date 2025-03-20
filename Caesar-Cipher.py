def encrypt_decrypt(text, mode, key):  
    letters = 'abcdefghijklmnopqrstuvwxyz'  
    result = ''  
    num_letters = len(letters)  

    if mode == 'd':  
        key = -key
        'Reverse the key for decryption' 

    for letter in text.lower():  
        if letter not in letters:  
            result += letter  
            continue  

        index = letters.find(letter)  
        new_index = index + key  

        'Wrap around if the new index is out of bounds'  
        if new_index >= num_letters:  
            new_index -= num_letters  
        elif new_index < 0:  
            new_index += num_letters  

        result += letters[new_index]  

    return result  

'Main program'  
print("~~~Caesar Cipher Program~~~")  
user_input = input("Do you want to encrypt or decrypt? (e/d): ").lower()  
key = int(input("Enter the key (1 through 25): "))  
text = input("Enter the text: ")  

if user_input == 'e':  
    print("Encryption mode selected")  
    ciphertext = encrypt_decrypt(text, 'e', key)  
    print(f"Ciphertext: {ciphertext}")  
elif user_input == 'd':  
    print("Decryption mode selected")  
    plaintext = encrypt_decrypt(text, 'd', key)  
    print(f"Plaintext: {plaintext}")  
else:  
    print("Invalid input. Please enter 'e' for encrypt or 'd' for decrypt.")
