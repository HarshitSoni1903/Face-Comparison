import face_recognition
import cv2
import os

class know:
    def function(self):

        path1 = "E:/Project/known_people/"

        knownpics = []
        knownpic_face_encoding = []

        for filename in os.listdir(path1):
            if filename.endswith(".jpg"):
                knownpics.append(path1 + filename)

        for knownpic in knownpics:
            pic = face_recognition.load_image_file(knownpic)
            knownpic_face_encoding.append(face_recognition.face_encodings(pic)[0])

        return knownpics,knownpic_face_encoding
if __name__=="__main__":
    ob = know()
    ob.function()