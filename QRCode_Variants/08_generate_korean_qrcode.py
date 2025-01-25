import qrcode

# Define Korean text
data = "안녕하세요, 세계"  # "Hello, World" in Korean

# Create a QR Code
qr = qrcode.QRCode(
    version=1,  # Adjust size (1: 21x21 modules)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
    box_size=10,
    border=4,
)

# Add Korean text (no need for manual encoding if using UTF-8)
qr.add_data(data)
qr.make(fit=True)

# Save the QR Code
img = qr.make_image(fill_color="black", back_color="white")
img.save("korean_qrcode.png")
print("QR Code with Korean text saved as 'korean_qrcode.png'")