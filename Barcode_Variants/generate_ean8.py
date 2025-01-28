import barcode
from barcode.writer import ImageWriter

# Step 1: Define the EAN-8 data
# Provide 7 digits; the 8th digit (checksum) will be calculated automatically.
ean8_data = "9638507"  # Replace with your own 7-digit data

# Step 2: Create an EAN-8 barcode object
# Use ImageWriter to save the barcode as an image
ean8 = barcode.get("ean8", ean8_data, writer=ImageWriter())

# Step 3: Save the barcode as a PNG file
output_file = "ean8_barcode"  # The file will be saved as ean8_barcode.png
ean8.save(output_file)

# Inform the user
print(f"EAN-8 barcode saved as '{output_file}.png'")