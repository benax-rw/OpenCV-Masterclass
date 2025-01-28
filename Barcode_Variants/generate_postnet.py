import subprocess

# Step 1: Define the POSTNET data
postnet_data = "123456789"  # Replace with your desired data (5, 9, or 11 digits)
output_file = "postnet_barcode.png"

# Step 2: Call Zint to generate the barcode
command = [
    "zint",
    "--barcode=24",  # POSTNET barcode type
    f"--data={postnet_data}",
    f"--output={output_file}",
]

result = subprocess.run(command, capture_output=True, text=True)

# Step 3: Check the result
if result.returncode == 0:
    print(f"POSTNET barcode saved as '{output_file}'")
else:
    print(f"Error: {result.stderr}")