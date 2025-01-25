from cryptography.fernet import Fernet
from PIL import Image
from pyzbar.pyzbar import decode

# Step 1: Load the encryption key
with open("encryption_key.key", "rb") as key_file:
    key = key_file.read()
cipher = Fernet(key)

# Step 2: Decode the QR Code
qr_img = Image.open("secure_qrcode.png")
decoded_data = decode(qr_img)[0].data

# Step 3: Decrypt the data
decrypted_data = cipher.decrypt(decoded_data).decode()
print(f"Decrypted data: {decrypted_data}")