# # הקדמה
# from flask import Flask, request, jsonify
# from flask_cors import CORS, cross_origin
# import base64
# from io import BytesIO
# import io
# from PIL import Image
# import numpy as np
# import cv2
# from keras.models import load_model
# import tensorflow as tf
# from keras.models import model_from_json


# json_file = open("model/model.json", 'r')
# loaded_model_json = json_file.read()
# json_file.close()
# model = model_from_json(loaded_model_json)

# # load weights into new model
# model.load_weights("model/model.h5")

# app = Flask(__name__)
# CORS(app)
# # מהשרת התחברתי ללקוח והצגתי שמה את     מה שהקלידו לי.
# # פונקציה מספר 1
# @app.route('/api/greeting', methods=['POST'])
# @cross_origin()
# def greetiing():
#     username = request.json.get('username')
#     # username="Eli"
#     message = f"Hello, {username}!"
#     response = {'message': message}
#     return (response)


# # פונקציה ללכידת פריימים מממצלמת האינטרנט שלי בזמן אמת והעברתן לעיבוד ולחיזוי על פי המודל המאומן שלי
# # פונקציה מספר 2


# @app.route('/decode_image', methods=['POST'])
# @cross_origin()
# def ecode_image():
#     data = request.get_data()
#     image = Image.open(io.BytesIO(base64.b64decode(data)))
#     image = np.array(image)
#     image = image / 255.0  # normalize the pixel values
#     result = model.predict(np.array([image]))[0]
#     label = np.argmax(result)
#     return jsonify({'label': str(label)})

# # הרצה
# if __name__ == '__main__':
#     app.run(debug=True)