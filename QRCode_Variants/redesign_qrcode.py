from PIL import Image, ImageDraw

# Load the generated QR code
qr_code = Image.open("frame_qrcode.png").convert("RGBA")

# Add a frame or call-to-action if needed
frame = Image.new("RGBA", (qr_code.size[0] + 40, qr_code.size[1] + 80), "green")
frame.paste(qr_code, (20, 20))

# Add text
draw = ImageDraw.Draw(frame)
draw.text((frame.size[0] // 2 - 30, qr_code.size[1] + 40), "SCAN ME", fill="white")

# Save and display
frame.save("custom_qrcode.png")
frame.show()