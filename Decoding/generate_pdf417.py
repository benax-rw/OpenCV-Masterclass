import pdf417gen as pdf417

# Data to encode
data = "This is a PDF417 barcode example. It supports encoding large amounts of data."

# Generate the PDF417 code
codes = pdf417.encode(data, columns=5)

# Render the codes to an image
pdf417_image = pdf417.render_image(codes, scale=3)

# Save the image
pdf417_image.save("pdf417_code.png")
print("PDF417 code saved as pdf417_code.png")

# Optional: Display the image
pdf417_image.show()