import sys

from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider, QPushButton, QLabel
from PyQt5.QtCore import Qt
import pygame
from music import music_source

class SettingsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Settings')
        self.setGeometry(300, 300, 900, 620)

        background_image = QPixmap("2.jpg")  # 替换为你的背景图像路径
        background_label = QLabel(self)
        background_label.setPixmap(background_image)
        background_label.setGeometry(0, 0, 900, 620)

        font1 = QFont("STXingkai", 40)
        title = QLabel("设置", self)
        title.setFont(font1)
        title.setGeometry(360, 50, 200, 80)
        layout = QVBoxLayout(self)

        for idx, (sound_name, sound_obj) in enumerate([
            ("方块一音效", music_source.m1),
            ("方块二音效", music_source.m2),
            ("方块三音效", music_source.m3),
            ("方块四音效", music_source.m4),
            ("按钮音效", music_source.button_sound),
            ("背景音乐", music_source.bgm)
        ]):
            sound_label = QLabel(sound_name, self)

            volume_slider = QSlider(Qt.Horizontal, self)
            volume_slider.setRange(0, 100)
            volume_slider.setValue(50)
            volume_slider.valueChanged.connect(lambda value, sound=sound_obj: self.set_volume(value, sound))
            volume_slider.setStyleSheet(
                "QSlider::groove:horizontal { border: 1px solid #dadbde; height: 10px; background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #dadbde, stop:1 #dadbde); margin: 0px; }"
                "QSlider::handle:horizontal { background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #dadbde, stop:1 #dadbde); border: 1px solid #dadbde; width: 20px; margin: -5px 0; border-radius: 10px; }"
                "QSlider::sub-page:horizontal { background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #45b6fe, stop:1 #dadbde); border: 1px solid #45b6fe; }"
                "QSlider::add-page:horizontal { background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #dadbde, stop:1 #dadbde); border: 1px solid #dadbde; }"
                "QSlider::handle:horizontal:hover { background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #007fff, stop:1 #45b6fe); }"
                "QSlider::sub-page:horizontal:disabled { background: #dadbde; border-color: #dadbde; }"
                "QSlider::add-page:horizontal:disabled { background: #dadbde; border-color: #dadbde; }"
                "QSlider::handle:horizontal:disabled { background: #dadbde; border: 1px solid #dadbde; }")

            # 设置位置
            font = QFont("STXingkai", 20)
            sound_label.setGeometry(100, 150 + idx * 70, 200, 80)
            sound_label.setFont(font)
            volume_slider.setGeometry(300, 170 + idx * 70, 400, 40)


        play_pause_button = QPushButton('播放/暂停', self)
        play_pause_button.setFont(font)
        play_pause_button.clicked.connect(self.play_pause_music)
        play_pause_button.setStyleSheet("QPushButton { border: 2px solid #3498db; padding: 5px; background-color: white; color: #3498db; }"
                                            "QPushButton:hover { background-color: #2980b9; color: white; }")

        # 设置按钮位置
        play_pause_button.setGeometry(720, 510, 150, 50)

    def play_pause_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

    def set_volume(self, value, sound):
        volume = value / 100.0
        sound.set_volume(volume)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_menu = SettingsWindow()
    main_menu.show()
    sys.exit(app.exec_())



