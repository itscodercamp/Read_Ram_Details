import cv2
import numpy as np
import pyautogui

# Set the screen capture dimensions (you may need to adjust this)
screen_width = 1920
screen_height = 1080

# Create a window to display the screen content
cv2.namedWindow("Live Presentation Screen", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live Presentation Screen", screen_width, screen_height)

while True:
    # Capture the screen content
    screenshot = pyautogui.screenshot()
    frame = np.array(screenshot)

    # Convert the frame to BGR format (OpenCV uses BGR)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Display the screen content in the OpenCV window
    cv2.imshow("Live Presentation Screen", frame)

    # Break the loop when the 'q' key is pressed
    if cv2.waitKey(1) == ord("q"):
        break

# Release resources
cv2.destroyAllWindows()
