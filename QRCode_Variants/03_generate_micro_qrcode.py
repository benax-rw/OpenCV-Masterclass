import subprocess

# Define the data to encode in the Micro QR Code
data = "benax.rw"

# Define the output file name
output_file = "micro_qrcode.png"

# Command to generate Micro QR Code using Zint
command = [
    "zint",  # Zint command-line tool
    "--barcode=97",  # Micro QR Code type (97 is the identifier for Micro QR Code in Zint)
    f"--data={data}",  # Data to encode
    f"--output={output_file}"  # Output file name
]

# Execute the command
try:
    subprocess.run(command, check=True)
    print(f"Micro QR Code generated and saved as '{output_file}'")
except FileNotFoundError:
    print("Error: Zint is not installed. Please install it to generate Micro QR Codes.")
except subprocess.CalledProcessError as e:
    print(f"Error while generating Micro QR Code: {e}")