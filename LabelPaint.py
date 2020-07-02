from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Rect:

    def __init__(self):
        self.start = QPoint()
        self.end = QPoint()

    def setStart(self, s):
        self.start = s

    def setEnd(self, e):
        self.end = e

    def startPoint(self):
        return self.start

    def endPoint(self):
        return self.end

    def paint(self, painter):
        painter.drawRect(self.startPoint().x(), self.startPoint().y(), self.endPoint().x() - self.startPoint().x(),
                         self.endPoint().y() - self.startPoint().y())


class PaintLabel(QLabel):

    def __init__(self,centralwidget):
        super().__init__(centralwidget)
        self.perm = False  # 描述在不在画
        self.shape = None  # 储存画的矩形对象
        self.rectList = None  # 矩形对象列表
        self.SAstatue= False #是否开启矩形绘制
        self.PicStatus=True#是否开启图像绘制
        self.painter = QPainter(self)
        self.pix=None#要绘制的图片


    def mouseMoveEvent(self, event):
        if self.SAstatue:
            globalPos = self.mapToGlobal(event.pos())

            #text = """鼠标的位置为: 窗口坐标为: Qpoint({0},{1}),屏幕坐标为：屏幕坐标为：QPoint({2},{3})""".format(
                #event.pos().x(), event.pos().y(), globalPos.x(), globalPos.y())
            #self.statusBar().showMessage(text)
            """self.Rectangle_list[0]= event.pos().x()-100
            self.Rectangle_list[1] = event.pos().y() - 100
            self.Rectangle_list[2] = event.pos().x() + 100
            self.Rectangle_list[3] = event.pos().y() + 100"""
            #pos = event.pos()  # 得到鼠标位置
            #window = self.window()  # 得到窗口对象
            #if window is not None:
                #window.labelCoordinates.setText('X: %d; Y: %d' % (pos.x(), pos.y()))  # 设置窗口状态栏信息
            if event.buttons() & Qt.LeftButton:
                if self.shape is not None and not self.perm :
                    self.shape.setEnd(event.pos())
                    self.update()


    def mousePressEvent(self, ev):
        if ev.button() == Qt.LeftButton & self.SAstatue:
            self.shape = Rect()
            if (self.shape is not None):
                self.perm = False
                self.rectList=self.shape
                self.shape.setStart(ev.pos())
                self.shape.setEnd(ev.pos())
            self.update()


    def mouseReleaseEvent(self, ev):
        if ev.button() == Qt.LeftButton & self.SAstatue:
            self.perm = True
            self.shape = None
            #self.update()

    def paintEvent(self, ev):
        QLabel.paintEvent(self, ev)
        if self.SAstatue:
            p = self.painter
            p.begin(self)
            p.setPen(QColor("red"))
            #brush = QBrush(Qt.BDiagPattern)
            #p.setBrush(brush)
            #for shape in self.rectList:
            if self.rectList is not None:
                self.rectList.paint(p)
            p.end()



