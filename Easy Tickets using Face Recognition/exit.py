import cv2
import numpy as np
import sqlite3
from datetime import datetime

station = 'phagwara'
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

    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
    if not data:
        # conn.execute('insert into history(id, dep, dep_time) values (?,?,?)', (str(id), station, date_time))
        # conn.commit()
        return row
    elif data:
        # print(data[0][2])
        if data[0][2] == '0':
            print('aya')
            curf = conn.cursor()
            curf.execute('select fair from fiars where dep=? and arr=?', ('jalandhar', 'phagwara'))
            fair = curf.fetchall()
            print(fair[0][0])
            conn.execute('UPDATE history SET arr =?, arr_time =?, fair=? WHERE id=? and arr=? ',
                         (station, date_time, int(fair[0][0]), str(id), '0'))
            conn.commit()

            bal = row[0][4]
            bal = int(bal) - int(fair[0][0])
            import requests
            import json

            URL = 'https://www.way2sms.com/api/v1/sendCampaign'

            # get request
            def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
                req_params = {
                    'apikey': '1WMXTV1QA38SFH7BQ1VAEG39YPW3LT7X',
                    'secret': '7RWX5BP2YZ6TLONE',
                    'usetype': 'stage',
                    'phone': row[0][3],
                    'message': f'Amount Rs.{fair[0][0]} has been dedeucted from your account for your journey. Your current balance is Rs.{bal} .',
                    'senderid': 'hritikgupta7080@gmail.com'
                }
                return requests.post(reqUrl, req_params)

            # get response
            response = sendPostRequest(URL, 'provided-api-key', 'provided-secret', 'prod/stage', 'valid-to-mobile',
                                       'active-sender-id', 'message-text')
            """
              Note:-
                you must provide apikey, secretkey, usetype, mobile, senderid and message values
                and then requst to api
            """
            # print response if you wan
            conn.execute('update users set balance=? where id=?', (bal, row[0][0]))
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
        now = datetime.now()
        row = database(id, now)
        if row:
            cv2.putText(img, str(id), (x, x), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

        # print('andar')
    cv2.imshow("Face", img)

    if (cv2.waitKey(1) == ord('q')):
        break
cam.release()
cv2.destroyAllWindows()
