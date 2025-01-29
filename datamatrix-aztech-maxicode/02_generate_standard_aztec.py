import subprocess

def generate_aztec_code(data, output_file="aztec_code.png", scale=10):
    """
    Generates an Aztec code using the `zint` command-line tool.
    Parameters:
        - data (str): The data to encode in the Aztec code.
        - output_file (str): The file path to save the Aztec code image.
        - scale (int): Scale factor for the generated Aztec code image.
    """
    try:
        # Construct the zint command
        command = [
            "zint",
            "--barcode=92",  # 92 is the identifier for Aztec codes in zint
            f"--data={data}",
            f"--output={output_file}",
            f"--scale={scale}"
        ]
        # Execute the command
        subprocess.run(command, check=True)
        print(f"Aztec Code successfully generated and saved as '{output_file}'")
    except FileNotFoundError:
        print("Error: 'zint' is not installed. Install it using 'brew install zint'.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to generate Aztec Code. {e}")

if __name__ == "__main__":
    # Data to encode
    data_to_encode = "Hello, Aztec Code!"  # Replace with your desired data
    output_image = "aztec_code.png"        # Replace with your desired file name

    # Generate Aztec Code
    generate_aztec_code(data=data_to_encode, output_file=output_image, scale=10)