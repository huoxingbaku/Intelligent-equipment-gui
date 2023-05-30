from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("向右对齐")
        self.setGeometry(100, 100, 400, 300)

        label = QLabel(self)
        label.setText("文本内容")
        label.setAlignment(Qt.AlignRight)  # 设置文本向右对齐

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
