import barcode
from barcode.writer import ImageWriter

# Step 1: Define the data for Code 39
# Code 39 supports uppercase letters, numbers, and specific special characters
code39_data = "CODE39-1234"  # Replace with your own data

# Step 2: Create a Code 39 barcode object
# Use ImageWriter to save the barcode as an image
code39 = barcode.get("code39", code39_data, writer=ImageWriter())

# Step 3: Save the barcode as a PNG file
output_file = "code39_barcode"  # The file will be saved as code39_barcode.png
code39.save(output_file)

# Inform the user
print(f"Code 39 barcode saved as '{output_file}.png'")