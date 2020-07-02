import sys
from ImgOperatePg import CuttingWindow
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import os

class Cutting(QMainWindow, CuttingWindow.Ui_Form):
    Rectangle_list = [0, 0, 0, 0]


    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setMouseTracking(True)
        self.SelectArea.clicked.connect(self.SelectAreaClicked)
        self.InputImg.clicked.connect(self.InputImgClicked)
        self.LastImg.clicked.connect(self.LastImgClicked)
        self.NextImg.clicked.connect(self.NextImgClicked)
        self.CuttingImg.clicked.connect(self.CuttingImgClicked)
        self.SAstatue=False#现在是否开启图片选框
        self.ImgCount=0#图片总数
        self.ImgDisplay=-1#现在展示的图片编号
        self.ImgList=[]#所有图片组成的列表
        self.Lbpix=None#现在显示的pix图片
        self.ImgLb.setStyleSheet('border-width: 1px;border-style: solid;')

    def SelectAreaClicked(self):
        if self.SAstatue:
            self.SAstatue=False
            self.ImgLb.SAstatue = False
            self.rectList = None
            #QApplication.processEvents()
            self.update()
        else:
            self.SAstatue = True
            self.ImgLb.SAstatue = True

    def InputImgClicked(self):
        self.ImgList,tp = QFileDialog.getOpenFileNames(self, '打开', r"E:\geography color\picture data", 'jpg(*.jpg)')
        print(self.ImgList)
        self.ImgCount=len(self.ImgList)
        if self.ImgCount<=0:
            self.statusBar().showMessage("图片打开失败")
        else:
            self.ImgDisplay=0
            print(os.path.basename(os.path.realpath(self.ImgList[self.ImgDisplay])))
            self.Lbpix = pix = QPixmap(self.ImgList[self.ImgDisplay])
            self.ImgLb.setPixmap(pix)
            self.ImgLb.resize(pix.width(), pix.height())
            text = "第" + str(self.ImgDisplay + 1) + "张"
            self.statusBar().showMessage("图" + str(1) + "加载成功")
            self.ImgNum.setText(text)

    def LastImgClicked(self):
        if self.ImgList is None:
            self.statusBar().showMessage("未加载图片，请先加载图片")
        elif self.ImgDisplay - 1 < 0:
            self.statusBar().showMessage("已是第一张图片")
        else :
            self.ImgDisplay -= 1
            self.statusBar().showMessage("图" + str(self.ImgDisplay) + "加载成功")
            self.Lbpix = pix = QPixmap(self.ImgList[self.ImgDisplay])
            self.ImgLb.setPixmap(pix)
            self.ImgLb.resize(pix.width(), pix.height())
            text="第"+str(self.ImgDisplay+1)+"张"
            self.ImgNum.setText(text)

    def NextImgClicked(self):
        if self.ImgList is None:
            self.statusBar().showMessage("未加载图片，请先加载图片")
        elif self.ImgDisplay+1>self.ImgCount-1:
            self.statusBar().showMessage("已是最后一张图片")
        else:
            self.ImgDisplay += 1
            self.statusBar().showMessage("图" + str(self.ImgDisplay)+"加载成功")
            self.Lbpix = pix = QPixmap(self.ImgList[self.ImgDisplay])
            self.ImgLb.setPixmap(pix)
            self.ImgLb.resize(pix.width(), pix.height())
            text = "第" + str(self.ImgDisplay + 1) + "张"
            self.ImgNum.setText(text)

    def CuttingImgClicked(self):
        if self.ImgList is None:
            self.statusBar().showMessage("图片列表为空。请先导入图片")
        elif self.ImgLb.rectList is None:
            self.statusBar().showMessage("还未选取剪切区域。请先选取区域")
        else:
            cuttingrect=self.ImgLb.rectList
            rect = QRect(cuttingrect.start,cuttingrect.end)
            new_pixmap = self.Lbpix.copy(rect)
            pathsplit=self.ImgList[self.ImgDisplay].split('/')
            fin_path=r'E:\geography color\picture data\CutResult' + '\\' +pathsplit[len(pathsplit) - 2] + '_' + str(os.path.basename(os.path.realpath(self.ImgList[self.ImgDisplay])))
            print(fin_path)
            new_pixmap.save(fin_path)
            print(pathsplit[len(pathsplit)-2])
            self.ImgLb.setPixmap(new_pixmap)
            self.ImgLb.setAlignment(Qt.AlignCenter)
            self.statusBar().showMessage("裁切成功，结果已保存至E:\\geography color\\picture data\\CutResult目录下")




def showCutting() -> object:
    app = QApplication(sys.argv)
    cutting=Cutting()
    cutting.show()
    sys.exit(app.exec_())
