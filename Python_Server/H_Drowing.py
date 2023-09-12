from Python_Libraries import*

def H_drawing(img, holistic_res):
    # צייר חיבורי פנים
    Drawing.draw_landmarks(img, holistic_res.face_landmarks, Holistic.FACEMESH_TESSELATION,
                           Drawing.DrawingSpec(color=(218, 112, 214), thickness=1, circle_radius=1),
                           Drawing.DrawingSpec(color=(218, 112, 214), thickness=1, circle_radius=1)
                           )
    # צייר חיבורי תנוחה
    Drawing.draw_landmarks(img, holistic_res.pose_landmarks, Holistic.POSE_CONNECTIONS,
                           Drawing.DrawingSpec(color=(255, 255, 255), thickness=2, circle_radius=4),
                           Drawing.DrawingSpec(color=(255, 255, 255), thickness=2, circle_radius=2)
                           )
    # צייר חיבורים ביד שמאל
    Drawing.draw_landmarks(img, holistic_res.left_hand_landmarks, Holistic.HAND_CONNECTIONS,
                           Drawing.DrawingSpec(color=(0, 0, 0), thickness=2, circle_radius=4),
                           Drawing.DrawingSpec(color=(0, 0, 0), thickness=2, circle_radius=2)
                           )
    # צייר חיבורים ביד ימין
    Drawing.draw_landmarks(img, holistic_res.right_hand_landmarks, Holistic.HAND_CONNECTIONS,
                           Drawing.DrawingSpec(color=(0, 0, 0), thickness=2, circle_radius=4),
                           Drawing.DrawingSpec(color=(0, 0, 0), thickness=2, circle_radius=2)
                           )
