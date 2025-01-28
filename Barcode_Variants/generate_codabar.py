import barcode
from barcode.writer import ImageWriter

# Step 1: Define the data for Codabar
# Data must include a start and stop character (A, B, C, or D)
codabar_data = "A123456B"  # Replace with your desired data

# Step 2: Create a Codabar barcode object
# Use ImageWriter to save the barcode as an image
codabar = barcode.get("codabar", codabar_data, writer=ImageWriter())

# Step 3: Save the barcode as a PNG file
output_file = "codabar_barcode"  # The file will be saved as codabar_barcode.png
codabar.save(output_file)

# Inform the user
print(f"Codabar barcode saved as '{output_file}.png'")