#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, send_from_directory
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
    
# faceframe(photo)
# grayscale(photo)
# outline(photo)









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

# アップロードした画像を一覧表示
@app.route('/upload')
def upload():
    # upload_img直下のファイルを全て取得する
    files = glob.glob("upload_img/*")
    # 画像ファイルへのパス
    urls = []
    for file in files:
        urls.append({
            "filename": os.path.basename(file),
            "url": "/upload/" + os.path.basename(file)
        })
    return render_template("show_img.html", target_files=urls)

# 画像を表示
@app.route('/upload/<path:filename>')
def upload_show(filename):
    return send_from_directory('./upload_img', filename)

# グレースケール画像を一覧表示
@app.route('/gray')
def gray():
    files = glob.glob("result_img/gray_img/*")
    urls = []
    for file in files:
        urls.append({
            "filename": os.path.basename(file),
            "url": "/gray/" + os.path.basename(file)
        })
    return render_template("show_img.html", target_files=urls)

# 画像を表示
@app.route('/gray/<path:filename>')
def gray_show(filename):
    return send_from_directory('./result_img/gray_img', filename)

# 顔枠画像を一覧表示
@app.route('/faceframe')
def faceframe():
    files = glob.glob("./result_img/faceframe_img/*")
    app.logger.info(files)
    urls = []
    for file in files:
        urls.append({
            "filename": os.path.basename(file),
            "url": "/faceframe/" + os.path.basename(file)
        })
    return render_template("show_img.html", target_files=urls)

# 画像を表示
@app.route('/faceframe/<path:filename>')
def faceframe_show(filename):
    return send_from_directory('./result_img/faceframe_img', filename)

# アウトライン画像を一覧表示
@app.route('/outline')
def outline():
    files = glob.glob("./result_img/outline_img/*")
    urls = []
    for file in files:
        urls.append({
            "filename": os.path.basename(file),
            "url": "/outline/" + os.path.basename(file)
        })
    return render_template("show_img.html", target_files=urls)

# 画像を表示
@app.route('/outline/<path:filename>')
def outline_show(filename):
    return send_from_directory('./result_img/outline_img', filename)

if __name__ == '__main__':
    app.run(debug=True)