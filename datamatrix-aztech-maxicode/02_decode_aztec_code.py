import imageio.v3 as imageio
import numpy as np
from PIL import Image
from pyztec.aztec import AztecBarcodeCompact

def process_and_decode(image_path, layers, channel=2):
    """
    Process the image and decode the Aztec barcode.
    Parameters:
        - image_path (str): Path to the image file containing the Aztec code.
        - layers (int): Number of layers for the Aztec code.
        - channel (int): Channel to use for decoding (default: 2).
    """
    dimension = layers * 4 + 11  # Calculate dimensions based on layers
    image = imageio.imread(image_path)

    # Handle GIF files (use the first frame)
    if image_path.endswith(".gif"):
        image = image[0]

    # Extract the specified channel or use grayscale
    if len(image.shape) > 2:
        image_alpha = image[:, :, channel]
    else:
        image_alpha = image

    # Resize and convert to binary
    pil_img = Image.fromarray(image_alpha).resize((dimension, dimension)).convert("1")
    nparr = np.array(pil_img)

    # Invert bits if not using alpha channel
    if channel != 3:
        nparr = ~nparr

    # Decode Aztec code
    aztec = AztecBarcodeCompact(nparr)
    decoded_data = aztec.decode()
    return "".join(decoded_data)

if __name__ == "__main__":
    # Define parameters here
    image_path = "aztec_code.png"  # Replace with your image file
    layers = 2  # Replace with the appropriate number of layers
    channel = 2  # Replace with the desired channel (default: 2)

    try:
        result = process_and_decode(image_path, layers, channel)
        print("Decoded Data:", result)
    except Exception as e:
        print("Decoding failed:", e)