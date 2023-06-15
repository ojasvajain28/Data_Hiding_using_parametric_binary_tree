# from PIL import Image

# # Step 1: Encryption
# def encrypt_image(image_path, key):
#     image = Image.open('D:\projects\Image hiding using parametric binary tree\download.jfif')
#     # Apply encryption algorithm of your choice
#     # Here's a simple example using XOR encryption
#     encrypted_pixels = []
#     for pixel in image.getdata():
#         encrypted_pixel = tuple((p ^ key) for p in pixel)
#         encrypted_pixels.append(encrypted_pixel)
#     encrypted_image = Image.new(image.mode, image.size)
#     encrypted_image.putdata(encrypted_pixels)
#     return encrypted_image

# # Step 2: Data hiding in encrypted image
# def hide_data_in_image(encrypted_image, message):
#     # Convert the message to binary
#     binary_message = ''.join(format(ord(char), '08b') for char in message)
#     image_pixels = list(encrypted_image.getdata())
#     if len(binary_message) > len(image_pixels):
#         raise ValueError("Message too large to hide in the image.")
#     stego_pixels = []
#     for i in range(len(binary_message)):
#         pixel = image_pixels[i]
#         bit = int(binary_message[i])
#         stego_pixel = tuple((p ^ (bit * 255)) for p in pixel)
#         stego_pixels.append(stego_pixel)
#     stego_image = Image.new(encrypted_image.mode, encrypted_image.size)
#     stego_image.putdata(stego_pixels)
#     return stego_image

# # Step 3: Data extraction from encrypted image
# def extract_data_from_image(stego_image):
#     stego_pixels = list(stego_image.getdata())
#     binary_message = ""
#     for pixel in stego_pixels:
#         bit = pixel[0] & 1  # Extract the least significant bit
#         binary_message += str(bit)
#     message = ""
#     for i in range(0, len(binary_message), 8):
#         byte = binary_message[i:i+8]
#         char = chr(int(byte, 2))
#         message += char
#     return message

# # Example usage
# # Encryption
# encrypted_image = encrypt_image("cover_image.png", 123)

# # Data hiding
# message = "This is a secret message."
# stego_image = hide_data_in_image(encrypted_image, message)

# # Save the stego image
# stego_image.save("stego_image.png")

# # Data extraction
# extracted_message = extract_data_from_image(stego_image)
# print("Extracted message:", extracted_message)

# # Step 4: Decryption
# def decrypt_image(encrypted_image, key):
#     decrypted_pixels = []
#     for pixel in encrypted_image.getdata():
#         decrypted_pixel = tuple((p ^ key) for p in pixel)
#         decrypted_pixels.append(decrypted_pixel)
#     decrypted_image = Image.new(encrypted_image.mode, encrypted_image.size)
#     decrypted_image.putdata(decrypted_pixels)
#     return decrypted_image

# # Step 5: Data extraction from decrypted image
# def extract_data_from_decrypted_image(decrypted_image):
#     decrypted_pixels = list(decrypted_image.getdata())
#     binary_message = ""
#     for pixel in decrypted_pixels:
#         bit = pixel[0] & 1  # Extract the least significant bit
#         binary_message += str(bit)
#     message = ""
#     for i in range(0, len(binary_message), 8):
#         byte = binary_message[i:i+8]
#         char = chr(int(byte, 2))
#         message += char
#     return message

# # Example usage
# # Decryption
# decrypted_image = decrypt_image(stego_image, 123)

# # Data extraction from decrypted image
# extracted_message = extract_data_from_decrypted_image(decrypted_image)
# print("Extracted message from decrypted image:", extracted_message)
from PIL import Image
from data_hiding import encrypt_image, hide_data_in_image, extract_data_from_image, decrypt_image, extract_data_from_decrypted_image

# Encryption
encrypted_image = encrypt_image('D:\projects\Image hiding using parametric binary tree\download.jfif', 123)

# Data hiding
message = "This is a secret message."
stego_image = hide_data_in_image(encrypted_image, message)

# Save the stego image
stego_image.save("stego_image.png")

# Data extraction
extracted_message = extract_data_from_image(stego_image)
print("Extracted message:", extracted_message)

# Decryption
decrypted_image = decrypt_image(stego_image, 123)

# Data extraction from decrypted image
extracted_message = extract_data_from_decrypted_image(decrypted_image)
print("Extracted message from decrypted image:", extracted_message)
