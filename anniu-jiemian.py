import sys
from PyQt5.QtCore import QTime, QDate, Qt, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow
from untitled import Ui_MainWindow
from PyQt5.QtGui import QPixmap


class WinLogin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.run()
    def run(self):
        # 将信号连接到槽
        self.ui.pushButton_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        self.ui.pushButton_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.pushButton_4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
        self.ui.pushButton_5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))
        self.ui.pushButton_6.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_5))
        self.ui.pushButton_7.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_6))
        self.ui.pushButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_7))
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(0)
        self.ui.label_5.setText('1营1连一炮')
        pixmap = QPixmap("./image/警告2 (1).png")
        pixmap = pixmap.scaled(30, 30)
        self.ui.label_4.setPixmap(pixmap)
        self.ui.label_2.setAlignment(Qt.AlignRight)
        self.ui.label_2.setText('图标显示2')
        self.ui.label_2.setAlignment(Qt.AlignRight)
    def update_time(self):
        # 获取当前时间和日期
        current_time = QTime.currentTime().toString(Qt.DefaultLocaleLongDate)
        current_date = QDate.currentDate().toString(Qt.DefaultLocaleLongDate)
        # 更新标签显示时间和日期
        self.ui.label_3.setText(f"{current_date} {current_time}")


def main():
    app = QApplication(sys.argv)
    login_ui = WinLogin()
    login_ui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
