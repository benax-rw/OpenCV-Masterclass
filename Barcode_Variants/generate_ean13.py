import barcode
from barcode.writer import ImageWriter

# Step 1: Define the EAN-13 data
# Provide 12 digits; the 13th (checksum) will be calculated automatically.
ean13_data = "400638133393"  # Replace with your own 12-digit data

# Step 2: Create an EAN-13 barcode object
# Use ImageWriter to save the barcode as an image
ean13 = barcode.get("ean13", ean13_data, writer=ImageWriter())

# Step 3: Save the barcode as a PNG file
output_file = "ean13_barcode"  # The file will be saved as ean13_barcode.png
ean13.save(output_file)

# Inform the user
print(f"EAN-13 barcode saved as '{output_file}.png'")