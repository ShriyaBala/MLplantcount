import cv2

# Load the image
# Replace 'crop_field.jpg' with your image file path
image = cv2.imread("Images/caax3.jpeg")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a threshold to create a binary image
_, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

# Find contours in the binary image
contours, _ = cv2.findContours(
    binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Initialize a counter for counting the crops
crop_count = 0

# Loop through the contours
for contour in contours:
    # Calculate the area of the contour
    area = cv2.contourArea(contour)

    # You can adjust this threshold to suit your specific image
    if area > 100:  # Adjust the threshold as needed
        # Draw a rectangle around the detected crop
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Increment the crop count
        crop_count += 1

# Display the image with contours and count
cv2.putText(image, f'Crop Count: {crop_count}', (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
cv2.imshow('Crops in a Row', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Print the total crop count
print(f"Total Crop Count: {crop_count}")
