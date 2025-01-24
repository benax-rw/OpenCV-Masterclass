import barcode
from barcode.writer import ImageWriter

# Step 1: Define the UPC data
# Provide the first 11 digits; the 12th digit (checksum) will be calculated automatically
upc_data = "12345678901"

# Step 2: Select the "upc" barcode type and generate the barcode
upc = barcode.get("upc", upc_data, writer=ImageWriter())

# Step 3: Save the barcode as an image
output_file = "upc_barcode"
upc.save(output_file)

print(f"UPC Barcode saved as {output_file}.png")