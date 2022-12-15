from flask import Flask, request, render_template
import cv2
import numpy as np
photo = 'upload_img/25390.jpg'

def faceframe(src):

    face_cascade_path = 'site-packages/haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(face_cascade_path)

    photo = cv2.imread(src)
    src_gray = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(src_gray)

    for x, y, w, h in faces:
        cv2.rectangle(photo, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
    cv2.imwrite('result_img/faceframe_img/253902.jpg', photo)

def grayscale(src): 
    # 画像読み込みとグレースケール
    gray_img = cv2.imread(src,cv2.IMREAD_GRAYSCALE)


    # 画像保存
    cv2.imwrite('result_img/gray_img/gray.jpg',gray_img)

def outline(src):
    # グレースケール変換
    gray = cv2.imread(src,cv2.IMREAD_GRAYSCALE)

    # Cannyフィルター
    dst = cv2.Canny(gray, 100, 200)

    # 結果を出力
    cv2.imwrite('result_img/outline_img/doraemon_filter.png', dst)
    
faceframe(photo)
grayscale(photo)
outline(photo)








app = Flask(__name__)

#ホーム画面
@app.route('/', methods=["GET"])
def home_get():
    return render_template('index.html')
  
# 画像をアップロードするとき
@app.route('/', methods=["POST"])
def home_post():
    return render_template('index.html')

# アップロードした画像を表示
@app.route('/upload')
def upload():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()