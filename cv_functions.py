import streamlit as st
import cv2
import numpy as np

# Define constants for image processing
MIN_GREEN_HUE = 45
MAX_GREEN_HUE = 77
MIN_GREEN_SAT = 19
MAX_GREEN_SAT = 255
MIN_GREEN_VAL = 164
MAX_GREEN_VAL = 255

def process_image(img):
    # Convert the image to the HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds for green color
    lower_green = np.array([MIN_GREEN_HUE, MIN_GREEN_SAT, MIN_GREEN_VAL])
    upper_green = np.array([MAX_GREEN_HUE, MAX_GREEN_SAT, MAX_GREEN_VAL])

    # Create a mask to isolate the green regions
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Apply morphological operations to the mask to clean up noise
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel, iterations=2)
    mask = cv2.dilate(mask, kernel, iterations=2)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Count the number of contours (plants)
    plant_count = len(contours)

    # Draw the contours on the original image
    img_with_contours = img.copy()
    cv2.drawContours(img_with_contours, contours, -1, (0, 255, 0), 2)

    return img_with_contours, plant_count

def main():
    st.title("Plant Counting App")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        img = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)

        st.image(img, caption="Uploaded Image", use_column_width=True)

        if st.button("Process Image"):
            processed_img, plant_count = process_image(img)
            st.image(processed_img, caption=f"Processed Image (Plants: {plant_count})", use_column_width=True)

if __name__ == "__main__":
    main()
