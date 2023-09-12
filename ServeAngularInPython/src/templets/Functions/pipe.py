# from flask import Flask, request, jsonify
# import cv2
# from flask_cors import CORS
# import numpy as np
# import base64
# import mediapipe as mp
# from flask import Flask, request, jsonify
# import cv2
# import numpy as np
# import base64
# from io import BytesIO
# from mediapipe_detection import*
# from holistic_drawing import*
# from extract_keypoints import*


# from keras.models import model_from_json

# mp_holistic = mp.solutions.holistic
# mp_drawing = mp.solutions.drawing_utils
# app = Flask(__name__)
# CORS(app)
# #טעינת המודל
# labels = np.array(['Please','Thanks' , 'y' , 'a' ,'e' ,'l'])# המילים שאימנו פה
# json_file = open("model/model.json", 'r')
# loaded_model_json = json_file.read()
# json_file.close()
# model = model_from_json(loaded_model_json)
# # load weights into new mssodel
# model.load_weights("model/model.h5")
# @app.route('/process_image', methods=['POST'])

# def process_image():
#     image_data = request.json['image']
#     image_bytes = BytesIO(base64.b64decode(image_data))
#     img_bgr = cv2.imdecode(np.frombuffer(image_bytes.read(), np.uint8), cv2.IMREAD_COLOR)
#     with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
#         img,res=mediapipe_detection(img_bgr,holistic)
#         holistic_drawing(img,res)
#         keypoints = extract_keypoints(res)
#     _, img_encoded = cv2.imencode('.jpg', img)
#     processed_image = base64.b64encode(img_encoded).decode('utf-8')
#     return jsonify({'processed_image': processed_image})
# if __name__ == '__main__':
#     app.run(debug=True)