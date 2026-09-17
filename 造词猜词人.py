import sys

import pandas as pd
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QTextEdit, QMessageBox, QDialog
from fuzzywuzzy import fuzz
from openai import OpenAI
import webbrowser
from drawing_data import drawing_data_instance
from music import music_source

class GuesserGame(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
        self.chatgpt_explanation = None

    def init_ui(self):
        self.setWindowTitle('猜词人界面')
        self.setGeometry(500, 200, 900, 640)
        # 设置背景图片
        background_image = QPixmap("5.jpg")  # 替换为你的背景图像路径
        background_label = QLabel(self)
        background_label.setPixmap(background_image)
        background_label.setGeometry(0, 0, 900, 640)
        layout = QVBoxLayout()
        font = QFont("STXingkai", 20)
        font1 = QFont("STXingkai", 40)
        font2=QFont("STXingkai", 15)
        # 添加 ChatGPT 解释按钮
        chatgpt_button = QPushButton('ChatGPT解释', self)
        chatgpt_button.setGeometry(120, 570, 200, 50)
        chatgpt_button.clicked.connect(self.get_chatgpt_explanation)
        chatgpt_button.setFont(font)
        chatgpt_button.setStyleSheet(
            "QPushButton { border: 2px solid #3498db; padding: 5px; background-color: white; color: #3498db; }"
            "QPushButton:hover { background-color: #2980b9; color: white; }")

        # 添加图像按钮
        image_button = QPushButton('显示图像', self)
        image_button.setGeometry(600, 570, 180, 50)
        image_button.clicked.connect(self.show_generated_image)
        image_button.setFont(font)
        image_button.setStyleSheet(
            "QPushButton { border: 2px solid #3498db; padding: 5px; background-color: white; color: #3498db; }"
            "QPushButton:hover { background-color: #2980b9; color: white; }")
        # 添加按钮用于查看绘制的图形
        view_drawn_image_button = QPushButton('提示', self)
        view_drawn_image_button.setGeometry(400, 300, 120, 50)
        view_drawn_image_button.clicked.connect(self.show_drawn_image)
        view_drawn_image_button.setFont(font)
        view_drawn_image_button.setStyleSheet(
            "QPushButton { border: 2px solid #3498db; padding: 5px; background-color: white; color: #3498db; }"
            "QPushButton:hover { background-color: #2980b9; color: white; }")

        self.df_guesser = pd.read_excel('猜词人.xlsx')  # 猜词人表
        self.df_artist = pd.read_excel('出词人.xlsx')  # 出词人表

        self.current_row = 1  # 初始行数

        self.label_word = QLabel(self.df_artist.iloc[self.current_row - 1, 0], self)
        self.label_word.setGeometry(320, 50, 300, 80)  # 设置位置和大小
        self.label_word.setFont(font1)

        self.label_artist_meaning = QLabel('', self)
        self.label_artist_meaning.setGeometry(280, 150, 300, 50)  # 设置位置和大小

        prev_button = QPushButton('上一行', self)
        prev_button.setGeometry(270, 220, 150, 60)
        prev_button.clicked.connect(self.show_previous_row)
        prev_button.setFont(font)
        prev_button.setStyleSheet(
            "QPushButton { border: 2px solid #3498db; padding: 5px; background-color: white; color: #3498db; }"
            "QPushButton:hover { background-color: #2980b9; color: white; }")

        next_button = QPushButton('下一行', self)
        next_button.setGeometry(480, 220, 150, 60)
        next_button.clicked.connect(self.show_next_row)
        next_button.setFont(font)
        next_button.setStyleSheet(
            "QPushButton { border: 2px solid #3498db; padding: 5px; background-color: white; color: #3498db; }"
            "QPushButton:hover { background-color: #2980b9; color: white; }")

        self.info_input = QTextEdit(self)
        self.info_input.setGeometry(160, 370, 600, 180)
        self.info_input.setPlaceholderText('输入猜测的意思')  # 设置占位文本
        self.info_input.setFont(font2)
        self.info_input.setStyleSheet(
            "QTextEdit { background-color: #f0f5f5; border: 2px solid #3498db; padding: 8px; border-radius: 10px; }"
            "QTextEdit::placeholder { color: #95a5a6; }"
            "QTextEdit:focus { border: 2px solid #2980b9; }"
            "QTextEdit:hover { border: 2px solid #2980b9; }")

        submit_button = QPushButton('提交', self)
        submit_button.setGeometry(400, 570, 120, 50)
        submit_button.clicked.connect(self.on_submit)
        submit_button.setFont(font)
        submit_button.setStyleSheet(
            "QPushButton { border: 2px solid #3498db; padding: 5px; background-color: white; color: #3498db; }"
            "QPushButton:hover { background-color: #2980b9; color: white; }")

        self.setLayout(layout)

    def show_previous_row(self):
        music_source.button_sound.play()
        if self.current_row > 1:
            self.current_row -= 1
            self.label_word.setText(self.df_artist.iloc[self.current_row - 1, 0])
            self.label_artist_meaning.setText('')
    def show_next_row(self):
        music_source.button_sound.play()
        if self.current_row < len(self.df_artist):
            self.current_row += 1
            self.label_word.setText(self.df_artist.iloc[self.current_row - 1, 0])
            self.label_artist_meaning.setText('')
    def show_artist_meaning(self):
        guessed_word = self.label_word.text()
        artist_meaning = self.df_artist[self.df_artist['词语'] == guessed_word]['词语意思'].iloc[0]
        self.label_artist_meaning.setText(artist_meaning)
        font2 = QFont("STXingkai", 15)
        self.label_artist_meaning.setFont(font2)



    def on_submit(self):
        music_source.button_sound.play()
        input_text = self.info_input.toPlainText()
        guessed_word = self.label_word.text()

        # 将猜测的意思保存到表格中
        data = {'词语': [guessed_word], '猜测的意思': [input_text]}
        df_submit = pd.DataFrame(data)
        # 读取原始 Excel 文件
        excel_file = '猜词人.xlsx'
        try:
            df_existing = pd.read_excel(excel_file)
            # 将新数据追加到原始数据后面
            df_updated = pd.concat([df_existing, df_submit], ignore_index=True)
        except FileNotFoundError:
            df_updated = df_submit
        df_updated.to_excel('猜词人.xlsx', index=False)
        # 获取出词人给定的意思
        artist_meaning = self.df_artist[self.df_artist['词语'] == guessed_word]['词语意思'].iloc[0]
        # 计算相似度得分
        similarity_score = fuzz.ratio(input_text, artist_meaning)
        # 显示得分
        QMessageBox.information(self, '得分', f'相似度得分：{similarity_score}')
        # 显示出词人给定的意思
        self.show_artist_meaning()

    def show_drawn_image(self):
        music_source.button_sound.play()
        drawn_image = drawing_data_instance.drawn_image
        hint_dialog = HintDialog(self, drawn_image)
        hint_dialog.exec_()

    def get_chatgpt_explanation(self):
        music_source.button_sound.play()
        # 获取当前词语
        current_word = self.label_word.text()

        # 调用 ChatGPT 生成解释
        chatgpt_explanation = self.generate_chatgpt_explanation(current_word)

        # 显示解释（这里可以将结果展示在 QLabel 或其他控件上）
        QMessageBox.information(self, 'ChatGPT 解释', chatgpt_explanation)
        self.chatgpt_explanation=chatgpt_explanation

    def generate_chatgpt_explanation(self, word):
        # 使用 ChatGPT 生成解释
        client = OpenAI()
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "现在你作为一个造词游戏的猜词人，猜测四字词语可能的意思，用一句中文描述"},
                {"role": "user", "content": f"Explain the meaning of {word}."},
            ]
        )
        explanation = completion.choices[0].message.content
        tokens=completion.usage.total_tokens
        print(f'本次对话费用为{(tokens/1000)*0.001}$')
        print(explanation)
        return explanation

    def show_generated_image(self):
        music_source.button_sound.play()
        # 调用 DALL-E 生成图像
        image_url = self.generate_dalle_image()
        QMessageBox.information(self, '生成图像', f'生成的图像链接：{image_url}')
        webbrowser.open(image_url)
    def generate_dalle_image(self):
        # 使用 DALL-E 生成图像
        print(self.chatgpt_explanation)
        client = OpenAI()
        response = client.images.generate(
            model="dall-e-2",
            prompt=self.chatgpt_explanation,
            n=1,
            size="1024x1024"
        )
        image_url = response.data[0].url
        print(image_url)
        return image_url

class HintDialog(QDialog):
    def __init__(self, parent, image):
        super().__init__(parent)
        self.initUI(image)

    def initUI(self, image):
        self.setWindowTitle('提示')
        self.setGeometry(200, 200, 400, 300)

        layout = QVBoxLayout(self)

        label = QLabel(self)
        label.setPixmap(QPixmap.fromImage(image))
        layout.addWidget(label)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_menu = GuesserGame()
    main_menu.show()
    sys.exit(app.exec_())
