import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setWindowTitle('Change Icon Color')
        self.setGeometry(300, 300, 300, 200)

        # 创建一个按钮
        self.btn = QPushButton('Change Color', self)
        self.btn.setGeometry(100, 150, 100, 30)
        self.btn.clicked.connect(self.change_color)

        # 创建一个标签
        self.label = QLabel(self)
        self.label.setGeometry(100, 50, 100, 100)

        # 设置标签的图标
        pixmap = QPixmap('icon1.png').scaled(100, 100, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.label.setPixmap(pixmap)

    def change_color(self):

        # 更改图标颜色
        self.label.setPixmap(self.colorize_icon('icon1.png', '#00FF00'))

    def colorize_icon(self, icon_path, color):

        # 加载图标
        pixmap = QPixmap(icon_path).scaled(100, 100, Qt.KeepAspectRatio, Qt.FastTransformation)

        # 创建一个纯色图像
        image = pixmap.toImage()
        color_hex = color.replace('#', '')
        r, g, b = int(color_hex[0:2], 16), int(color_hex[2:4], 16), int(color_hex[4:6], 16)
        for x in range(image.width()):
            for y in range(image.height()):
                pixel_color = image.pixelColor(x, y)
                if pixel_color.alpha() > 0:
                    image.setPixelColor(x, y, Qt.QColor(r, g, b))

        # 返回一个新的pixmap
        return QPixmap.fromImage(image)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
