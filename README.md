# Prodgy_Cs_02
Here’s a short description you can use with the code:
This is a simple Python program for image encryption and decryption using pixel manipulation. It uses a mathematical operation to modify the pixel values of an image based on a user-defined key. The same key is used to reverse the operation for decryption. This tool demonstrates a basic way to secure image files using simple encryption techniques.


How It Works:

1. Encryption:

Each pixel value in the image is increased by the encryption key modulo 256 (to ensure the value stays within the valid range for image pixels, i.e., 0-255).

2. Decryption:

The encrypted pixel values are reversed by subtracting the key and applying modulo 256.

3. Input and Output:

Users can specify the input image, encryption key, and where to save the output (encrypted or decrypted image).


Note: This method is a simple demonstration and not suitable for high-security applications. For more robust security, consider advanced encryption algorithms.
