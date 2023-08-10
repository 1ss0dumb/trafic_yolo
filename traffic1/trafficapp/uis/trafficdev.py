from PyQt5.QtCore import QThread, pyqtSignal
import cv2
import numpy as np
from trafficapp.aicv.imgshandle import toGray, toClear, toBright, toLine
from yolotr.detector import TrafficDetector

class WTrafficDev(QThread):
    sign_video = pyqtSignal(bytes, int, int, int, int)
    sign_item = pyqtSignal(int, int, int, int, float, str)  # 发送侦测的目标日志
    sign_light = pyqtSignal(str)  # 发送红绿灯
    def __init__(self, th_id, dev_id):
        super(WTrafficDev, self).__init__()
        self.dev_id = dev_id
        self.th_id = th_id
        self.dev = cv2.VideoCapture(self.dev_id, cv2.CAP_DSHOW)
        self.dev.open(self.dev_id) #, cv2.CAP_DSHOW)
        self.handle_type = 0

        self.detector = TrafficDetector()

    def recv_handle(self, h_type):
        self.handle_type = h_type
        # print("接受信号：", self.handle_type)
    
    def run(self):
        while True:
            # 视频捕捉
            reval, img = self.dev.read()
            if not reval:
                self.dev.open(self.dev_id)
                continue
            # 处理
            # AI侦测并标注处理
            img, pred = self.detector.detect_mark(img)
            # 显示到UI
            if pred is not None:
                for result in pred:
                    x1, y1, x2, y2 = result[0:4]
                    prob = result[4]
                    clss = int( result[5])
                    cls_name = self.detector.get_name(clss)
                    self.sign_item.emit(x1, y1, x2- x1, y2- y1, prob, cls_name)
                    if clss == 9: # 交通灯
                        self.sign_light.emit("红绿交通灯")

            # 保存数据到数据库 （略）

            # 亮度处理
            # toBright(img, ?)
            # 图像基础处理
            if self.handle_type == 0:
                # 不做任何处理，原始视频图像
                pass

            if self.handle_type == 1:
                # print("处理灰度图像")
                img = toGray(img)

            if self.handle_type == 2:
                # 清晰处理
                img = toClear(img)

            if self.handle_type == 3:
                # 线条处理
                img = toLine(img)

            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            # 发送信号
            data = img.tobytes()
            h, w, c = img.shape
            self.sign_video.emit(data, h, w, c, self.th_id)
            # 暂停，复合人眼的视觉习惯
            QThread.usleep(100000)

    def close(self):
        self.terminate()    
        while self.isRunning():
            pass
        self.dev.release()
