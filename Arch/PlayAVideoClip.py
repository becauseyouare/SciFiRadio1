import cv2

# Capture the video from the specified path
cap = cv2.VideoCapture('your_video.mp4')

# Check if the video file was opened successfully
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Loop through the video frames
while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # If frame is not read correctly, break the loop
    if not ret:
        break

    # Display the frame
    cv2.imshow('Video Player', frame)

    # Wait for 1 millisecond and check for the 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
