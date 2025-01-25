import qrcode
from cryptography.fernet import Fernet
from PIL import Image

# Step 1: Generate a key for encryption
key = Fernet.generate_key()
cipher = Fernet(key)

# Step 2: Define the data to be encoded
data = "https://benax.rw"

# Step 3: Encrypt the data
encrypted_data = cipher.encrypt(data.encode())

# Step 4: Create a QR Code
qr = qrcode.QRCode(
    version=3,  # Larger version to accommodate the logo
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction to embed the logo
    box_size=10,
    border=4,
)
qr.add_data(encrypted_data)
qr.make(fit=True)

# Step 5: Generate the QR code image
qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

# Step 6: Add a logo to the QR code
logo_path = "we-chat-logo.png"  # Replace with the path to your logo
try:
    logo = Image.open(logo_path)
    # Resize logo to fit within the QR code
    logo_size = int(qr_img.size[0] * 0.3)  # Logo size: 30% of the QR code
    logo = logo.resize((logo_size, logo_size), Image.LANCZOS)  # Use LANCZOS for high-quality resizing

    # Calculate logo position to center it
    qr_width, qr_height = qr_img.size
    logo_position = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

    # Paste the logo onto the QR code
    qr_img.paste(logo, logo_position, mask=logo)
    print("Logo added to the QR code.")
except FileNotFoundError:
    print("Logo file not found. Generating QR code without a logo.")

# Step 7: Save the QR code with the logo
output_file = "branded_encrypted_qrcode.png"
qr_img.save(output_file)
print(f"Branded encrypted QR code saved as '{output_file}'")

# Step 8: Save the encryption key to a file
key_file = "proprietary_encryption_key.txt"
with open(key_file, "wb") as file:
    file.write(key)
print(f"Encryption key saved as '{key_file}'")

# Optional: Display the QR code
qr_img.show()