from PyQt5.QtWidgets import QDialog
from trafficapp.uis.trafficui import Ui_Traffic
from trafficapp.uis.trafficdev import WTrafficDev
from PyQt5.QtGui import QImage, QPixmap, QStandardItem, QStandardItemModel
from trafficapp.uis.trafficvideoframe import WTrafficVideoDialog
from PyQt5.QtCore import QUrl
from trafficapp.biz.map import GetMapUrl
from PyQt5.QtCore import pyqtSignal
import time

class WTrafficDialog(QDialog):
    signal_handle = pyqtSignal(int)  # int传递图像的处理方式0：原图，1，灰色图。2.高斯模糊（替换成锐化处理）3. 线条处理
    def __init__(self):
        super(WTrafficDialog, self).__init__()
        self.main_id = 1
        self.is_sub_dialog = False
        self.ui = Ui_Traffic()
        self.ui.setupUi(self)
        self.ui.lbl_video_1.clicked.connect(self.switch_video1_main)
        self.ui.lbl_video_2.clicked.connect(self.switch_video2_main)
        self.ui.lbl_video_3.clicked.connect(self.switch_video3_main)
        self.ui.lbl_video_4.clicked.connect(self.switch_video4_main)
        self.ui.lbl_video_5.clicked.connect(self.switch_video5_main)
        self.ui.lbl_video_6.clicked.connect(self.switch_video6_main)
        self.ui.lbl_video_7.clicked.connect(self.switch_video7_main)
        self.ui.lbl_video_main.clicked.connect(self.show_main_video)

        self.init_dev()
    
    def init_dev(self):
        # 初始化表格
        self.list_model = QStandardItemModel()    # 列表框
        self.table_model = QStandardItemModel()   # 表格框

        # 表头
        self.table_model.setHorizontalHeaderItem(0, QStandardItem("x坐标"))
        self.table_model.setHorizontalHeaderItem(1, QStandardItem("y坐标"))
        self.table_model.setHorizontalHeaderItem(2, QStandardItem("宽度"))
        self.table_model.setHorizontalHeaderItem(3, QStandardItem("高度"))
        self.table_model.setHorizontalHeaderItem(4, QStandardItem("概率"))
        self.table_model.setHorizontalHeaderItem(5, QStandardItem("目标名"))
        self.ui.tbv_log.horizontalHeader().setStyleSheet("QHeaderView::section {background-color:#00DDDD;color:#000000;}")
        
        # 绑定组件与数据模式
        self.ui.tbv_log.setModel(self.table_model)
        self.ui.lsv_warning.setModel(self.list_model)
        # 加载地图(还可以优化)
        # map_url =  GetMapUrl()
        # self.ui.wdt_map.load(QUrl(map_url))   
        # 创建线程
        self.th_1 = WTrafficDev(1, 0)
        self.th_2 = WTrafficDev(2, "交通视频.mp4")
        self.th_3 = WTrafficDev(3, "街口1.mp4")
        self.th_4 = WTrafficDev(4, "街口2.mp4")
        self.th_5 = WTrafficDev(5, "街口3.mp4")
        self.th_6 = WTrafficDev(6, "街口4.mp4")
        self.th_7 = WTrafficDev(7, "交通视频.mp4")
        # 绑定图像处理信号到视频抓取模块
        self.signal_handle.connect(self.th_1.recv_handle)
        self.signal_handle.connect(self.th_2.recv_handle)
        self.signal_handle.connect(self.th_3.recv_handle)
        self.signal_handle.connect(self.th_4.recv_handle)
        self.signal_handle.connect(self.th_5.recv_handle)
        self.signal_handle.connect(self.th_6.recv_handle)
        self.signal_handle.connect(self.th_7.recv_handle)
        # 绑定视频槽函数
        self.th_1.sign_video.connect(self.show_video)
        self.th_2.sign_video.connect(self.show_video)
        self.th_3.sign_video.connect(self.show_video)
        self.th_4.sign_video.connect(self.show_video)
        self.th_5.sign_video.connect(self.show_video)
        self.th_6.sign_video.connect(self.show_video)
        self.th_7.sign_video.connect(self.show_video)

        # 绑定列表框与表格框的数据显示函数
        self.th_1.sign_item.connect(self.show_table)
        self.th_1.sign_light.connect(self.show_list)
        self.th_2.sign_item.connect(self.show_table)
        self.th_2.sign_light.connect(self.show_list)
        self.th_3.sign_item.connect(self.show_table)
        self.th_3.sign_light.connect(self.show_list)
        self.th_4.sign_item.connect(self.show_table)
        self.th_4.sign_light.connect(self.show_list)
        self.th_5.sign_item.connect(self.show_table)
        self.th_5.sign_light.connect(self.show_list)
        self.th_6.sign_item.connect(self.show_table)
        self.th_6.sign_light.connect(self.show_list)
        self.th_7.sign_item.connect(self.show_table)
        self.th_7.sign_light.connect(self.show_list)
        # 启动线程
        self.th_1.start()
        self.th_2.start()
        self.th_3.start()
        self.th_4.start()
        self.th_5.start()
        self.th_6.start()
        self.th_7.start()

    def show_list(self, light):
        lt = time.localtime(time.time())
        self.list_model.appendRow(QStandardItem(light + "：" + F"{lt.tm_year}-{lt.tm_mon}-{lt.tm_mday} {lt.tm_hour}:{lt.tm_min}:{lt.tm_sec}")) # 时间 
    
    def show_table(self, x, y, w, h, prob, cls_name):
        # print(x, y, w, h, prob, cls_name)
        self.table_model.appendRow([QStandardItem(F"{x:d}"), QStandardItem(F"{y:d}"), QStandardItem(F"{w:d}"), QStandardItem(F"{h:d}"), QStandardItem(F"{prob:5.4f}"), QStandardItem(cls_name)])
        
    # 其他交互与逻辑处理
    def show_video(self, data, h, w, c, th_id):
        qimg = QImage(data, w, h, w*c, QImage.Format_RGB888)
        qpixmap = QPixmap.fromImage(qimg)
        
        if th_id == 1:
            self.show_video_in_label(self.ui.lbl_video_1,qpixmap)
            if self.main_id == 1:
                self.show_video_in_label(self.ui.lbl_video_main,qpixmap)
                if self.is_sub_dialog:
                    self.show_video_in_label(self.main_video_dlg.ui.lbl_video,qpixmap)

        if th_id == 2:
            self.show_video_in_label(self.ui.lbl_video_2,qpixmap)
            if self.main_id == 2:
                self.show_video_in_label(self.ui.lbl_video_main,qpixmap)
                if self.is_sub_dialog:
                    self.show_video_in_label(self.main_video_dlg.ui.lbl_video,qpixmap)

        if th_id == 3:
            self.show_video_in_label(self.ui.lbl_video_3,qpixmap)
            if self.main_id == 3:
                self.show_video_in_label(self.ui.lbl_video_main,qpixmap)
                if self.is_sub_dialog:
                    self.show_video_in_label(self.main_video_dlg.ui.lbl_video,qpixmap)

        if th_id == 4:
            self.show_video_in_label(self.ui.lbl_video_4,qpixmap)
            if self.main_id == 4:
                self.show_video_in_label(self.ui.lbl_video_main,qpixmap)
                if self.is_sub_dialog:
                    self.show_video_in_label(self.main_video_dlg.ui.lbl_video,qpixmap)
        
        if th_id == 5:
            self.show_video_in_label(self.ui.lbl_video_5,qpixmap)
            if self.main_id == 5:
                self.show_video_in_label(self.ui.lbl_video_main,qpixmap)
                if self.is_sub_dialog:
                    self.show_video_in_label(self.main_video_dlg.ui.lbl_video,qpixmap)

        if th_id == 6:
            self.show_video_in_label(self.ui.lbl_video_6,qpixmap)
            if self.main_id == 6:
                self.show_video_in_label(self.ui.lbl_video_main,qpixmap)
                if self.is_sub_dialog:
                    self.show_video_in_label(self.main_video_dlg.ui.lbl_video,qpixmap)

        if th_id == 7:
            self.show_video_in_label(self.ui.lbl_video_7,qpixmap)
            if self.main_id == 7:
                self.show_video_in_label(self.ui.lbl_video_main,qpixmap)
                if self.is_sub_dialog:
                    self.show_video_in_label(self.main_video_dlg.ui.lbl_video,qpixmap)

    def show_video_in_label(self, component, img):
        component.setPixmap(img)
        component.setScaledContents(True)

    def switch_video1_main(self):
        # 记录点击的标签
        self.main_id = 1
        # 显示视频，做个逻辑判定，并显示在主区
        
    def switch_video2_main(self):
        self.main_id = 2

    def switch_video3_main(self):
        self.main_id = 3

    def switch_video4_main(self):
        self.main_id = 4

    def switch_video5_main(self):
        self.main_id = 5

    def switch_video6_main(self):
        self.main_id = 6

    def switch_video7_main(self):
        self.main_id = 7
    

    def handle_video(self, btn_id):
        """
            实际得图像得处理，从设计结构上讲，都交给视频抓取模块再抓取后处理
             1. 发送一个信号给视频抓取模块（信号指定一个处理方式的参数）
                |- 定义信息
                |- 绑定信号
             2. 视频抓取类定义一个变量存储处理方式，并根据处理方式处理图像
                |- 绑定接受信号
                |- 根据信号的图像处理方式处理图像
                |- （再使用信号发送给窗体显示）
        """
        handle_type = 0
        if btn_id == 100:
            handle_type = 0
        if btn_id == 101:
            handle_type = 1
        if btn_id == 102:
            handle_type = 2
        if btn_id == 103:
            handle_type = 3
        self.signal_handle.emit(handle_type)    
        # print("发送信号：", handle_type)

    def modify_bright(self, val):
        print("调整亮度值：", val)
    
    # 主显示区弹窗显示监控视频
    def show_main_video(self):
        # 1. 创建一个窗体
        self.main_video_dlg = WTrafficVideoDialog(self)  # 非模式对话框
        # 设置一个标记
        self.is_sub_dialog = True
        
        # 2. 进入窗体的消息训练
        # self.main_video_dlg.setModal(False)
        # self.main_video_dlg.show()
        self.main_video_dlg.exec()
        # 3. 释放窗体
        self.is_sub_dialog = False
        self.main_video_dlg.destroy()
        self.main_video_dlg = None
        
    
    def closeEvent(self, e):
        self.th_1.close()
        self.th_2.close()
        self.th_3.close()
        self.th_4.close()
        self.th_5.close()
        self.th_6.close()
        self.th_7.close()
