from PyQt6.QtCore import Qt, QSize, QUrl
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout,QGridLayout,QButtonGroup,QLabel
from PyQt6.QtGui import QPixmap,QImage
from qfluentwidgets import (Action, DropDownPushButton, DropDownToolButton, PushButton, ToolButton, TextEdit,PrimaryPushButton,ScrollArea,ImageLabel)

from ..common.style_sheet import StyleSheet

class HomeInterface(ScrollArea):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.initUI()
        # self.loadModel()
        
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
        
        img1=QImage(r"C:\Users\Dusk_Hermit\Desktop\1.jpg".replace('\\','/')).scaledToWidth(350)
        img2=QImage(r"C:\Users\Dusk_Hermit\Desktop\2.jpg".replace('\\','/')).scaledToWidth(350)
        
        self.imagelabel1.setPixmap(QPixmap.fromImage(img1))
        self.imagelabel2.setPixmap(QPixmap.fromImage(img2))
        
        # self.imagelabel1.setBaseSize(300,400)
        # self.imagelabel2.setBaseSize(300,300)
        
        self.w1=ScrollArea(self.view1)
        self.w2=ScrollArea(self.view1)
        
        self.w1.setWidget(self.imagelabel1)
        self.w2.setWidget(self.imagelabel2)
        self.w1.horizontalScrollBar().setValue(0)
        self.w2.horizontalScrollBar().setValue(0)
        self.w1.setFixedHeight(250)
        self.w2.setFixedHeight(250)
        self.w1.setAlignment(Qt.AlignmentFlag.AlignHCenter )
        self.w2.setAlignment(Qt.AlignmentFlag.AlignHCenter )
        
        self.vBoxLayout1.addWidget(self.w1,0,0)
        self.vBoxLayout1.addWidget(self.w2,1,0)
        
        ## 第二栏
        self.button1 = PushButton('图片1',self.view2)
        self.button2 = PushButton('图片2',self.view2)
        self.button3 = PushButton('图片3',self.view2)
        
        self.button1.setFixedWidth(60)
        self.button2.setFixedWidth(60)
        self.button3.setFixedWidth(60)
        
        self.vBoxLayout2.addWidget(self.button1,0,0)
        self.vBoxLayout2.addWidget(self.button2,1,0)
        self.vBoxLayout2.addWidget(self.button3,2,0)
        
        ## 第三栏
        self.textEdit1 = TextEdit(self.view3)
        self.textEdit2 = TextEdit(self.view3)
        
        self.textEdit1.setFixedSize(300,250)
        self.textEdit2.setFixedSize(300,250)
        
        self.vBoxLayout3.addWidget(self.textEdit1,0,0)
        self.vBoxLayout3.addWidget(self.textEdit2,1,0)
        
    def get_img_from_clipboard(self):
        pass
    
    def ocr_exec(self):
        pass
    
    def render_latex(self):
        pass
    