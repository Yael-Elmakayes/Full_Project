import numpy as np

from Mp_Detection import *
from H_Drowing import *
from key_points import *
from Python_Libraries import *

labels = np.array(['Help', 'Father', 'M','i'])
# טעינת המודל
json_file = open('Model\\model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
model.load_weights("Model\\model.h5")
print("Loaded model from disk")


# sequence = []
# sentence = []
# predictions = []
# threshold = 0.7
# frames = []
# cap = cv2.VideoCapture(0)
# # Set mediapipe model
# with Holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
#     while cap.isOpened():
#         ret, frame = cap.read()
#         img, res = Mp_detection(frame, holistic)
#         print(res)#מחזיר ציוני דרך של מה שתפסה המסגרת
#         H_drawing(img, res)
#         key_points(res)
#         arr_points = key_points(res)
#         print(arr_points.shape)
#         frames.append(arr_points)
#         frames = frames[-30:]
#         frame_test = np.array(frames)
#         print(frame_test.shape)
#         if len(frames) == 30:
#             #עכשיו אחרי שהמערך התמלא ב30 פריימים הראשונים אפשר להעביר למודל לצורך חיזוי המילה או האות
#             frames = np.array(frames)
#             res = model.predict(np.expand_dims(frames, axis=0))[0]
#             print(labels[np.argmax(res)])
#             if np.unique(predictions[-10:])[0] == np.argmax(res):
#                     if res[np.argmax(res)] > threshold:
#                             if len(sentence) > 0:
#                                if labels[np.argmax(res)] != sentence[-1] and len(labels[np.argmax(res)]) > 1:
#                                    sentence.append(labels[np.argmax(res)])
#                                    f = open("WORD.txt", "a")
#                                    f.write(" " + str(labels[np.argmax( res)]) + " ")
#                                    f.close()
#                             else:
#                                if labels[np.argmax(res)] != sentence[-1] and len(
#                                    labels[np.argmax(res)]) == 1:  # אומר לו לך למערך של התוויות במקום שהמודל חזה
#                                    sentence.append(labels[np.argmax(res)])
#                                    f = open("WORD.txt", "a")
#                                    f.write(str(labels[np.argmax(res)]))
#                                    f.close()
#                     else:
#                         sentence.append(labels[np.argmax(res)])
#             if len(sentence) > 5:
#                 sentence = sentence[-5:]
#
#
#
#         cv2.imshow('OpenCV Feed', img)
#         if cv2.waitKey(10) & 0xFF == ord('q'):
#             break
#     cap.release()
#     cv2.destroyAllWindows()
#
#










#
# colors = [(245, 117, 16), (117, 245, 16), (16, 117, 245), (16, 117, 245), (16, 117, 245), (16, 117, 245)]
#
#
# def prob_viz(res, actions, input_frame, colors):
#     output_frame = input_frame.copy()
#     for num, prob in enumerate(res):
#         cv2.rectangle(output_frame, (0, 60 + num * 40), (int(prob * 100), 90 + num * 40), colors[num], -1)
#         cv2.putText(output_frame, actions[num], (0, 85 + num * 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2,
#                     cv2.LINE_AA)
#
#     return output_frame


# 1. New detection variables
sequence = []
sentence = []
predictions = []
threshold = 0.5

cap = cv2.VideoCapture(0)
# Set mediapipe model
with Holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():

        ret, frame = cap.read()

        # Make detections
        image, results = Mp_detection(frame, holistic)
        print(results)#מחזיר ציוני דרך של מה שתפסה המסגרת

        # Draw landmarks
        H_drawing(image, results)

        # 2. היגיון חיזוי
        keypoints = key_points(results)
        print(keypoints.shape)
        sequence.append(keypoints)
        sequence = sequence[-30:]
        sequence_array = np.array(sequence)
        print(sequence_array.shape)  # Output: (5,)
        if len(sequence) == 30:#ברגע שהגעת ל30 מסגרות אפשר להכנ
            # יס למודל לצורך חיזוי
            sequence_array = np.array(sequence)
            print(sequence_array.shape)  # Output: (5,)
            res = model.predict(np.expand_dims(sequence, axis=0))[0]
            # print(labels[np.argmax(res)])
            predictions.append(np.argmax(res))#זה המערך של המיליםנ
            # 3. Viz logic
            if np.unique(predictions[-10:])[0] == np.argmax(res):
                if res[np.argmax(res)] > threshold:
                    if len(sentence)==0:
                        f = open("WORD.txt", "a")
                        f.write(" " + str(labels[np.argmax(res)]) + " ")
                        f.close()
                    if len(sentence) > 0:
                        if labels[np.argmax(res)] != sentence[-1] and len(labels[np.argmax(res)]) > 1:
                            sentence.append(labels[np.argmax(res)])
                            f = open("WORD.txt", "a")
                            f.write(" " + str(labels[np.argmax( res)]) + " ")

                            f.close()
                        else:
                            if labels[np.argmax(res)] != sentence[-1] and len( labels[np.argmax(res)]) == 1:
                                    # אומר לו לך למערך של התוויות במקום שהמודל חזה
                                sentence.append(labels[np.argmax(res)])
                                f = open("WORD.txt", "a")
                                f.write(str(labels[np.argmax(res)]))
                                f.close()
                                # TypeError: can only concatenate str (not "type") to str   פתרנו על ידי שהוספנו המרה ל str
                    else:
                        sentence.append(labels[np.argmax(res)])

            if len(sentence) > 5:
                sentence = sentence[-5:]

            # כלומר הסתברויות
            # image = prob_viz(res, labels, image, colors)

        cv2.rectangle(image, (0, 0), (640, 40), (245, 117, 16), -1)
        cv2.putText(image, ' '.join(sentence), (3, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

        # Show to screen
        cv2.imshow('OpenCV Feed', image)

        # Break gracefully
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    cap.release()

    cv2.destroyAllWindows()


