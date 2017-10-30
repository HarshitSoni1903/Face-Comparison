import face_recognition
import os
from backend import know, getimage
from tkinter import *

def check():

    #get image database encoding

    ob = know.know()
    knownpics,knownpic_face_encoding = ob.function()

    #capture new image

    ob1 = getimage.image()
    ob1.capture()

    filename = "E:/Project/known_people/temp.jpg"

    unknown_picture = face_recognition.load_image_file(filename)
    unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

    # Now we can see the two face encodings are of the same person with `compare_faces`!
    for encoding1 in knownpic_face_encoding:
        results = face_recognition.compare_faces([encoding1], unknown_face_encoding)
        if results[0] == True:
            print("It's a picture of me!")
            #ob=show(knownpics[knownpic_face_encoding.index(encoding1)])
            return knownpics[knownpic_face_encoding.index(encoding1)]
        else:
            print("It's not a picture of me!")
            return "Not Found"

def savenew(name):
    new1 = "E:/Project/known_people/"+name+".jpg"
    os.rename("E:/Project/known_people/temp.jpg",new1)

def replace(rpath):
    os.remove(rpath)
    os.rename("E:/Project/known_people/temp.jpg", rpath)