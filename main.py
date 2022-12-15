#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
import os

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
    return render_template('index.html')


if __name__ == '__main__':
    app.run()