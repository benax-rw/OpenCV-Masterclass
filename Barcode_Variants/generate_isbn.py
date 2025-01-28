import barcode
from barcode.writer import ImageWriter

# Step 1: Define the ISBN number
# ISBN-13 includes 12 digits; the 13th (checksum) is calculated automatically.
isbn_data = "978030640615"  # Replace with your desired ISBN-12

# Step 2: Create an EAN-13 barcode object for the ISBN
# Use ImageWriter to save the barcode as an image
isbn_barcode = barcode.get("ean13", isbn_data, writer=ImageWriter())

# Step 3: Save the barcode as a PNG file
output_file = "isbn_barcode"  # The file will be saved as isbn_barcode.png
isbn_barcode.save(output_file)

# Inform the user
print(f"ISBN barcode saved as '{output_file}.png'")