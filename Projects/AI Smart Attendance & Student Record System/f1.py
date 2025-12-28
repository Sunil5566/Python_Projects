import numpy as np
import pandas as pd
import cv2
import os

FILE = "student.csv"
n = int(input("How many students do you want to register: "))

if not os.path.exists(FILE):
    df = pd.DataFrame(columns=["id","name"])
    df.to_csv(FILE,index=False)

for i in range(n):
    sid = input("Enter Student ID: ")
    name = input("Enter Student Name: ")

    new_data = pd.DataFrame([[sid,name]], columns=["id","name"])
    new_data.to_csv(FILE,mode="a",header=False,index=False) 
print("\nAll student data recorded successfully")

# ---------- FACE IMAGE CAPTURE ----------
face_cascade = cv2.CascadeClassifier(r"haarcascade_frontalface_default.xml")
camera = cv2.VideoCapture(0)

Folder_Name = f"dataset/{sid}_{name}"

if not os.path.exists(Folder_Name):
    os.makedirs(Folder_Name)

count = 0

while count < 20:
    ret, frame = camera.read()
    if not ret:
        continue

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        count += 1
        face_img = gray[y:y+h, x:x+w]
        file_path = f"{Folder_Name}/{count}.jpg"
        cv2.imwrite(file_path, face_img)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("Capture face", frame)
    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()
