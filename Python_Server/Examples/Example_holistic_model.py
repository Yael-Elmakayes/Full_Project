from Mp_Detection import *
from Python_Libraries import*
# פונקצית הסבר למודל ההולסטי ולציוני דרך

def holistic_model():
    cap = cv2.VideoCapture(0)
    with Holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic_model:
        while cap.isOpened():
            _, frame = cap.read()
            img, results = Mp_detection(frame, holistic_model)
            cv2.imshow("OpenCV Cam feed", img)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                return results
    cap.release()
    cv2.destroyAllWindows()
    cv2.waitKey(1)


