from PIL import Image
import numpy as np

def encrypt_decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    img_array = np.array(img)
    encrypted_array = img_array ^ key  # XOR operation on each pixel

    encrypted_img = Image.fromarray(encrypted_array)
    encrypted_img.save(output_path)

    print(f"Image saved at {output_path}")

#User Input
mode = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()
input_path = input("Enter input image file path: ")
output_path = input("Enter output image file path: ")
key = int(input("Enter a numeric key (0-255): "))  # XOR key must be 0-255

#Encryption or decryption
if mode in ["encrypt", "decrypt"]:
    encrypt_decrypt_image(input_path, output_path, key)
else:
    print("Invalid mode! Choose 'encrypt' or 'decrypt'.")