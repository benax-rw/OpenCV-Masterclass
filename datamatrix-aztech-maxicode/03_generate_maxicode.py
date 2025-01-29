import subprocess

def generate_maxicode(data, output_file="maxicode.png"):
    """
    Generates a MaxiCode using the zint command-line tool.
    Parameters:
        - data (str): The data to encode in the MaxiCode.
        - output_file (str): The file path to save the MaxiCode image.
    """
    try:
        # Construct the zint command for MaxiCode (barcode type 47)
        command = [
            "zint",
            "--barcode=57",  # MaxiCode type
            f"--data={data}",
            f"--output={output_file}"
        ]
        # Execute the command
        subprocess.run(command, check=True)
        print(f"MaxiCode saved as '{output_file}'")
    except FileNotFoundError:
        print("Error: 'zint' is not installed. Install it using 'brew install zint'.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to generate MaxiCode: {e}")

if __name__ == "__main__":
    data_to_encode = "123456789012"  # Replace with your data
    generate_maxicode(data_to_encode)