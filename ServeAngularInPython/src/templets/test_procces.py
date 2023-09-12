
# import base64
# from flask import Flask, request, jsonify
# from io import BytesIO
# from PIL import Image
# from flask_cors import CORS

# import mediapipe as mp # ספריה לראיה ממוחשבת  לצורך זיהוי פנים וידיים
# import numpy as np # עבודה על מערכים קריטי ללמידת מכונה
# import cv2 # ספריית קוד פתוח לזיהוי פנים ועיבוד תמונה
# import pandas as pd # עבודה על קבצים קריאה כתיבה וכו
# import os# מאפשר ליצור אינטראקציה עם מספר פונקציות של מערכת ההפעלה
# from sklearn.model_selection import train_test_split #   אלגורתמים + משמש לבניית מודלים של למידת מכונה
# from keras.utils import to_categorical # משמש ללמידה עמוקה ולבניית השכבות במודלים
# from scipy import stats # היא ספריית קוד פתוח המשמשת לפתרון בעיות מתמטיות, מדעיות, הנדסיות וטכניות
# from matplotlib import pyplot as plt # היא ספרייה מקיפה ליצירת הדמיות סטטיות
# # from bidi.algorithm import get_display
# from keras.models import Sequential
# from keras.layers import LSTM, Dense
# # LSTM -  שכבה לביצוע פעותות זמן
# #DENSE - שכבה רגילה
# from keras.callbacks import ModelCheckpoint
# from keras.models import model_from_json




# app = Flask(__name__)
# CORS(app)
# @app.route('/process-image', methods=['POST'])
# def process_image():

    
#     file = request.files['image']
#     image = Image.open(BytesIO(file.read()))
    
#     # results = mediapipe_detection(image, holistic)
    
#     bw_image = image.convert('L')
#     buffer = BytesIO()
#     bw_image.save(buffer, format='JPEG')
#     image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
#     return jsonify({'image': image_base64})

# if __name__ == '__main__':
#     app.run(debug=True)


# #טעינת המודל
# labels = np.array(['Please','Thanks' , 'y' , 'a' ,'e' ,'l'])# המילים שאימנו פה
# json_file = open("model/model.json", 'r')
# loaded_model_json = json_file.read()
# json_file.close()
# model = model_from_json(loaded_model_json)
# # load weights into new mssodel
# model.load_weights("model/model.h5")
# from flask import Flask, request, jsonify
# import numpy as np

# app = Flask(__name__)
# CORS(app)
# @app.route('/train', methods=['POST'])
# def train():
#     # Get frames data from request body
#     frames = np.array(request.json['frames'])#אוקייי כל המסגרות מאוכסנות עכשיו כמערך numpy
#     res = model.predict(np.expand_dims(frames, axis=0))[0]
#     p=str(labels[np.argmax(res)])
#     prediction = {'result': p}
#     return jsonify(prediction)

# if __name__ == '__main__':
#     app.run(host='localhost', port=8000)


from keras.models import load_model
from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import tensorflow as tf

#טעינת המודל המאומן
labels = np.array(['Help', 'Father', 'M','i'])
json_file = open("Model/model.json", 'r')
loaded_model_json = json_file.read()
json_file.close()
model = tf.keras.models.model_from_json(loaded_model_json)
model.load_weights("Model/model.h5")


sentence = []
predictions = []
threshold = 0.4
app = Flask(__name__)
CORS(app)
@app.route('/process_frames', methods=['POST'])
def process_frames():
    frames =request.json['frames']
    #הדפסת המימד של המערך שקיבלנו מצד לקוח 
    my = np.array(frames)
    print(my.shape)
    #שליחה למודל
    res = model.predict(np.expand_dims(frames, axis=0))[0]
    print(str(labels[np.argmax(res)]))
    if res[np.argmax(res)] > threshold:
            p = str(labels[np.argmax(res)])
            return jsonify({'prediction': p})
    else:
          return jsonify({"error": "some error message"})
if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
    