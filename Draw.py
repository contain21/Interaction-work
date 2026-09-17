import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QDialog, QLabel, QMessageBox
from PyQt5.QtGui import QPainter, QPen, QImage, QPixmap, QFont
from PyQt5.QtCore import Qt, QPoint
from drawing_data import drawing_data_instance
from wordgame.music import music_source


class DrawingApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(500, 200, 800, 600)
        self.setWindowTitle('Drawing')

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.canvas = Canvas(self)
        self.layout.addWidget(self.canvas)
        font2 = QFont("STXingkai", 15)
        self.clear_button = QPushButton('Clear', self)
        self.clear_button.clicked.connect(self.canvas.clear)
        self.clear_button.setFont(font2)
        self.clear_button.setStyleSheet(
            "QLabel { border: 2px solid #3498db; padding: 2px; background-color: white; color: #3498db; }"
            "QLabel:hover { background-color: #2980b9; color: white; }")
        self.layout.addWidget(self.clear_button)

        #self.hint_button = QPushButton('Hint', self)
        #self.hint_button.clicked.connect(self.showHint)
        #self.layout.addWidget(self.hint_button)

        self.drawn_image = None  # 添加一个属性用于存储绘制的图像信息
        self.save_button = QPushButton('Save', self)
        self.save_button.clicked.connect(self.saveImage)
        self.save_button.setFont(font2)
        self.save_button.setStyleSheet(
            "QLabel { border: 2px solid #3498db; padding: 2px; background-color: white; color: #3498db; }"
            "QLabel:hover { background-color: #2980b9; color: white; }")
        self.layout.addWidget(self.save_button)

        self.show()

    def saveImage(self):
        music_source.button_sound.play()
        # 将图像保存到共享的实例中
        drawing_data_instance.drawn_image = self.canvas.image
        # 保存成功提示
        QMessageBox.information(self, '保存成功', '图像保存成功！')


class Canvas(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 800, 500)
        self.setStyleSheet("background-color: white;")

        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

        self.drawing = False
        self.lastPoint = QPoint()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(self.rect(), self.image, self.image.rect())

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.lastPoint = event.pos()
            self.drawing = True

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) and self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(Qt.black, 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.drawing:
            self.drawing = False

    def clear(self):
        music_source.button_sound.play()
        self.image.fill(Qt.white)
        self.update()








