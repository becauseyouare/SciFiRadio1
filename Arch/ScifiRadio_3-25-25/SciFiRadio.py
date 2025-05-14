# This is Science Fiction Radio Version 0.05(ish)
# An Arduino attached to USB port 0 spits out numbers from 0 to 1024
# a golactic radio dial image "RadioDial_4x3.png" is displayed full screen
# a pointer indicates something related to the number received
# should be displayed on a 1280 x 1024 monitor for full effect
# by Tom McGuire 2/21/2025

import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
import serial
import time

def create_needle(image, center, angle, length, color=(44,94,148), thickness=4):
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

def update_dial():
    global current_value, needle_image, photo, running

    if not running:
        return

    # Calculate the needle angle
    angle = (current_value / 1023) * 360

    # Create the needle image
    needle_image = create_needle(dial_image.copy(), center, angle, needle_length)

    # Convert the needle image to PIL Image for Tkinter
    pil_image = Image.fromarray(cv2.cvtColor(needle_image, cv2.COLOR_BGR2RGB))
    photo = ImageTk.PhotoImage(image=pil_image)

    # Update the canvas
    canvas.create_image(0, 0, image=photo, anchor=tk.NW)
    root.update()

    # Update value (for demonstration)
    current_value = current_value % 1024
    if ser.in_waiting > 0:
        data = ser.readline().decode('utf-8').strip()
        if data.isdigit():
            current_value = int(data)
            
    print(hex(current_value)+" ")

    # Schedule the next update
    root.after(10, update_dial)

def stop_animation(event):
    global running
    running = False
    ser.close()
    root.destroy()  # Close the window

# configure serial port
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=2, xonxoff=False)
print(f"Port {ser.name} open: {ser.is_open} \n")

# Load the dial image
dial_image = cv2.imread("RadioDial_4x3.png") 

# Get the center of the dial
center = (dial_image.shape[1] // 2, dial_image.shape[0] // 2)

# Define the needle length
needle_length = 350

# Initialize Tkinter
root = tk.Tk()
root.attributes('-fullscreen', True)  # Set to full screen

# Create a canvas to display the image
canvas = tk.Canvas(root, width=dial_image.shape[1], height=dial_image.shape[0])
canvas.pack()

# Initialize current value and running flag
current_value = 1
running = True

# Create the initial needle image
needle_image = create_needle(dial_image.copy(), center, 0, needle_length) 

# Convert the needle image to PIL Image for Tkinter
pil_image = Image.fromarray(cv2.cvtColor(needle_image, cv2.COLOR_BGR2RGB))
photo = ImageTk.PhotoImage(image=pil_image)

# Display the initial image
canvas.create_image(0, 0, image=photo, anchor=tk.NW)

# Bind any key press to the stop_animation function
root.bind("<Any Key>", stop_animation)

# Start the update loop
update_dial()

root.mainloop()
