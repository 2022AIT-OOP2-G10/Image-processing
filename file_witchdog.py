from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer
import os
import time

import cv2  #

if __name__ == "__main__":

    # 対象ディレクトリ
    DIR_WATCH = './result_img/faceframe_img'
    # 対象ファイル名のパターン
    PATTERNS = ['*.jpg']

    def on_modified(event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        print('%s changed' % filename)


    # event_handler = LoggingEventHandler()
    event_handler = PatternMatchingEventHandler(PATTERNS)
    event_handler.on_modified = on_modified



    observer = Observer()
    observer.schedule(event_handler, DIR_WATCH, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()