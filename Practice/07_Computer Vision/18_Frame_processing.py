import tensorflow as tf

# Load pretrained FaceNet model
model = tf.keras.models.load_model("facenet_keras.h5")

def get_embedding(face_img):
    face_img = face_img.astype('float32')
    mean, std = face_img.mean(), face_img.std()
    face_img = (face_img - mean) / std

    sample = tf.expand_dims(face_img, axis=0)
    embedding = model.predict(sample)

    return embedding[0]

import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

def extract_face(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) == 0:
        return None

    x, y, w, h = faces[0]
    face = frame[y:y+h, x:x+w]

    face = cv2.resize(face, (160, 160))
    return face, (x, y, w, h)

import os

known_embeddings = []
known_names = []

dataset_path = "dataset"

for person_name in os.listdir(dataset_path):
    person_folder = os.path.join(dataset_path, person_name)

    for img_name in os.listdir(person_folder):
        img_path = os.path.join(person_folder, img_name)

        img = cv2.imread(img_path)
        face_data = extract_face(img)

        if face_data is not None:
            face, _ = face_data
            embedding = get_embedding(face)

            known_embeddings.append(embedding)
            known_names.append(person_name)

print("Database Ready!")
cap = cv2.VideoCapture(0)

def recognize_face(embedding, threshold=0.6):
    min_dist = float("inf")
    name = "Unknown"

    for i, known_emb in enumerate(known_embeddings):
        dist = np.linalg.norm(known_emb - embedding)

        if dist < min_dist:
            min_dist = dist
            name = known_names[i]

    if min_dist > threshold:
        return "Unknown"

    return name

while True:
    ret, frame = cap.read()
    if not ret:
        break

    face_data = extract_face(frame)

    if face_data is not None:
        face, (x, y, w, h) = face_data
        embedding = get_embedding(face)

        name = recognize_face(embedding)

        # Draw result
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
        cv2.putText(frame, name, (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)

    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()