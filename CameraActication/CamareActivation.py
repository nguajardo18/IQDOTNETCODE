import cv2

# Create a VideoCapture object
cap = cv2.VideoCapture(0)  # Use 0 to capture from the default camera

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    
    # Check if the frame was read successfully
    if not ret:
        print("Error: Could not read frame.")
        break
    
    # Display the frame
    cv2.imshow('Camera Feed', frame)
    
    # Capture a frame when 's' key is pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        # Save the frame as an image
        cv2.imwrite('captured_frame.jpg', frame)
        print("Frame captured and saved as 'captured_frame.jpg'")
    elif key == ord('q'):
        break

# Release the VideoCapture object and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
#IQDOTNET CODE - By Nelson Guajardo 