# Image-processing
Webインターフェースを持つ画像処理システム

## 1.作業分担



## 2.システムの動作確認方法
各自ブランチを作成を作成して頻繁にプッシュをするある程度形になったら動作確認をした後Pull Requestをする。
リーダーはプログラムをチェックしてからマージをしてmainブランチを動作確認をする。

## 3.動作仕様
ファイル構造はこうする。
 ―┬― README.md
　├― main.py
　├― upload_img 
　｜　　　　 └― ここに画像アップロード
　└― result_img 
           ├―gray_img
           |      └― ここに画像アップロード
           ├―outline_img
                  └― ここに画像アップロード
           └―