
import base64
import json
from flask import Flask, request, jsonify
from io import BytesIO
from PIL import Image
from flask_cors import CORS
import base64
import io
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from PIL import Image
from mediapipe_detection import*
from holistic_drawing import*
from extract_keypoints import*
from keras.models import model_from_json
import mediapipe as mp # ספריה לראיה ממוחשבת  לצורך זיהוי פנים וידיים
import numpy as np # עבודה על מערכים קריטי ללמידת מכונה
import cv2 # ספריית קוד פתוח לזיהוי פנים ועיבוד תמונה
import pandas as pd # עבודה על קבצים קריאה כתיבה וכו
import os# מאפשר ליצור אינטראקציה עם מספר פונקציות של מערכת ההפעלה
from sklearn.model_selection import train_test_split #   אלגורתמים + משמש לבניית מודלים של למידת מכונה
from keras.utils import to_categorical # משמש ללמידה עמוקה ולבניית השכבות במודלים
from scipy import stats # היא ספריית קוד פתוח המשמשת לפתרון בעיות מתמטיות, מדעיות, הנדסיות וטכניות
from matplotlib import pyplot as plt # היא ספרייה מקיפה ליצירת הדמיות סטטיות
# from bidi.algorithm import get_display
from keras.models import Sequential
from keras.layers import LSTM, Dense
# LSTM -  שכבה לביצוע פעותות זמן
#DENSE - שכבה רגילה
from keras.callbacks import ModelCheckpoint
from keras.models import model_from_json



# app = Flask(__name__)
# CORS(app)
# @app.route('/process-image', methods=['POST'])
# def process_image():
#     # Get the image file from the request
#     img_file = request.files['image']

#     # Read the image file as a NumPy array
#     img_array = np.frombuffer(img_file.read(), np.uint8)
#     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#     image,results = mediapipe_detection(img,mp_holistic)
#     holistic_drawing(image, results)
#     _, encoded_img = cv2.imencode('.jpg', image)
#     encoded_img_str = base64.b64encode(encoded_img).decode('utf-8')
#     return jsonify({'image': encoded_img_str})
# if __name__ == '__main__':
#     app.run(debug=True)

#קוד קודם   היה שגיאה בשליחה משו בקטנה בכל זאת רץ

# import base64
# import cv2
# import numpy as np
# import asyncio
# import websockets


# async def process_frame(websocket, path):
#     async for message in websocket:
#         data = json.loads(message)
#         image_data = data['image']
#         image_data = image_data.split(',')[1]
#         image_bytes = base64.b64decode(image_data)
#         img_bgr = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)
#         with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
#             img,res=mediapipe_detection(img_bgr,holistic)
#             holistic_drawing(img,res)
#             keypoints = extract_keypoints(res)
#             array_list = keypoints.tolist()
#             ret, buffer = cv2.imencode('.jpg', img)
#             processed_image_data = base64.b64encode(buffer).decode('utf-8')
#             await websocket.send(json.dumps(array_list))

# if __name__ == '__main__':
#     start_server = websockets.serve(process_frame, 'localhost', 8000)
#     asyncio.get_event_loop().run_until_complete(start_server)
#     asyncio.get_event_loop().run_forever()

#  הקוד המתוקןן

import base64
import cv2
import numpy as np
import asyncio
import websockets
async def process_frame(websocket, path):
    try:
        async for message in websocket:
            data = json.loads(message)
            image_data = data['image']
            image_data = image_data.split(',')[1]
            image_bytes = base64.b64decode(image_data) 
            img_bgr = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)
            with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
                img,res=Mp_detection(img_bgr,holistic)
                H_drawing(img,res)
                keypoints = key_points(res)
                array_list = keypoints.tolist()
                ret, buffer = cv2.imencode('.jpg', img)
                processed_image_data = base64.b64encode(buffer).decode('utf-8')
                await websocket.send(json.dumps(array_list))
    except websockets.exceptions.ConnectionClosedError:
        pass
if __name__ == '__main__':
    start_server = websockets.serve(process_frame, 'localhost', 8000)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
    
    