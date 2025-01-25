import subprocess

# Step 1: Define the Morse-to-Model1 mapping
morse_to_model1 = {
    ".": "D",
    "-": "A",
    " ": "F"
}

# Step 2: Define the Morse code
morse_code = ".... . .-.. .-.. ---"  # Morse code for "HELLO"

# Step 3: Convert Morse code to Model 1-compatible characters
model1_data = "".join(morse_to_model1[char] for char in morse_code)

# Step 4: Define the output file name
output_file = "model1_morse_qrcode.png"

# Step 5: Command to generate Model 1 QR Code using Zint
command = [
    "zint",  # Zint command-line tool
    "--barcode=93",  # Model 1 QR Code type
    f"--data={model1_data}",  # Transformed Morse code
    f"--output={output_file}"  # Output file name
]

# Step 6: Execute the command
try:
    subprocess.run(command, check=True)
    print(f"Model 1 QR Code with Morse Code generated and saved as '{output_file}'")
except FileNotFoundError:
    print("Error: Zint is not installed. Please install it to generate QR Codes.")
except subprocess.CalledProcessError as e:
    print(f"Error while generating Model 1 QR Code: {e}")