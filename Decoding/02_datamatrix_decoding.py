from pylibdmtx import decode
from PIL import Image

# Load the Data Matrix image
image = Image.open("datamatrix.png")

# Decode the Data Matrix
decoded = decode(image)
if decoded:
    print(f"Decoded Data: {decoded[0].data.decode('utf-8')}")
else:
    print("No Data Matrix code detected.")