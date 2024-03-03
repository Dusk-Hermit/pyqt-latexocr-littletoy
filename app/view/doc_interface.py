from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QFont
from qfluentwidgets import ScrollArea,TitleLabel

from ..common.style_sheet import StyleSheet

class DocInterface(ScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        
    def initUI(self):
        StyleSheet.HOME_INTERFACE.apply(self)
        self.view=QWidget(self)
        
        self.view.setObjectName('view')
        self.setObjectName('docInterface')
        
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setWidget(self.view)
        self.setWidgetResizable(True)
        
        # 布局
        self.vBoxLayout = QVBoxLayout(self.view)
        self.setFixedSize(900, 600)
        
        self.vBoxLayout.setSpacing(20)
        self.vBoxLayout.setContentsMargins(40, 40, 40, 40)
        self.vBoxLayout.setAlignment(Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop )
        
        # 组件
        
        self.titleLabel1=TitleLabel('界面使用说明',self)
        self.text1=QLabel('''
        1、Screenshot：截图工具，可以截取屏幕上的任意区域，截图结果保存到剪贴板。
        2、Clipboard：将左栏第一张图片设置为剪贴板图片，准备执行识别。即也可以使用区别于按钮1的其他的截图工具将图片保存到剪贴板。
        3、OCR：执行识别，将剪贴板图片识别为LaTeX公式，并填充进右栏的两个文本框，其中上面的是只读，下面可以编辑。
        4、Render：将右栏第二个文本框中的LaTeX公式渲染为图片，并显示在左栏的第二张图片位置上。
        5、Save：将左栏第二张图片保存到本地。
        6、Copy：将右侧第二栏文本框中内容粘贴到剪贴板，便于直接复制到其他地方。
        
        '''.strip().replace(' ',''),self)
        self.titleLabel2=TitleLabel('注意事项',self)
        self.text2=QLabel('''
        1、确保Texlive安装好，并配置好环境变量，建议使用国内镜像安装，10-20min即可。MikeTex由于缺少一些包，可能会导致渲染失败。
        2、安装环境后，第一次运行会下载权重文件，会在开始界面中卡一会
        
                          '''.strip().replace(' ','') ,self)
        
        self.vBoxLayout.addWidget(self.titleLabel1)
        self.vBoxLayout.addWidget(self.text1)
        self.vBoxLayout.addWidget(self.titleLabel2)
        self.vBoxLayout.addWidget(self.text2)
        
        self.text1.setFont(QFont('微软雅黑', 12))
        self.text2.setFont(QFont('微软雅黑', 12))
        self.text1.setWordWrap(True)
        self.text2.setWordWrap(True)