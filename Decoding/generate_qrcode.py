import qrcode

# Data to encode in the QR code
data = "https://benax.rw"

# Create a QR code object
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code (1 is 21x21, up to 40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in the QR Code grid
    border=4,  # Thickness of the border (minimum is 4)
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image of the QR code
qr_image = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image
qr_image.save("qrcode.png")
print("QR code saved as 'qrcode.png'")