from PyQt5.QtGui import QPixmap

import untitled
from PyQt5.QtWidgets import *
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt, QDate


class winlogin(untitled.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(winlogin, self).__init__()
        self.setupUi(self)
        '''界面居中显示'''
        # 获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        '''将信号连接到槽'''
        self.move(int(newLeft), int(newTop))
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(0)
        self.pixmap = QPixmap("./image/警告2 (1).png")
        # pushButton_21 = self.pushButton_2
        self.pushButton_2.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.page))
        self.pushButton_3.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.page_2))
        self.pushButton_4.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.page_3))
        self.pushButton_5.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.page_4))
        self.pushButton_6.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.page_5))
        self.pushButton_7.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.page_6))
        self.pushButton.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.page_7))
        # self.page.pushButton_2.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        # self.page_2.pushButton_3.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        # self.page_3.pushButton_4.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        # self.page_4.pushButton_5.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        # self.page_5.pushButton_6.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        # self.page_6.pushButton_7.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        # self.page_7.pushButton.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        self.run()
    def run(self):
        print("111")
        self.label_5.setText('1营1连一炮')
        self.label_4.setPixmap(self.pixmap)
        self.label_4.resize(self.pixmap.width(), self.pixmap.height())
        self.label_4.setScaledContents(True)
        self.label_2.setText('图标显示2')
        # self.label_2.setText('图标显示3')

    def update_time(self):
        # 获取当前时间和日期
        current_time = QTime.currentTime().toString(Qt.DefaultLocaleLongDate)
        current_date = QDate.currentDate().toString(Qt.DefaultLocaleLongDate)
        # 更新标签显示时间和日期
        self.label_3.setText(f"{current_date} {current_time}")
def main():
    '''防止界面变形'''
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    loginUi = winlogin()  # 将窗口换个名字
    loginUi.show()  # 将窗口显示出来
    sys.exit(app.exec_())  # app.exet_()是指程序一直循环运行直到主窗口被关闭终止进程（如果没有这句话，程序运行时会一闪而过）


if __name__ == '__main__':
    main()