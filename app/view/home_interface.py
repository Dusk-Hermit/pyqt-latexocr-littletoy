from PyQt6.QtCore import Qt, QTimer,QThread,pyqtSignal
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout,QGridLayout,QLabel,QFrame,QApplication
from PyQt6.QtGui import QPixmap,QFont
from qfluentwidgets import  TextEdit,ScrollArea,ImageLabel,FluentIcon,IconWidget,StateToolTip

from ..common.style_sheet import StyleSheet
from ..common.render import render_latex,latex_result_replace

from PIL import ImageGrab,Image,ImageQt
import pyperclip
from pix2tex.cli import LatexOCR
import time
import os
from ..common.screenshot import CaptureScreen
from ..common.check import cmd_exists

class RenderThread(QThread):
    result_ready = pyqtSignal(Image.Image)
    
    def __init__(self,param,parent=None):
        super().__init__(parent=parent)
        self.param=param
    
    def run(self):
        text=self.param['text']
        img=render_latex(text)
        self.result_ready.emit(img)

class OCRThread(QThread):
    result_ready = pyqtSignal(str)
    
    def __init__(self,img,parent=None):
        super().__init__(parent=parent)
        self.img=img
    
    def run(self):
        model=LatexOCR()
        result=model(self.img)
        self.result_ready.emit(result)


class IconCard(QFrame):
    """ Icon card """

    def __init__(self, icon: FluentIcon,text='', parent=None):
        super().__init__(parent=parent)
        self.icon = icon

        self.iconWidget = IconWidget(icon, self)
        self.nameLabel = QLabel(self)
        self.vBoxLayout = QVBoxLayout(self)
        self.setStyleSheet('background-color: rgb(251, 251, 251);border: 1px solid rgb(229, 229, 229);border-radius: 6px;')
        self.nameLabel.setStyleSheet("color: rgb(96, 96, 96);font: 11px 'Segoe UI', 'PingFang SC';border: 0px;")

        self.setFixedSize(84, 84)
        self.vBoxLayout.setSpacing(0)
        self.vBoxLayout.setContentsMargins(8, 24, 8, 0)
        self.vBoxLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.iconWidget.setFixedSize(24, 24)
        self.vBoxLayout.addWidget(self.iconWidget, 0, Qt.AlignmentFlag.AlignHCenter)
        self.vBoxLayout.addSpacing(14)
        self.vBoxLayout.addWidget(self.nameLabel, 0, Qt.AlignmentFlag.AlignHCenter)

        self.nameLabel.setText(text)
        
        
        self.setCursor(Qt.CursorShape.PointingHandCursor)


def scale_qpixmap(img:QPixmap):
    """缩放图片"""
    return img.scaled(340, 250, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)


    
