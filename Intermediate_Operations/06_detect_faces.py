import cv2

# Step 1: Load the pre-trained Haar cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Step 2: Read the image
image = cv2.imread("face_image.jpg")  # Replace with your image file
if image is None:
    print("Error: Image not found!")
    exit()

# Step 3: Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 4: Detect faces in the image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Step 5: Draw rectangles around detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)  # Green rectangle

# Step 6: Display the result
cv2.imshow("Detected Faces", image)

# Save the result
cv2.imwrite("faces_detected.jpg", image)

cv2.waitKey(0)
cv2.destroyAllWindows()