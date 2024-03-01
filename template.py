from PyQt6 import QtWidgets,QtCore
import sys

if __name__=="__main__":
    # QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app=QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QMainWindow()
    ui=Ui_MainWindow()    
    #我这边是默认的Ui_MainWindow，要是你们自己有修改，这边要相应修改
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec())


# pyuic6 -o outputUI.py untitled.ui
