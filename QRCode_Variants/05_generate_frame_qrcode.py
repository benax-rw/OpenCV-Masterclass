from PIL import Image
import qrcode

# Step 1: Define the data for the QR code
data = "https://benax.rw"

# Step 2: Create a standard QR code
qr = qrcode.QRCode(
    version=4,  # Adjust size (4 allows more data, but keep it reasonable for frame design)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction for custom design
    box_size=10,  # Size of each QR code box in pixels
    border=4,  # Minimum border (quiet zone)
)
qr.add_data(data)
qr.make(fit=True)

# Step 3: Generate the QR code image
qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

# Step 4: Open the logo image
logo = Image.open("benax-logo-white-bg.png") #depends on the name of your file
logo_size = (120, 120)  # Resize logo to fit within the QR code
logo = logo.resize(logo_size)

# Step 5: Calculate the position for the logo
qr_width, qr_height = qr_img.size
logo_position = (
    (qr_width - logo_size[0]) // 2,
    (qr_height - logo_size[1]) // 2,
)

# Step 6: Overlay the logo onto the QR code
qr_img.paste(logo, logo_position, mask=logo)

# Step 7: Save the Frame QR Code
qr_img.save("frame_qrcode.png")
print("Frame QR Code saved as 'frame_qrcode.png'")