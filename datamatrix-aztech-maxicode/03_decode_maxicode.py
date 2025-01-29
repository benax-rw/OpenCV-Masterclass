import subprocess
import os

def decode_maxicode_with_docker(image_path, docker_image="zxing-decoder"):
    """
    Decodes a MaxiCode using a Dockerized ZXing setup.
    Parameters:
        - image_path (str): Path to the MaxiCode image file to decode.
        - docker_image (str): Name of the Docker image containing ZXing.
    Returns:
        - Decoded result as a string or an error message if decoding fails.
    """
    # Ensure the file exists
    if not os.path.exists(image_path):
        return f"Error: File '{image_path}' not found."

    try:
        # Run the Docker command to decode the MaxiCode
        command = [
            "docker", "run", "--rm", "-v",
            f"{os.path.abspath(os.path.dirname(image_path))}:/data",
            docker_image, f"/data/{os.path.basename(image_path)}"
        ]
        result = subprocess.run(command, capture_output=True, text=True)

        # Check for errors
        if result.returncode != 0:
            return f"Error: {result.stderr.strip()}"

        # Return the decoded result
        return result.stdout.strip()

    except FileNotFoundError:
        return "Error: Docker is not installed or not accessible from this script."
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    # Path to the MaxiCode image file
    image_path = "maxicode.png"  # Replace with your MaxiCode image path

    # Decode the MaxiCode
    decoded_output = decode_maxicode_with_docker(image_path)

    # Print the result
    print(decoded_output)