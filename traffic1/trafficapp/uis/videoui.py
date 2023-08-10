# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'video.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Video(object):
    def setupUi(self, Video):
        Video.setObjectName("Video")
        Video.resize(900, 600)
        self.lbl_video = QtWidgets.QLabel(Video)
        self.lbl_video.setGeometry(QtCore.QRect(0, 0, 900, 600))
        self.lbl_video.setFrameShape(QtWidgets.QFrame.Panel)
        self.lbl_video.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lbl_video.setLineWidth(2)
        self.lbl_video.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_video.setObjectName("lbl_video")

        self.retranslateUi(Video)
        QtCore.QMetaObject.connectSlotsByName(Video)

    def retranslateUi(self, Video):
        _translate = QtCore.QCoreApplication.translate
        Video.setWindowTitle(_translate("Video", "主视频界面"))
        self.lbl_video.setText(_translate("Video", "主监控视频"))
