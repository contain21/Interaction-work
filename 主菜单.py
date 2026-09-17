from PyQt5.QtGui import QFont
from PyQt5.QtMultimedia import QSound
from 设置 import SettingsWindow
from 造词游戏 import*
from 造字游戏 import*
import pygame
from music import music_source
class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Main Menu')
        self.setGeometry(460, 160, 900, 620)

        # 设置背景图片
        background_image = QPixmap("1.jpg")  # 替换为你的背景图像路径
        background_label = QLabel(self)
        background_label.setPixmap(background_image)
        background_label.setGeometry(0, 0, 900, 620)

        word_game_button = QPushButton('开始游戏',self)
        setting_button = QPushButton('设置',self)

        font = QFont("STXingkai", 20)
        word_game_button.setFont(font)
        setting_button.setFont(font)


        #background_label.setScaledContents(True)

        font1 = QFont("STXingkai", 40)
        title=QLabel("造词游戏",self)
        title.setFont(font1)
        title.setGeometry(320,100,300,80)
        word_game_button.setStyleSheet("QPushButton { border: 2px solid #3498db; padding: 5px; background-color: white; color: #3498db; }"
                                            "QPushButton:hover { background-color: #2980b9; color: white; }")
        setting_button.setStyleSheet("QPushButton { border: 2px solid #3498db; padding: 5px; background-color: white; color: #3498db; }"
                                            "QPushButton:hover { background-color: #2980b9; color: white; }")


        word_game_button.setGeometry(350,300,200,80)
        setting_button.setGeometry(350,450,200,80)

        word_game_button.clicked.connect(self.show_word_game)
        setting_button.clicked.connect(self.show_setting)



    def show_word_game(self):
        music_source.button_sound.play()
        self.word_game = WordGame()
        self.word_game.show()

    def show_setting(self):
        music_source.button_sound.play()
        self.set_window=SettingsWindow()
        self.set_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_menu = MainMenu()
    main_menu.show()
    sys.exit(app.exec_())

