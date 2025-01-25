import qrcode

# Define Kanji/Kana data
data = "こんにちは、世界"  # "Hello, World" in Japanese

# Explicitly encode the data in Shift JIS
encoded_data = data.encode("shift_jis")

# Create a QR Code
qr = qrcode.QRCode(
    version=1,  # Controls size (1: 21x21 modules)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Low error correction
    box_size=10,  # Size of each box in pixels
    border=4,  # Minimum border size
)

# Add binary-encoded data
qr.add_data(encoded_data)
qr.make(fit=True)

# Save the QR Code
img = qr.make_image(fill_color="black", back_color="white")
img.save("kanji_kana_qrcode.png")
print("QR Code with Kanji/Kana saved as 'kanji_kana_qrcode.png'")