class HomeInterface(ScrollArea):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.initUI()
        
        self.clipboard=QApplication.clipboard()
        self.tooltip_queue=[]
        self.loadModel()

    def loadModel(self):
        # start_time=time.time()
        # self.set_tip('模型加载中','模型加载中，请稍等')
        self.ocr=LatexOCR()
        # end_time=time.time()
        # self.set_tip('模型加载成功',f'模型加载成功，耗时{end_time-start_time:.2f}秒')
        
        
    def initUI(self):
        
        StyleSheet.HOME_INTERFACE.apply(self)
        
        
        # 顶级布局
        self.view = QWidget(self)        
        self.hBoxLayout = QHBoxLayout(self.view)
        
        self.view.setObjectName('view')
        self.setObjectName('homeInterface')
        
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setWidget(self.view)
        self.setWidgetResizable(True)
        
        self.hBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.hBoxLayout.setSpacing(25)
        self.hBoxLayout.setAlignment(Qt.AlignmentFlag.AlignJustify )
        
        # 分栏布局
        self.view1 = QWidget(self.view)
        self.view2 = QWidget(self.view)
        self.view3 = QWidget(self.view)
        
        self.vBoxLayout1 = QGridLayout(self.view1)
        self.vBoxLayout2 = QGridLayout(self.view2)
        self.vBoxLayout3 = QGridLayout(self.view3)
        
        self.vBoxLayout1.setContentsMargins(10, 10, 10, 10)
        self.vBoxLayout2.setContentsMargins(10, 10, 10, 10)
        self.vBoxLayout3.setContentsMargins(10, 10, 10, 10)
        self.vBoxLayout1.setSpacing(10)
        self.vBoxLayout2.setSpacing(10)
        self.vBoxLayout3.setSpacing(10)
        self.vBoxLayout1.setAlignment(Qt.AlignmentFlag.AlignCenter )
        self.vBoxLayout2.setAlignment(Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignHCenter)
        self.vBoxLayout3.setAlignment(Qt.AlignmentFlag.AlignCenter )

        self.hBoxLayout.addWidget(self.view1)
        self.hBoxLayout.addWidget(self.view2)
        self.hBoxLayout.addWidget(self.view3)
        
        self.view1.setFixedSize(360,600)
        self.view2.setFixedSize(100,600)
        self.view3.setFixedSize(360,600)
        
        # 控件
        ## 第一栏
        self.imagelabel1 = ImageLabel(self.view1)
        self.imagelabel2 = ImageLabel(self.view2)
        
        self.img1=None
        self.img2=None
        self.imagelabel1.setPixmap(scale_qpixmap(QPixmap(':/resource/3.jpg')))
        self.imagelabel2.setPixmap(scale_qpixmap(QPixmap(':/resource/2.jpg')))

        self.w1=ScrollArea(self.view1)
        self.w2=ScrollArea(self.view1)
        
        self.w1.setWidget(self.imagelabel1)
        self.w2.setWidget(self.imagelabel2)
        self.w1.horizontalScrollBar().setValue(0)
        self.w2.horizontalScrollBar().setValue(0)
        self.w1.setFixedHeight(250)
        self.w2.setFixedHeight(250)
        self.w1.setAlignment(Qt.AlignmentFlag.AlignCenter )
        self.w2.setAlignment(Qt.AlignmentFlag.AlignCenter )
        
        self.vBoxLayout1.addWidget(self.w1,0,0)
        self.vBoxLayout1.addWidget(self.w2,1,0)
        
        ## 第二栏
        self.iconcard1 = IconCard(FluentIcon.DOCUMENT,'Clipboard',self.view2)
        self.iconcard2 = IconCard(FluentIcon.RIGHT_ARROW,'OCR',self.view2)
        self.iconcard3 = IconCard(FluentIcon.LEFT_ARROW,'Render',self.view2)
        self.iconcard4 = IconCard(FluentIcon.FIT_PAGE,'Screenshot',self.view2)
        self.iconcard5= IconCard(FluentIcon.DOWNLOAD,'Save',self.view2)
        self.iconcard6 = IconCard(FluentIcon.COPY,'Copy',self.view2)
        
        self.vBoxLayout2.addWidget(self.iconcard4,0,0)
        self.vBoxLayout2.addWidget(self.iconcard1,1,0)
        self.vBoxLayout2.addWidget(self.iconcard2,2,0)
        self.vBoxLayout2.addWidget(self.iconcard3,3,0)
        self.vBoxLayout2.addWidget(self.iconcard5,4,0)
        self.vBoxLayout2.addWidget(self.iconcard6,5,0)
        
        self.iconcard1.mouseReleaseEvent = self.get_img_from_clipboard
        self.iconcard2.mouseReleaseEvent = self.ocr_exec
        self.iconcard3.mouseReleaseEvent = self.render_latex
        self.iconcard4.mouseReleaseEvent = self.exec_screenshot
        self.iconcard5.mouseReleaseEvent = self.save_rendered_image
        self.iconcard6.mouseReleaseEvent = lambda e:pyperclip.copy(self.textEdit2.toPlainText())
        
        ## 第三栏
        self.textEdit1 = TextEdit(self.view3)
        self.textEdit2 = TextEdit(self.view3)
        self.textEdit1.setFont(QFont('Source Code Pro', 16))
        self.textEdit2.setFont(QFont('Source Code Pro', 14))
        
        self.textEdit1.setFixedSize(300,250)
        self.textEdit2.setFixedSize(300,250)
        
        self.textEdit1.setReadOnly(True)
        
        self.vBoxLayout3.addWidget(self.textEdit1,0,0)
        self.vBoxLayout3.addWidget(self.textEdit2,1,0)
    
    def set_tip(self,str1,str2):
        tooltip=StateToolTip(str1,str2,self.window())
        tooltip.move(tooltip.getSuitablePos())
        tooltip.show()
        timer=QTimer(self)
        timer.start(3000)
        timer.timeout.connect(lambda:(tooltip.hide(),timer.stop()))
    
    def get_img_from_clipboard(self,e):
        img = ImageGrab.grabclipboard()
        print(f'Got image from clipboard: {type(img)}')
        
        if img is None:
            self.set_tip('错误','剪贴板中无图片')
            return

        img=img.convert('RGB') # 不同截图方式保存在剪贴板中的文件，需要格式统一
        self.img1=img
        img_pixmap=self.clipboard.pixmap()
        self.imagelabel1.setPixmap(scale_qpixmap(img_pixmap))
    
    def ocr_exec(self,e):
        print('OCR started')
        try:
            self.ocr_thread=OCRThread(self.img1)
            self.ocr_thread.result_ready.connect(self.ocr_handle_result)
            self.ocr_thread.start()
        except Exception as e:
            print(f'Error: {e}')

    def ocr_handle_result(self,result):
        if result is not None:
            result=latex_result_replace(result)
            self.textEdit1.setText(result)
            self.textEdit2.setText(f'${result}$')
        print('OCR finished')
        
    def render_latex(self,e):
        text=self.textEdit2.toPlainText()
        print(f'Rendering {text}')
        
        if not cmd_exists('latex'):
            self.set_tip('Latex 未安装','建议安装TexLive，并确保环境变量配置正确。可使用where/which命令检查')
            return
        
        try:
            self.thread=RenderThread({'text':text})
            self.thread.result_ready.connect(self.render_handle_result)
            self.thread.start()
        except Exception as e:
            print(f'Error: {e}')

    def render_handle_result(self,result):
        if result.size[0] == 0 or result.size[1] == 0:
            self.set_tip('渲染失败','请检查latex表达式语法，或在代码中添加宏包')
            return
        print('Render finished')
        self.img2=result
        self.imagelabel2.setPixmap(scale_qpixmap(QPixmap.fromImage(ImageQt.ImageQt(result))))

    def exec_screenshot(self,e):
        print('Screenshot exeuted')
        self.screenshot_widget=CaptureScreen()
        self.screenshot_widget.showFullScreen()
        # self.show()
    
    def save_rendered_image(self,e):
        img=self.imagelabel2.pixmap()
        os.makedirs('output',exist_ok=True)
        img_name=time.strftime('%Y-%m-%d-%H%M%S',time.localtime())+'.png'
        img_path=f'output/{img_name}'
        img.save(img_path)
        print(f'Saved to {img_path}')
        self.set_tip('已保存',f'保存到{img_path}')