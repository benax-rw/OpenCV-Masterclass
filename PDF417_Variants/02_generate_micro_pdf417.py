import subprocess

# Define valid data (20 characters, digits only)
data = "12345678901234567890"  # Valid example data (exactly 20 digits)

# Define the output file
output_file = "compact_pdf417.png"

# Command to generate MicroPDF417 using Zint
command = [
    "zint",  # Zint command-line tool
    "--barcode=85",  # Code for MicroPDF417
    f"--data={data}",  # Valid 20-character data to encode
    f"--output={output_file}"  # Output file name
]

# Execute the command
try:
    subprocess.run(command, check=True)
    print(f"Compact PDF417 (MicroPDF417) generated and saved as '{output_file}'")
except FileNotFoundError:
    print("Error: Zint is not installed. Please install it to generate MicroPDF417.")
except subprocess.CalledProcessError as e:
    print(f"Error while generating Compact PDF417: {e}")