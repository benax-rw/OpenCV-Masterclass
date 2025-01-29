from pylibdmtx import pylibdmtx
from PIL import Image

# Data to encode
data = "Hello, ECC 200 Data Matrix!"

# Generate ECC 200 Data Matrix
encoded = pylibdmtx.encode(data.encode('utf-8'))

# Create image from encoded data
img = Image.frombytes('RGB', (encoded.width, encoded.height), encoded.pixels)
img.save('ecc200_datamatrix.png')

print("ECC 200 Data Matrix saved as 'ecc200_datamatrix.png'")