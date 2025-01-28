import barcode
from barcode.writer import ImageWriter

# Step 1: Define the POSTNET data
postnet_data = "123456789"  # Replace with ZIP+4 or delivery point data

# Step 2: Create a POSTNET barcode object
postnet = barcode.get("postnet", postnet_data, writer=ImageWriter())

# Step 3: Save the barcode as a PNG file
output_file = "postnet_barcode"
postnet.save(output_file)

print(f"POSTNET barcode saved as '{output_file}.png'")