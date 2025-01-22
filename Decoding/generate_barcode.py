import barcode
from barcode.writer import ImageWriter

# Define the data for the barcode
data = "https://benax.rw" 

# Specify the barcode type (e.g., 'ean13', 'code128', 'upc', etc.)
barcode_type = "code128"

# Generate the barcode with an image writer
barcode_class = barcode.get_barcode_class(barcode_type)
barcode_instance = barcode_class(data, writer=ImageWriter())

# Save the barcode as an image
output_filename = "barcode"
barcode_instance.save(output_filename)

print(f"Barcode saved as {output_filename}.png")