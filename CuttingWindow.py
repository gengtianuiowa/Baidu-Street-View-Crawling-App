# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CuttingWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(628, 545)
        self.SelectArea = QtWidgets.QPushButton(Form)
        self.SelectArea.setGeometry(QtCore.QRect(550, 230, 75, 23))
        self.SelectArea.setObjectName("SelectArea")
        self.InputImg = QtWidgets.QPushButton(Form)
        self.InputImg.setGeometry(QtCore.QRect(550, 30, 75, 23))
        self.InputImg.setObjectName("InputImg")
        self.ImgLb = PaintLabel(Form)
        self.ImgLb.setGeometry(QtCore.QRect(10, 10, 512, 512))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.ImgLb.setFont(font)
        self.ImgLb.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ImgLb.setLineWidth(1)
        self.ImgLb.setMidLineWidth(0)
        self.ImgLb.setText("")
        self.ImgLb.setObjectName("ImgLb")
        self.LastImg = QtWidgets.QPushButton(Form)
        self.LastImg.setGeometry(QtCore.QRect(550, 110, 75, 23))
        self.LastImg.setObjectName("LastImg")
        self.NextImg = QtWidgets.QPushButton(Form)
        self.NextImg.setGeometry(QtCore.QRect(550, 140, 75, 23))
        self.NextImg.setObjectName("NextImg")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(560, 60, 61, 21))
        self.label.setObjectName("label")
        self.ImgNum = QtWidgets.QLabel(Form)
        self.ImgNum.setGeometry(QtCore.QRect(570, 80, 61, 21))
        self.ImgNum.setObjectName("ImgNum")
        self.CuttingImg = QtWidgets.QPushButton(Form)
        self.CuttingImg.setGeometry(QtCore.QRect(550, 260, 75, 23))
        self.CuttingImg.setObjectName("CuttingImg")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "图像处理窗口"))
        self.SelectArea.setText(_translate("Form", "选择区域"))
        self.InputImg.setText(_translate("Form", "导入图片"))
        self.LastImg.setText(_translate("Form", "上一张"))
        self.NextImg.setText(_translate("Form", "下一张"))
        self.label.setText(_translate("Form", "当前图片："))
        self.ImgNum.setText(_translate("Form", "第0张"))
        self.CuttingImg.setText(_translate("Form", "裁切并保存"))

from LabelPaint import PaintLabel
