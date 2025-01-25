import qrcode
from cryptography.fernet import Fernet

# Step 1: Generate an encryption key
key = Fernet.generate_key()
cipher = Fernet(key)

# Step 2: Define data to encode and encrypt it
data = "Confidential Information: Access Restricted"
encrypted_data = cipher.encrypt(data.encode())

# Step 3: Generate the QR Code with the encrypted data
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
    box_size=10,
    border=4,
)
qr.add_data(encrypted_data)
qr.make(fit=True)

# Step 4: Save the QR Code as an image
qr_img = qr.make_image(fill_color="black", back_color="white")
qr_img.save("secure_qrcode.png")
print("Secure QR Code (SQRC) saved as 'secure_qrcode.png'")

# Step 5: Save the encryption key for decryption
with open("encryption_key.key", "wb") as key_file:
    key_file.write(key)
print("Encryption key saved as 'encryption_key.key'")