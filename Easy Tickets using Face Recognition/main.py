from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import cv2

app = Flask(__name__, template_folder='video capture')


@app.route('/')
def login():
    return render_template('main.html')


@app.route('/su')
def su():
    return render_template('signup.html')


@app.route('/sign', methods=['POST', 'GET'])
def details():
    if request.method == 'POST':
        name = request.form['name'].lower()
        email = request.form['email'].lower()
        phone = request.form['phone']
        address = request.form['address'].lower()
        password = request.form['password']
        bal = 500
        import cv2

        import numpy as np
        conn = sqlite3.connect('./FaceBase.db')
        cur = conn.cursor()
        cur.execute("select id from users")
        row = cur.fetchall()
        if not row:
            id = 1
        else:
            id = list(row[-1])[-1] + 1
        print(id)

        conn.execute('Insert into users(id, name, email, phone, balance, address, password) values(?,?,?,?,?,?,?)',
                     (id, name, email, phone, bal, address, password))
        conn.commit()
        conn.close()

        faceDetect = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
        cam = cv2.VideoCapture(0)

        # name=input('Enter the name:')
        # insertOrUpdate(id,name)
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = faceDetect.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                sampleNum += 1
                cv2.imwrite('./dataset/User.' + str(id) + '.' + str(sampleNum) + '.jpg', gray[y:y + h, x:x + w])
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.waitKey(100)
            cv2.imshow('Face', img)
            cv2.waitKey(1)
            if (sampleNum > 50):
                break
        cam.release()
        cv2.destroyAllWindows()
        import os
        import cv2
        import numpy as np
        from PIL import Image

        recogniser = cv2.face.LBPHFaceRecognizer_create()
        path = './dataset'

        def getImagesWithID(path):
            imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
            faces = []
            IDs = []
            for imagePath in imagePaths:
                faceImg = Image.open(imagePath).convert('L')
                faceNp = np.array(faceImg, 'uint8')
                ID = int(os.path.split(imagePath)[-1].split('.')[1])
                faces.append(faceNp)
                IDs.append(ID)
                cv2.imshow("training", faceNp)
                cv2.waitKey(10)
            return IDs, faces

        Ids, faces = getImagesWithID(path)
        recogniser.train(faces, np.array(Ids))
        recogniser.save('./recogniser/trainingData.yml')
        cv2.destroyAllWindows()
        return redirect(url_for('login'))


@app.route('/image')
def login_face():
    faceDetect = cv2.CascadeClassifier(
        './haarcascade_frontalface_default.xml')

    rec = cv2.face.LBPHFaceRecognizer_create()
    rec.read(
        './recogniser/trainingData.yml')
    import time
    time.sleep(5)
    img = cv2.imread('./login/input.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)
    print(faces)
    x, y, w, h = faces[0]
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
    id, conf = rec.predict(gray[y:y + h, x:x + w])
    cv2.putText(img, str(id), (x, x), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    conn = sqlite3.connect('./FaceBase.db')
    cur = conn.cursor()
    import os
    os.remove('./login/input.png')
    cur.execute('select * from users where id=?', (str(id),))
    row = cur.fetchall()
    curh = conn.cursor()
    curh.execute('select * from history where id=?', (str(id),))
    record = curh.fetchall()
    if row:
        name = row[0][1]
        print(row[0])
        return render_template('profile.html', result=[row[0], record])
    else:
        account = 0
        # return redirect(url_for('open'))
        return render_template('login.html', result=account)


@app.route('/login', methods=['POST', 'GET'])
def login_get():
    if request.method == 'POST':
        name = request.form['email'].lower()
        passw = request.form['password']
        conn = sqlite3.connect('./FaceBase.db')
        cur = conn.cursor()
        cur.execute('select * from users where email=? and password=?', (name, passw))
        row = cur.fetchall()

        if not row:
            # print('nahi hai')
            account = 0
            # return redirect(url_for('open'))
            return render_template('main.html', result=account)
        else:
            user = row[0][1]
            id = row[0][0]
            curh = conn.cursor()
            curh.execute('select * from history where id=?', (str(id),))
            record = curh.fetchall()
            return render_template('profile.html', result=[row[0], record])


if __name__ == '__main__':
    app.run()
