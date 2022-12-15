#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
import os
import glob

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
    file = request.files['file']
    file.save(os.path.join('./upload_img', file.filename))
    return render_template('index.html')

# アップロードした画像を表示
@app.route('/upload')
def upload():
    return render_template('show_img.html')

@app.route('/gray')
def gray():
    files = glob.glob("./gray_img")
    urls = []
    for file in files:
        urls.append({
            "filename": os.path.basename(file),
            "url": "/processed/gs/" + os.path.basename(file)
        })
    return render_template("show_img.html", target_files=urls)


@app.route('/faceframe')
def faceframe():
    files = glob.glob("./faceframe_img")
    app.logger.info(files)
    urls = []
    for file in files:
        urls.append({
            "filename": os.path.basename(file),
            "url": "/processed/gs/" + os.path.basename(file)
        })
    return render_template("show_img.html", target_files=urls)

  
@app.route('/outline')
def outline():
    files = glob.glob("./outline_img")
    urls = []
    for file in files:
        urls.append({
            "filename": os.path.basename(file),
            "url": "/processed/gs/" + os.path.basename(file)
        })
    return render_template("show_img.html", target_files=urls)


if __name__ == '__main__':
    app.run()