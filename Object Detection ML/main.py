import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox

from Commands.calculate_center import calculate_rotation_command

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

first_person_bbox = None
while True:
    ret, frame = cap.read()

    bbox, label, conf = cv.detect_common_objects(frame)

    if 'person' in label:
        # if first_person_bbox is None:
        #     first_person_index = label.index('bottle')
        #     first_person_bbox = bbox[first_person_index]       
        output_image = draw_bbox(frame, bbox, label, conf)
        calculate_rotation_command(bbox, screen_width = frame.shape[1], screen_height = frame.shape[0])
    else:
        # If no person is detected, keep showing the original frame
        output_image = frame


    # Check if frame is read correctly
    if not ret:
        print("Error: Could not read frame.")
        break

    # Display the frame
    cv2.imshow('Camera', output_image)

    # Wait for 'q' key to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
