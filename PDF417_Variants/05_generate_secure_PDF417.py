from cryptography.fernet import Fernet
import pdf417gen
from pdf417gen import encode, render_image

# Step 1: Generate an encryption key
# Run this section only once and save the key securely
key = Fernet.generate_key()
cipher = Fernet(key)

# Save the key to a file for later decryption (optional)
with open("encryption_key.key", "wb") as key_file:
    key_file.write(key)
print("Encryption key generated and saved as 'encryption_key.key'.")

# Step 2: Define the message to be secured
original_message = "This is a secure PDF417 message."

# Step 3: Encrypt the message
encrypted_message = cipher.encrypt(original_message.encode('utf-8'))
print("Encrypted message:", encrypted_message)

# Step 4: Encode the encrypted message into a PDF417 barcode
# Ensure the encrypted message is converted to a string
codes = encode(encrypted_message.decode('utf-8'), columns=8)

# Step 5: Render the PDF417 barcode as an image and save it
image = render_image(codes, scale=3)
image.save("secure_pdf417.png")
print("Secure PDF417 barcode generated and saved as 'secure_pdf417.png'.")