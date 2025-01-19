import segno

# Data to encode
data = "https://benax.rw"

# Generate the code
matrix = segno.make(data)

# Save the code as a PNG
matrix.save("datamatrix_simulation.png", scale=10)
print("Simulated Data Matrix code saved as datamatrix_simulation.png")