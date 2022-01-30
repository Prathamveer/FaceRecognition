from PIL import Image
import face_recoginition

given_image = face_recognition.load_image_file("queen.jpeg")
encoding = face_recognition.face_encodings(given_image)[0]

unknown_image = face_recognition.load_image_file("freddie.jpeg")

face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recogintion.face_encodings(unknown_image, face_locations)