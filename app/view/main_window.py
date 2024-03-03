from PyQt6.QtCore import Qt,  QSize
from PyQt6.QtGui import QIcon,QGuiApplication,QFontDatabase
from PyQt6.QtWidgets import QApplication


from qfluentwidgets import FluentIcon as FIF

from qfluentwidgets import SplashScreen, setThemeColor, NavigationBarPushButton, setTheme, Theme,FluentWindow
from qfluentwidgets import FluentIcon as FIF

from .home_interface import HomeInterface
from .doc_interface import DocInterface

from ..common  import src_rc



class MainWindow(FluentWindow):

    def __init__(self):
        super().__init__()
        self.initWindow()

        self.initInterface()
        self.initNavigation()
        
        self.splashScreen.finish()


    def initWindow(self):
        setThemeColor('#136FF0', lazy=True)
        setTheme(Theme.AUTO, lazy=True)
        # self.setMicaEffectEnabled(False)

        # 禁用最大化
        self.titleBar.maxBtn.setHidden(True)
        self.titleBar.maxBtn.setDisabled(True)
        self.titleBar.setDoubleClickEnabled(False)
        self.setResizeEnabled(False)
        self.setWindowFlags(Qt.WindowType.WindowMinimizeButtonHint | Qt.WindowType.WindowCloseButtonHint)

        self.resize(960, 680)
        self.setWindowIcon(QIcon(':/resource/favicon (5).ico'))
        self.setWindowTitle("Latex OCR")

        # 启动界面
        self.splashScreen = SplashScreen(self.windowIcon(),self)
        self.splashScreen.setIconSize(QSize(106, 106))
        self.splashScreen.raise_()

        desktop = QGuiApplication.primaryScreen().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

        self.show()
        QApplication.processEvents()

    def initInterface(self):
        fontID=QFontDatabase.addApplicationFont(':/ttf/SourceCodePro-Regular.ttf')  # Source Code Pro
        fontID=QFontDatabase.addApplicationFont(':/ttf/Hack-Regular.ttf')   # Hack

        # print(fontID)
        # fontFamilies = QFontDatabase.applicationFontFamilies(fontID)
        # print(fontFamilies)
        
        
        self.homeInterface = HomeInterface(self)
        self.docInterface = DocInterface(self)

    def initNavigation(self):
        self.addSubInterface(self.homeInterface, FIF.HOME, self.tr('Latex 识别'))
        self.addSubInterface(self.docInterface, FIF.DOCUMENT, self.tr('使用简介'))
