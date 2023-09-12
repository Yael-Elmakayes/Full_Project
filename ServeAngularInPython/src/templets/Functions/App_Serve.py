# import base64
# import io
# from flask import Flask, request, jsonify
# from flask_cors import CORS, cross_origin
# from PIL import Image
# from mediapipe_detection import*
# from holistic_drawing import*
# from extract_keypoints import*
# from keras.models import model_from_json


# app = Flask(__name__)
# CORS(app)

# @app.route('/python_process', methods=['POST'])
# #שרת עיבוד הפריימים
# def process_image():
#     image_data = request.json['image']
#     image_bytes = io.BytesIO(base64.b64decode(image_data))
#     img_bgr = cv2.imdecode(np.frombuffer(image_bytes.read(), np.uint8), cv2.IMREAD_COLOR)
#     with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
#         img,res=mediapipe_detection(img_bgr,holistic)
#         holistic_drawing(img,res)
#         keypoints = extract_keypoints(res)
#     _, img_encoded = cv2.imencode('.jpg', img)
#     processed_image = base64.b64encode(img_encoded).decode('utf-8')
#     return jsonify(keypoints)#מחזיר מערך של פריים יחיד


# # #טעינת המודל
# # json_file = open("model/model.json", 'r')
# # loaded_model_json = json_file.read()
# # json_file.close()
# # model = model_from_json(loaded_model_json)
# # # load weights into new mssodel
# # model.load_weights("model/model.h5")


# # # שליחה לשרת של המודל
# # @app.route('/predict', methods=['POST'])
# # def model():
# #  labels = np.array(['Please','Thanks' , 'y' , 'a' ,'e' ,'l'])# המילים שאימנו פה
# #  data = request.get_json()
# #  array = data['array']
# #  res = model.predict(np.expand_dims(array, axis=0))[0]
# #  name = str(labels[np.argmax(res)])
# #  return name
    
    
# if __name__ == '__main__':
#     app.run(debug=True)
    



