from flask import Flask, jsonify, request
from flask_cors import CORS
import numpy as np
import face_recognition
import cv2

def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.route("/authenticate", methods=['POST'])
    def authenticate():
        # Upload known face
        face_encodings = []
        addEncondingFace("..\\src\\assets\\images\juan\\edu2.jpg",face_encodings)
        addEncondingFace("..\\src\\assets\\images\\juan\\edu1.png",face_encodings)
        addEncondingFace("..\\src\\assets\\images\\juan\\0.jpg",face_encodings)
        addEncondingFace("..\\src\\assets\\images\\juan\\Gabe.jpg",face_encodings)
        addEncondingFace("..\\src\\assets\\images\\juan\\Chris.jpg",face_encodings)
        # base_img = cv2.cvtColor(base_img, cv2.COLOR_BGR2RGB)
        # encode_my_face = face_recognition.face_encodings(base_img)
        # Get image from request
        # sample_image_bytes = request.files['face'].stream.read()
        # sample_image_np_array = np.fromstring(sample_image_bytes, np.uint8)
        # sample_image = cv2.imdecode(sample_image_np_array, cv2.IMREAD_COLOR)
        # sample_image = cv2.cvtColor(sample_image, cv2.COLOR_BGR2RGB)
        sample_image = face_recognition.load_image_file("..\\src\\assets\\images\\juan\\edu3.png")
        encode_sample_face = face_recognition.face_encodings(sample_image)[0]
        # Compare faces
        result = face_recognition.compare_faces(face_encodings, encode_sample_face)
        if True in result:
            return jsonify(data = 'True')
        else:
            return jsonify(data = 'False')

    def addEncondingFace(photo,list):
        base_img = face_recognition.load_image_file(photo)
        list.append(face_recognition.face_encodings(base_img)[0])
        return list

    return app
