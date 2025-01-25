import subprocess
import os

# Path to the QR Code image
qr_image_path = "kanji_kana_qrcode.png"
output_file = "decoded_kanji_kana.txt"

# Docker command to decode the QR Code
command = [
    "docker", "run", "--rm",
    "-v", f"{os.getcwd()}:/app",  # Mount current directory to /app
    "openjdk:17",
    "java", "-cp",
    "/app/javase-3.5.0.jar:/app/core-3.5.0.jar:/app/jcommander-1.82.jar",
    "com.google.zxing.client.j2se.CommandLineRunner",
    f"/app/{qr_image_path}"
]

try:
    # Execute the Docker command
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    decoded_output = result.stdout

    # Save the decoded output to a file
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(decoded_output)
    print(f"Decoded content saved to '{output_file}'")

except subprocess.CalledProcessError as e:
    print("Error during decoding:")
    print(e.stderr)