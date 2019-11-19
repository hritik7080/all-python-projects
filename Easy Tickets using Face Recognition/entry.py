import cv2
import numpy as np
import sqlite3
from datetime import datetime

station = 'jalandhar'
station = station.lower()

faceDetect = cv2.CascadeClassifier(
    './haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)
rec = cv2.face.LBPHFaceRecognizer_create()
rec.read(
    './recogniser/trainingData.yml')
a = set()


def database(id, now):
    conn = sqlite3.connect('./FaceBase.db')
    cur = conn.cursor()
    cur.execute('select * from users where id=?', (str(id)))
    row = cur.fetchall()
    curr = conn.cursor()
    curr.execute('select * from history where id=? order by dep_time desc ', (str(id)))
    data = curr.fetchall()
    date_time=now.strftime("%d/%m/%Y, %H:%M:%S")
    if not data:
        conn.execute('insert into history(id, dep, arr, dep_time) values (?,?,?,?)', (str(id), station, '0', date_time))
        conn.commit()
        return row
    elif data:
        if data[0][2]!='0':
            conn.execute('insert into history(id, dep, arr, dep_time) values (?,?,?,?)', (str(id), station, '0', date_time))
            conn.commit()
            return row
        else:
            return row
    else:
        return row


while (True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        id, conf = rec.predict(gray[y:y + h, x:x + w])
        now=datetime.now()
        print(type(id))
        row = database(id,now)
        if row:
            cv2.putText(img, str(id), (x, x), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

        # print('andar')
    cv2.imshow("Face", img)
    print(a)

    if (cv2.waitKey(1) == ord('q')):
        break
cam.release()
cv2.destroyAllWindows()
