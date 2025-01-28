from cryptography.fernet import Fernet
from pyzxing import BarCodeReader

# Step 1: Load the encryption key
try:
    with open("encryption_key.key", "rb") as key_file:
        key = key_file.read()
        cipher = Fernet(key)
    print("Encryption key loaded successfully.")
except FileNotFoundError:
    print("Error: Encryption key file not found. Make sure 'encryption_key.key' exists.")
    exit()

# Step 2: Decode the Secure PDF417 barcode
try:
    reader = BarCodeReader()
    result = reader.decode("secure_pdf417.png")
    
    if not result:
        print("No barcodes detected. Ensure the image contains a valid Secure PDF417 barcode.")
        exit()
    
    # Extract the encrypted message
    encrypted_data = result[0]['parsed']
    print("Encrypted data retrieved from barcode:", encrypted_data.decode('utf-8'))
except Exception as e:
    print("Error during barcode decoding:", e)
    exit()

# Step 3: Decrypt the encrypted message
try:
    decrypted_message = cipher.decrypt(encrypted_data).decode('utf-8')
    print("Decrypted Message:", decrypted_message)

    # Save the decrypted message to a text file (optional)
    with open("decrypted_message.txt", "w") as file:
        file.write(decrypted_message)
    print("Decrypted message saved to 'decrypted_message.txt'.")
except Exception as e:
    print("Error during decryption:", e)