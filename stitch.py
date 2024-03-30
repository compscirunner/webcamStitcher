import cv2
import numpy as np

# Open video captures for each webcam
cap1 = cv2.VideoCapture(0)
# cap2 = cv2.VideoCapture(1)
# cap3 = cv2.VideoCapture(2)

while True:
    # Read frames from each webcam
    ret1, frame1 = cap1.read()
    # ret2, frame2 = cap2.read()
    # ret3, frame3 = cap3.read()

    # Resize frames to a consistent size
    frame1 = cv2.resize(frame1, (640, 480))
    # frame2 = cv2.resize(frame2, (640, 480))
    # frame3 = cv2.resize(frame3, (640, 480))

    # Concatenate frames horizontally
    # stitched_frame = np.concatenate((frame1, frame2, frame3), axis=1)
    stitched_frame = np.concatenate((frame1,frame1,frame1), axis=1)
    # Display the stitched video
    cv2.imshow("Stitched Video", stitched_frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video captures and close windows
cap1.release()
# cap2.release()
# cap3.release()
cv2.destroyAllWindows()