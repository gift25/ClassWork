import cv2
import numpy as np

# Load the image
image = cv2.imread('C:/Users/us/Documents/Python/classWork2/Circle.png')


  # Replace 'your_image.jpg' with the path to your image

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise and improve circle detection
blurred = cv2.GaussianBlur(gray, (9, 9), 2)

# Use the Hough Circle Transform to detect circles in the image
circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=100, param2=30, minRadius=0, maxRadius=0)

# If circles are found, draw them and mark their centers
if circles is not None:
    circles = np.uint16(np.around(circles))
    
    # Initialize a list to store unique centers
    unique_centers = []

    for circle in circles[0, :]:
        center = (circle[0], circle[1])
        
        # Print the center coordinates
        print(f"Center: {center}")
        
        # Check if the center is close to any previously detected centers
        is_duplicate = False
        for existing_center in unique_centers:
            if np.linalg.norm(np.array(center) - np.array(existing_center)) < 10:
                is_duplicate = True
                break
        
        # If not a duplicate, draw the circle and mark the center
        if not is_duplicate:
            unique_centers.append(center)
            cv2.circle(image, center, 1, (0, 100, 100), 3)  # Draw the center as a small circle
            cv2.circle(image, center, circle[2], (255, 0, 0), 2)  # Draw the outer circle
            cv2.putText(image, f"Center: {center}", (circle[0] - 20, circle[1] - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Display the image with circles and centers
    cv2.imshow('Circle Detection', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No circles found in the image.")
