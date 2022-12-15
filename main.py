#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
import os
import glob

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