from pyzxing import BarCodeReader

# Path to the barcode image
image_path = "macro_pdf417_combined.png"

# Decode the barcode
reader = BarCodeReader()
result = reader.decode(image_path)

# Check if the barcode was decoded
if result:
    # Extract the parsed message
    decoded_message = result[0]['parsed'].decode('utf-8')

    # Save the message to a text file
    with open("decoded_message.txt", "w") as file:
        file.write(decoded_message)

    print("Decoded message saved to 'decoded_message.txt'.")
else:
    print("No barcodes detected or decoding failed.")