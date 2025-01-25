from pyzbar.pyzbar import decode
from PIL import Image
from cryptography.fernet import Fernet

# Load the encrypted QR code
qr_image = Image.open("branded_encrypted_qrcode.png")

# Decode the QR code
decoded_data = decode(qr_image)
if decoded_data:
    encrypted_content = decoded_data[0].data

    # Load the encryption key
    with open("proprietary_encryption_key.txt", "rb") as key_file:
        key = key_file.read()
    cipher = Fernet(key)

    # Decrypt the content
    decrypted_content = cipher.decrypt(encrypted_content).decode("utf-8")
    print("Decoded and Decrypted Data:", decrypted_content)
else:
    print("No QR code detected or unreadable.")