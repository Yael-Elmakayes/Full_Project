import io
import json
from tkinter import Image
from flask import Flask, request
import face_recognition
from flask_cors import CORS
import cv2
import os
app = Flask(__name__)
CORS(app)


@app.route('/register', methods=['POST'])
def register():
    if not os.path.exists('faces'):
     os.makedirs('faces')
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    name = request.form['name']
    id = request.form['id']
    print(id)
    print(name)
    frames = json.loads(request.form['frames'])
    
    # photos = []
    # for i in range(10):
    #     photo = request.files[f'photo{i}']
    #     photo.save(f'{name}_{id}_photo{i}.jpg')
    #     photos.append(face_recognition.load_image_file(photo))
    
    # # Process each frame and append it to the photos array
    # for i, frame in enumerate(frames):
    #     frame_image = Image.open(io.BytesIO(frame))
    #     # TODO: Process the frame image as needed
    #     frame_image.save(f'{name}_{id}_frame{i}.jpg')
    #     photos.append(face_recognition.load_image_file(f'{name}_{id}_frame{i}.jpg'))
    # known_face_encodings = [face_recognition.face_encodings(photo)[0] for photo in photos]
    # known_face_names = [f'{name}_{id}' for _ in range(len(photos))]
    # # Train the face recognition model on the known face encodings
    # face_recognition_model = face_recognition.api.face_encoder.FaceEncoder()
    # face_recognition_model.fit(known_face_encodings, known_face_names)
    # # Use the first photo to identify the person
    # unknown_face_encoding = face_recognition.face_encodings(photos[0])[0]
    # results = face_recognition_model.predict(unknown_face_encoding)
    # if len(results) > 0:
    #     identified_name = results[0]
    #     return f'Welcome, {identified_name}!'
    # else:
    #     return 'Sorry, we could not identify you.'

if __name__ == '__main__':
    app.run(port=5000)