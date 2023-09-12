from Libraries import*

def key_points(results):
    points_pose = np.zeros(33 * 4)
    if results.pose_landmarks:
        points_pose = np.array(
            [[res.x, res.y, res.z, res.visibility] for res in results.pose_landmarks.landmark]).flatten()

    points_face = np.zeros(468 * 3)
    if results.face_landmarks:
        points_face = np.array([[res.x, res.y, res.z] for res in results.face_landmarks.landmark]).flatten()

    points_lh = np.zeros(21 * 3)
    if results.left_hand_landmarks:
        points_lh = np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten()

    points_rh = np.zeros(21 * 3)
    if results.right_hand_landmarks:
        points_rh = np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten()

    return np.concatenate([points_pose, points_lh, points_rh])
