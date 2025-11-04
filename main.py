import cv2

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Could not open camera.")
else:
    while True:
        ret, frame = camera.read()
        flippedFrame = cv2.flip(frame, 1)
        grayFrame= cv2.cvtColor(flippedFrame, cv2.COLOR_BGR2GRAY)
        
        if not ret:
            print("Failed to grab frame.")
            break
        
        cv2.imshow('CAMERA', grayFrame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

camera.release()
cv2.destroyAllWindows()