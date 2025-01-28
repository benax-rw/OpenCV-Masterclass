import subprocess

# Define the data to encode
data = "Truncated PDF417 Example"

# Define the output file
output_file = "truncated_pdf417.png"

# Command to generate Truncated PDF417 using Zint
command = [
    "zint",  # Zint command-line tool
    "--barcode=56",  # Code for Truncated PDF417
    f"--data={data}",  # Data to encode
    f"--output={output_file}",  # Output file name
    "--notext",  # Option to hide text below the barcode
]

# Execute the command
try:
    subprocess.run(command, check=True)
    print(f"Truncated PDF417 generated and saved as '{output_file}'")
except FileNotFoundError:
    print("Error: Zint is not installed. Please install it to generate Truncated PDF417.")
except subprocess.CalledProcessError as e:
    print(f"Error while generating Truncated PDF417: {e}")