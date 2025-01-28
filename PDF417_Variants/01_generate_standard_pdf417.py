import pdf417gen
from PIL import Image

# Define the data to encode
data = "This is a Standard PDF417 code example. PDF417 is a high-capacity 2D barcode."

# Generate the PDF417 code
codes = pdf417gen.encode(data, columns=5)  # Adjust 'columns' to control the width of the barcode

# Render the PDF417 code as an image
pdf417_img = pdf417gen.render_image(codes, scale=3)  # Scale controls the resolution
pdf417_img.save("standard_pdf417.png")

print("Standard PDF417 code generated and saved as 'standard_pdf417.png'")