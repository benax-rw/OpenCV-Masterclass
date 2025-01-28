import pdf417gen
from pdf417gen import encode, render_image

# Define parts of the message
parts = [
    "This is the first part of the message.",
    "This is the second part of the message.",
    "This is the third part of the message."
]

# Combine all parts into a single message
combined_message = "\n".join(f"Part {i+1}: {part}" for i, part in enumerate(parts))

# Encode the combined message into a single PDF417 barcode
codes = encode(combined_message, columns=10)  # Adjust columns for size

# Render the barcode as an image
image = render_image(codes, scale=3)  # Scale controls image resolution
image.save("macro_pdf417_combined.png")

print("Single Macro PDF417 barcode generated and saved as 'macro_pdf417_combined.png'.")