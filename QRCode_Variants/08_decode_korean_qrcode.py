from pyzbar.pyzbar import decode
from PIL import Image

# Load the QR Code image
qr_image = Image.open("korean_qrcode.png")
output_file = "decoded_korean.txt"

# Decode the QR Code
decoded_data = decode(qr_image)
for obj in decoded_data:
    raw_data = obj.data
    print(f"Raw Data: {raw_data}")  # Print raw byte data
    try:
        # Decode as UTF-8 (Korean characters are supported)
        decoded_text = raw_data.decode("utf-8")
        print(f"Decoded Data (UTF-8): {decoded_text}")
        
        # Save the decoded output to a file
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(decoded_text)
        print(f"Decoded content saved to '{output_file}'")
    except UnicodeDecodeError as e:
        print(f"UTF-8 Decode Error: {e}")