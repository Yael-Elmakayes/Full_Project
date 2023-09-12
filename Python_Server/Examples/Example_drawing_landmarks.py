from Python_Libraries import*
from H_Drowing import*
from Mp_Detection import*
def Drowing():
    cap = cv2.VideoCapture(0)
    # Set mediapipe model
    with Holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        while cap.isOpened():
            ret, frame = cap.read()
            image, results = Mp_detection(frame, holistic)
            # Draw landmarks
            H_drawing(image, results)
            cv2.imshow('OpenCV Feed', image)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()