import subprocess

# Define the data to encode
data = "https://benax.rw"

# Define the output file name
output_file = "iqr_code.png"

# Command to generate iQR Code using Zint
command = [
    "zint",  # Zint command-line tool
    "-v",  # verbose
    "--barcode=58",  # iQR Code type
    f"--data={data}",  # Data to encode
    f"--output={output_file}"  # Output file name
]

# Execute the command
try:
    subprocess.run(command, check=True)
    print(f"iQR Code generated and saved as '{output_file}'")
except FileNotFoundError:
    print("Error: Zint is not installed. Please install it to generate iQR Codes.")
except subprocess.CalledProcessError as e:
    print(f"Error while generating iQR Code: {e}")