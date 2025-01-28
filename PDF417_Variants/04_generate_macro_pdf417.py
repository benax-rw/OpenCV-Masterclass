import pdf417gen
from pdf417gen import encode, render_image

# Define parts of the message
parts = [
    "This is the first part of the message.",
    "This is the second part of the message.",
    "This is the third part of the message."
]

# Unique identifier for the Macro PDF417 barcodes
macro_id = "12345"

# Generate Macro PDF417 barcodes
barcodes = []
for index, part in enumerate(parts):
    # Add Macro PDF417 metadata to the message
    macro_data = f"ID:{macro_id}\nIndex:{index + 1}\nTotal:{len(parts)}\n{part}"
    # Encode the message with PDF417
    codes = encode(macro_data, columns=5)
    barcodes.append(codes)

# Render and save each barcode
for index, codes in enumerate(barcodes):
    image = render_image(codes, scale=2)
    image.save(f"macro_pdf417_part_{index + 1}.png")

print("Macro PDF417 barcodes have been generated and saved.")