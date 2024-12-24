"""This is simple python code for image encruption/decryption

from PIL import Image
import numpy as np

def encrypt_image(image_path, key, output_path):
    """
    Encrypts an image by manipulating its pixel values using a key.

    Parameters:
    - image_path (str): Path to the input image file.
    - key (int): Key used to modify pixel values.
    - output_path (str): Path to save the encrypted image.
    """
    # Open the image and convert it to an array
    img = Image.open(image_path)
    img_array = np.array(img)

    # Encrypt: Modify pixel values using the key
    encrypted_array = (img_array + key) % 256

    # Convert array back to an image and save it
    encrypted_img = Image.fromarray(encrypted_array.astype(np.uint8))
    encrypted_img.save(output_path)
    print(f"Encrypted image saved to {output_path}")


def decrypt_image(image_path, key, output_path):
    """
    Decrypts an image by reversing the encryption process using the key.

    Parameters:
    - image_path (str): Path to the encrypted image file.
    - key (int): Key used to modify pixel values during encryption.
    - output_path (str): Path to save the decrypted image.
    """
    # Open the image and convert it to an array
    img = Image.open(image_path)
    img_array = np.array(img)

    # Decrypt: Reverse the pixel value manipulation
    decrypted_array = (img_array - key) % 256

    # Convert array back to an image and save it
    decrypted_img = Image.fromarray(decrypted_array.astype(np.uint8))
    decrypted_img.save(output_path)
    print(f"Decrypted image saved to {output_path}")


# Example Usage
if __name__ == "__main__":
    print("Image Encryption and Decryption Tool")
    action = input("Choose an action (encrypt/decrypt): ").strip().lower()
    image_path = input("Enter the path to the image: ").strip()
    key = int(input("Enter the encryption key (integer): ").strip())
    output_path = input("Enter the output file path: ").strip()

    if action == "encrypt":
        encrypt_image(image_path, key, output_path)
    elif action == "decrypt":
        decrypt_image(image_path, key, output_path)
    else:
        print("Invalid action! Please choose 'encrypt' or 'decrypt'.")



