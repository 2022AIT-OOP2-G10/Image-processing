# Image-processing
Webインターフェースを持つ画像処理システム

## 1.作業分担
| 名前  | 作業名 |
| ------------- | ------------- |
|西|リーダー|
|村松|Webアプリケーション|
|岡本|Webアプリケーション|
|近藤|グレースケール|
|今井|輪郭|
|染木|顔に枠|
## 2.システムの動作確認方法
各自ブランチを作成を作成して頻繁にプッシュをするある程度形になったら動作確認をした後Pull Requestをする。
リーダーはプログラムをチェックしてからマージをしてmainブランチを動作確認をする。

## 3.動作仕様
ファイル構造はこうします。
<pre>
 ―┬― README.md
　├― main.py
　├― upload_img 
　｜　　　　 └― ここに画像アップロード
　└― result_img 
           ├―gray_img
           |      └― ここに画像アップロード
           ├―outline_img
           |       └― ここに画像アップロード
           └―frame_img
                   └― ここに画像アップロード
</pre>
