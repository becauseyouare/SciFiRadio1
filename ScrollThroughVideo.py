import cv2

def scroll_frames(video_path):
    """
    Allows scrolling through video frames using the spacebar and exiting with the 'q' key.

    Args:
        video_path (str): Path to the video file.
    """
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return

    frame_number = 0
    while True:
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        ret, frame = cap.read()

        if not ret:
            print("End of video.")
            break

        cv2.imshow('Video Frame', frame)
        key = cv2.waitKey(0) & 0xFF  # Wait for a key press

        if key == ord(' '):  # Spacebar: advance to next frame
            frame_number += 1
        elif key == ord('q'):  # 'q' key: exit
            break
        elif key == 8:  # Backspace: go to previous frame
            frame_number = max(0, frame_number - 1) # avoid negative frame numbers
        elif key == 27:  # Escape key: exit
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_file = 'SciFiRadioTestVid4.1.mp4'  # Replace with your video file path
    scroll_frames(video_file)