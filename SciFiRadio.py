import cv2
import numpy as np

def create_needle(image, center, angle, length, color=(0, 0, 255), thickness=4):
    """
    Creates a needle image overlay.

    Args:
        image: The background image.
        center: Tuple (x, y) representing the center of the dial.
        angle: Angle of the needle in degrees (0 is pointing upwards).
        length: Length of the needle.
        color: Color of the needle (BGR format).
        thickness: Thickness of the needle line.

    Returns:
        The image with the needle drawn on it.
    """
    image = image.copy() 
    angle_rad = np.radians(angle)
    end_x = center[0] + int(length * np.cos(angle_rad))
    end_y = center[1] + int(length * np.sin(angle_rad))
    cv2.line(image, center, (end_x, end_y), color, thickness)
    return image

def main():
    # Load the dial image
    dial_image = cv2.imread("RadioDial2.png") 

    # Get the center of the dial (assuming it's the center of the image)
    center = (dial_image.shape[1] // 2, dial_image.shape[0] // 2)

    # Define the needle length (adjust as needed)
    needle_length = 330 

    # Loop through input values (0 to 1023)
    for value in range(1024):
        # Calculate the needle angle (adjust mapping as needed)
        angle = (value / 1023) * 360  # Map input to 0-360 degrees

        # Create the needle image
        needle_image = create_needle(dial_image.copy(), center, angle, needle_length)

        # Display the image (optional)
        cv2.imshow("Dial", needle_image)
        cv2.waitKey(10)  # Adjust wait time for animation speed

if __name__ == "__main__":
    main()

"""
Explanation:

Import necessary libraries:

cv2: OpenCV for image processing.
numpy: For numerical operations.
create_needle function:

Takes the image, center coordinates, angle, length, color, and thickness as input.
Calculates the end coordinates of the needle based on the angle and length.
Draws a line on the image representing the needle.
Returns the modified image with the needle.
main function:

Loads the dial image using cv2.imread().
Calculates the center of the dial.
Defines the needle length.
Iterates through input values from 0 to 1023.
Calculates the needle angle based on the input value (adjust the mapping as needed).
Calls create_needle to generate the image with the needle at the calculated angle.
Displays the image using cv2.imshow() and waits for a short duration.
To use this code:

Save the code: Save the code as a Python file (e.g., dial_animation.py).
Replace "dial.png": Replace "dial.png" with the actual path to your dial image.
Adjust parameters:
Modify needle_length to change the needle's length.
Adjust the angle calculation within the loop to change the mapping of input values to needle angles.
Modify cv2.waitKey() to control the animation speed.
Run the script: Execute the script using python dial_animation.py.
This will create an animation of the needle moving across the dial based on the input values.

Note:

This code provides a basic framework. You can further enhance it by:
Adding more sophisticated needle designs.
Implementing smoother animations.
Integrating with external input sources (e.g., sensor readings).
Remember to install OpenCV using pip install opencv-python.
This code assumes the dial is centered in the image. You may need to adjust the center calculation if this is not the case.
"""