from Libraries import*


def H_drawing(img, holistic_res):
    # צייר חיבורי פנים
    mp_drawing.draw_landmarks(img, holistic_res.face_landmarks, mp_holistic.FACEMESH_TESSELATION,
                             mp_drawing.DrawingSpec(color=(80,110,10), thickness=1, circle_radius=1),
                             mp_drawing.DrawingSpec(color=(80,256,120), thickness=1, circle_radius=1)
                             )
    # צייר חיבורי תנוחה
    mp_drawing.draw_landmarks(img, holistic_res.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                             mp_drawing.DrawingSpec(color=(200,50,50), thickness=2, circle_radius=4),
                             mp_drawing.DrawingSpec(color=(200,25,25), thickness=2, circle_radius=2)
                             )
       # צייר חיבורים ביד שמאל
    mp_drawing.draw_landmarks(img, holistic_res.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                             mp_drawing.DrawingSpec(color=(25,25,200), thickness=2, circle_radius=4),
                             mp_drawing.DrawingSpec(color=(50,50,200), thickness=2, circle_radius=2)
                             )
     # צייר חיבורים ביד ימין
    mp_drawing.draw_landmarks(img, holistic_res.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                             mp_drawing.DrawingSpec(color=(25,25,200), thickness=2, circle_radius=4),
                             mp_drawing.DrawingSpec(color=(50,50,200), thickness=2, circle_radius=2)
                             )