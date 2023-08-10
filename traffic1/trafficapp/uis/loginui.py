# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(480, 360)
        Login.setModal(True)
        self.lbl_video = QtWidgets.QLabel(Login)
        self.lbl_video.setGeometry(QtCore.QRect(0, 0, 480, 360))
        self.lbl_video.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lbl_video.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lbl_video.setLineWidth(3)
        self.lbl_video.setMidLineWidth(2)
        self.lbl_video.setTextFormat(QtCore.Qt.RichText)
        self.lbl_video.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_video.setObjectName("lbl_video")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "人脸登录"))
        self.lbl_video.setText(_translate("Login", "登录人脸视频区"))
