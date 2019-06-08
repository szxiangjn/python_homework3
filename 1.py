import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from test import *

style=['candy','cubist','mosaic','muse','rain','scream','shipwreck','starry','udnie','wave']
# seq=0  # style[seq]
# img_odd=''
# #	原始图像
# img_new=''
# #	转换后图像
# img_show=''
# #	两个图像横向拼接后图像
# img_style=''
# #	原始风格图像
# img_path=''
# #	原始图像路径
# img_path_x=''
# #风格图像路径
class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
