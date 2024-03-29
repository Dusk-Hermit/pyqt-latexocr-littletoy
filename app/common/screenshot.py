import sys
# import keyboard
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import Qt, qAbs, QRect,QMimeData
from PyQt6.QtGui import QPen, QPainter, QColor, QGuiApplication

import io
from PIL import Image,ImageQt,ImageGrab

# https://blog.csdn.net/weixin_47440418/article/details/108837426

class CaptureScreen(QWidget):
    # 初始化变量
    beginPosition = None
    endPosition = None
    fullScreenImage = None
    captureImage = None
    isMousePressLeft = None
    painter = QPainter()

    def __init__(self,parent=None):
        super(QWidget, self).__init__(parent)
        self.initWindow()   # 初始化窗口
        self.captureFullScreen()    # 获取全屏

    def initWindow(self):
        self.setMouseTracking(True)     # 鼠标追踪
        self.setCursor(Qt.CursorShape.CrossCursor)  # 设置光标
        self.setWindowTitle('Screenshot')
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)  # 窗口无边框
        self.setWindowState(Qt.WindowState.WindowFullScreen)    # 窗口全屏

    def captureFullScreen(self):
        self.fullScreenImage = QGuiApplication.primaryScreen().grabWindow()


    def mousePressEvent(self, event):        
        if event.button() == Qt.MouseButton.LeftButton:
            self.beginPosition = event.pos()
            self.isMousePressLeft = True
        if event.button() == Qt.MouseButton.RightButton:
            self.close()
            
        #     # 如果选取了图片,则按一次右键开始重新截图
        #     if self.captureImage is not None:
        #         self.captureImage = None
        #         self.paintBackgroundImage()
        #         self.update()
        #     else:
        #         self.close()

    def mouseMoveEvent(self, event):
        if self.isMousePressLeft is True:
            self.endPosition = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        self.endPosition = event.pos()
        self.isMousePressLeft = False
        
        if self.captureImage is not None:
            self.saveImage()
            self.close()

    # def mouseDoubleClickEvent(self, event):
    #     if self.captureImage is not None:
    #         self.saveImage()
    #         self.close()

    # def keyPressEvent(self, event):
    #     if event.key() == Qt.Key_Escape:
    #         self.close()
    #     if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
    #         if self.captureImage is not None:
    #             self.saveImage()
    #             self.close()

    def paintBackgroundImage(self):
        shadowColor = QColor(0, 0, 0, 100)  # 黑色半透明
        self.painter.drawPixmap(0, 0, self.fullScreenImage)
        self.painter.fillRect(self.fullScreenImage.rect(), shadowColor)     # 填充矩形阴影

    def paintEvent(self, event):
        self.painter.begin(self)    # 开始重绘
        self.paintBackgroundImage()
        penColor = QColor(30, 144, 245)     # 画笔颜色
        self.painter.setPen(QPen(penColor, 1, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap))    # 设置画笔,蓝色,1px大小,实线,圆形笔帽
        if self.isMousePressLeft is True:
            pickRect = self.getRectangle(self.beginPosition, self.endPosition)   # 获得要截图的矩形框
            self.captureImage = self.fullScreenImage.copy(pickRect)         # 捕获截图矩形框内的图片
            self.painter.drawPixmap(pickRect.topLeft(), self.captureImage)  # 填充截图的图片
            self.painter.drawRect(pickRect)     # 画矩形边框
        self.painter.end()  # 结束重绘

    def getRectangle(self, beginPoint, endPoint):
        pickRectWidth = int(qAbs(beginPoint.x() - endPoint.x()))
        pickRectHeight = int(qAbs(beginPoint.y() - endPoint.y()))
        pickRectTop = beginPoint.x() if beginPoint.x() < endPoint.x() else endPoint.x()
        pickRectLeft = beginPoint.y() if beginPoint.y() < endPoint.y() else endPoint.y()
        pickRect = QRect(pickRectTop, pickRectLeft, pickRectWidth, pickRectHeight)
        # 避免高度宽度为0时候报错
        if pickRectWidth == 0:
            pickRect.setWidth(2)
        if pickRectHeight == 0:
            pickRect.setHeight(2)

        return pickRect

    def saveImage(self):
        # 保存到剪贴板
        
        # buffer=io.BytesIO()
        # image=ImageQt.fromqpixmap(self.captureImage)
        # image.save(buffer,format='png')
        # buffer.seek(0)
        # image_data=buffer.read()
        
        # mime_data = QMimeData()
        # mime_data.setData("image/png", image_data)
        
        # QApplication.clipboard().setMimeData(mime_data)
        
        
        QGuiApplication.clipboard().setPixmap(self.captureImage)
        # img = ImageGrab.grabclipboard()
        # print(type(img))
        

if __name__ == "__main__":
    # keyboard.wait(hotkey='f4')  # 按F4开始截图
    app = QApplication(sys.argv)
    windows = CaptureScreen()
    windows.show()
    sys.exit(app.exec())
