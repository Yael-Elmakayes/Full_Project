from Mp_Detection import *
from Python_Libraries import*
def Example_key_points(res):
    if res.pose_landmarks:
        points_pose = np.array([[res.x, res.y, res.z, res.visibility] for res in res.pose_landmarks.landmark]).flatten()
        print("מערך ציוני דרך של תנוחות", points_pose)
    else:
        points_pose = np.zeros(33 * 4)
        print("מערך ציוני דרך של תנוחות",points_pose)
    if res.face_landmarks:
        points_face = np.array([[res.x, res.y, res.z] for res in res.face_landmarks.landmark]).flatten()
        print("מערך ציוני דרך של פנים", points_face)
    else:
        points_face = np.zeros(468 * 3)
        print("מערך ציוני דרך של פנים",points_face)
    if res.left_hand_landmarks:
        points_lh = np.array([[res.x, res.y, res.z] for res in res.left_hand_landmarks.landmark]).flatten()
        print("מערך ציוני דרך של יד שמאל", points_lh)
    else:
        points_lh = np.zeros(21 * 3)
        print("מערך ציוני דרך של יד שמאל",points_lh)
    if res.right_hand_landmarks:
        points_rh = np.array([[res.x, res.y, res.z] for res in res.right_hand_landmarks.landmark]).flatten()
        print("מערך ציוני דרך של יד ימין", points_rh)
    else:
        points_rh = np.zeros(21 * 3)
        print("מערך ציוני דרך של יד ימין",points_rh)
    return np.concatenate([points_pose, points_lh, points_rh])


