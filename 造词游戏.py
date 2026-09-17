from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton,QTextEdit,QMessageBox
from 造词出词人 import*
from 造词猜词人 import*
from music import music_source

class WordGame(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('造词游戏')
        self.setGeometry(480, 180, 900, 620)

        background_image = QPixmap("3.jpg")  # 替换为你的背景图像路径
        background_label = QLabel(self)
        background_label.setPixmap(background_image)
        background_label.setGeometry(0, 0, 900, 620)

        artist_button = QPushButton('出词人',self)
        guesser_button = QPushButton('猜词人',self)

        font1 = QFont("STXingkai", 40)
        label_word = QLabel("角色选择", self)
        label_word.setFont(font1)
        label_word.setGeometry(320,100,300,80)


        font = QFont("STXingkai", 20)
        artist_button.setFont(font)
        guesser_button.setFont(font)

        artist_button.setGeometry(350,380,200,80)
        guesser_button.setGeometry(350,500 ,200,80)

        artist_button.setStyleSheet("QPushButton { border: 2px solid #3498db; padding: 5px; background-color: white; color: #3498db; }"
                                            "QPushButton:hover { background-color: #2980b9; color: white; }")
        guesser_button.setStyleSheet("QPushButton { border: 2px solid #3498db; padding: 5px; background-color: white; color: #3498db; }"
                                            "QPushButton:hover { background-color: #2980b9; color: white; }")

        artist_button.clicked.connect(self.show_word_artist_game)
        guesser_button.clicked.connect(self.show_guesser_game)



    def show_word_artist_game(self):
        music_source.button_sound.play()
        self.word_artist_game = WordArtistGame()
        self.word_artist_game.show()


    def show_guesser_game(self):
        music_source.button_sound.play()
        self.guesser_game = GuesserGame()
        self.guesser_game.show()


    def start_word_game(self):
        role = "出词人" if self.sender() == self.artist_button else "猜词人"
        print(f"进入造词游戏，角色: {role}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_menu = WordGame()
    main_menu.show()
    sys.exit(app.exec_())