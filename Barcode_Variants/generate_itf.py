import barcode
from barcode.writer import ImageWriter

# Step 1: Define the data for ITF
# ITF encodes numeric data in pairs; ensure an even number of digits
itf_data = "12345678"  # Replace with your own numeric data (must be even digits)

# Step 2: Create an ITF barcode object
# Use ImageWriter to save the barcode as an image
itf = barcode.get("itf", itf_data, writer=ImageWriter())

# Step 3: Save the barcode as a PNG file
output_file = "itf_barcode"  # The file will be saved as itf_barcode.png
itf.save(output_file)

# Inform the user
print(f"Interleaved 2 of 5 barcode saved as '{output_file}.png'")