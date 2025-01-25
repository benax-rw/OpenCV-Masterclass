import qrcode

# Define the data for the QR code
data = "https://benax.rw"

# Create a standard QR code
qr = qrcode.QRCode(
    version=1,  # Controls the size (1: 21x21, 40: 177x177)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
    box_size=10,  # Size of each box in pixels
    border=4,  # Border size (minimum is 4)
)

qr.add_data(data)
qr.make(fit=True)

# Save the QR code
qr_img = qr.make_image(fill_color="black", back_color="white")
qr_img.save("standard_qrcode.png")
print("QR Code saved as standard_qrcode.png")