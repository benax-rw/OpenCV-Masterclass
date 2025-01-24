import barcode
from barcode.writer import ImageWriter

# Step 1: Define the data for Code 128
# Code 128 supports letters, numbers, and symbols
code128_data = "CODE128-2023!"  # Replace with your desired data

# Step 2: Create a Code 128 barcode object
# Use ImageWriter to save the barcode as an image
code128 = barcode.get("code128", code128_data, writer=ImageWriter())

# Step 3: Save the barcode as a PNG file
output_file = "code128_barcode"  # The file will be saved as code128_barcode.png
code128.save(output_file)

# Inform the user
print(f"Code 128 barcode saved as '{output_file}.png'")