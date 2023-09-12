from Python_Libraries import *
from Mp_Detection import *
from H_Drowing import *
from key_points import *


# # נתיב עבור נתונים מיוצאים, מערכים numpy
DATA_PATH = os.path.join("Data")
# # פעולות שאנו מנסים לזהות
labels = np.array(['Help', 'Father', 'M','i'])
# # נתונים בשווי מאה סרטונים
num_video = 100
# # אורך הסרטונים יהיה 30 פריימים
frame_len = 30

# פונקציה זו צריכה לפעול פעם אחת בלבד!
# def Makedirs():
#     for label in labels:
#         for seq in range(num_seqs):
#             try:
#                 os.makedirs(os.path.join(DATA_PATH, label, str(seq)))
#             except:
#                 pass
# # הפעלתי אותה פעם אחת עכשיו אני יכבה אותה
# Makedirs()
# פונקציה לצילום הנתונים גם היא תעבוד פעם אחת בלבד!

def Date_Capture():

    cap = cv2.VideoCapture(0)
    with Holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic_model:
        break_all = 0
        for label in labels: #  לכך מילה עושה את הנ"ל  עובר על המילים
            for seq in range(num_video):#num_seqs # נתונים בשווי 100 סרטונים
                for frame_num in range(frame_len):#seq_len לכל סרטון 30 תמונות -- פריימים
                    _, frame = cap.read()

                    img, results = Mp_detection(frame, holistic_model)# עובר למודל ההולסטי
                    H_drawing(img, results)#ציור תנוחות

                    if frame_num == 0:
                        if seq == 0: # הפריים הראשון מתוך ה-30
                            cv2.putText(img,
                                        'Press a Key to Start Collection for {} Video Number {}'.format(label, seq),
                                        (120, 200),
                                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 4, cv2.LINE_AA)
                            cv2.imshow('OpenCV Cam Feed', img)
                            cv2.waitKey(0)
                        cv2.putText(img, 'STARTING COLLECTION', (120, 300),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 4, cv2.LINE_AA)
                        cv2.putText(img, 'Collecting frames for {} Video Number {}'.format(label, seq), (15, 12),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                        cv2.imshow('OpenCV Cam Feed', img)
                        cv2.waitKey(2000)
                        # Show to screen
                    else:
                        cv2.putText(img, 'Collecting frames for {} Video Number {}'.format(label, seq), (15, 12),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                        # Show to screen
                        cv2.imshow('OpenCV Cam Feed', img)

                    # NEW Export keypoints
                    keypoints = key_points(results)
                    # seq -- פריים שצולם מתוך ה-100
                    npy_path = os.path.join(DATA_PATH, label, str(seq), str(frame_num))
                    np.save(npy_path, keypoints)
                    if cv2.waitKey(10) & 0xFF == ord('q'):
                        break_all = 1
                        break
                if break_all:
                    break
            if break_all:
                break
    cap.release()
    cv2.destroyAllWindows()
    cv2.waitKey(1)

Date_Capture()