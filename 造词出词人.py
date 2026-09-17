import pandas as pd
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton,QTextEdit,QMessageBox
from PyQt5.QtCore import Qt
from Draw import*
from music import music_source

class WordArtistGame(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('出词人界面')
        self.setGeometry(500, 200, 900, 640)
        font = QFont("STXingkai", 20)
        font2 = QFont("STXingkai", 15)
        # 设置背景图片
        background_image = QPixmap("6.jpg")  # 替换为你的背景图像路径
        background_label = QLabel(self)
        background_label.setPixmap(background_image)
        background_label.setGeometry(0, 0, 900, 640)
        # 创建垂直布局
        layout = QVBoxLayout()
        self.central_label = QLabel('点击方块上的文字', self)
        self.central_label.setGeometry(325, 255, 300, 50)  # 居中显示
        self.central_label.setFont(font)

        # 读取Excel表格数据
        df = pd.read_excel('32块方块上的192字.xlsx', index_col=0)
        # 随机选取四个方块
        selected_blocks = df.sample(n=4)
        # 获取被选中行的索引（方块序号）
        selected_block_numbers = selected_blocks.index.tolist()
        # 将选取的四行元素构成列表
        selected_blocks_list = selected_blocks.values.tolist()
        # 输出方块序号和对应的行数据
        for block_number, row_data in zip(selected_block_numbers, selected_blocks_list):
            print(f'方块序号: {block_number}, 行数据: {row_data}')


         # 创建四个空白方格，并设置位置和大小
        self.blank_squares = [QLabel('', self) for _ in range(4)]
        positions = [(340, 320), (400, 320), (460, 320), (520, 320)]  # 指定每个方格的位置
        sizes = [(50, 40)] * 4  # 指定每个方格的大小

        for square, position, size in zip(self.blank_squares, positions, sizes):
            square.setGeometry(*position, *size)
            square.setAlignment(Qt.AlignCenter)
            square.setStyleSheet('border: 2px solid black;')  # 添加黑色边框

        # 创建按钮点击事件处理函数
        def label_click_handler1(word, square):
            music_source.m1.play()
            square.setText(word)
            square.setFont(font)


        def label_click_handler2(word, square):
            music_source.m2.play()
            square.setText(word)
            square.setFont(font)

        def label_click_handler3(word, square):
            music_source.m3.play()
            square.setText(word)
            square.setFont(font)

        def label_click_handler4(word, square):
            music_source.m4.play()
            square.setText(word)
            square.setFont(font)

        for i in range(4):
            # 创建标签并设置位置和大小
            label_cube = QLabel(f'方块{i + 1}', self)
            label_cube.setFont(font2)
            label_cube.setGeometry(95 + i * 200, 210, 100, 20)
        #方块一文字
        label_word1_1 = QLabel(selected_blocks_list[0][0], self)
        label_word1_1.setGeometry(50, 50, 50, 40)  # 设置位置和大小
        label_word1_1.setFont(font)
        label_word1_1.mousePressEvent = lambda event, word=selected_blocks_list[0][0], square=self.blank_squares[0]: label_click_handler1(word,square)
        label_word1_1.setStyleSheet(
            "QLabel { border: 2px solid #3498db; padding: 2px; background-color: white; color: #3498db; }"
            "QLabel:hover { background-color: #2980b9; color: white; }")

        label_word1_2 = QLabel(selected_blocks_list[0][1], self)
        label_word1_2.setGeometry(150, 50, 50, 40)  # 设置位置和大小
        label_word1_2.setFont(font)
        label_word1_2.mousePressEvent = lambda event, word=selected_blocks_list[0][1],square=self.blank_squares[0]: label_click_handler1(word, square)
        label_word1_2.setStyleSheet("QLabel { border: 2px solid #3498db; padding: 2px; background-color: white; color: #3498db; }"
                                            "QLabel:hover { background-color: #2980b9; color: white; }")

        label_word1_3 = QLabel(selected_blocks_list[0][2], self)
        label_word1_3.setGeometry(50, 100, 50, 40)  # 设置位置和大小
        label_word1_3.setFont(font)
        label_word1_3.mousePressEvent = lambda event, word=selected_blocks_list[0][2],square=self.blank_squares[0]: label_click_handler1(word, square)
        label_word1_3.setStyleSheet(
            "QLabel { border: 2px solid #3498db; padding: 2px; background-color: white; color: #3498db; }"
            "QLabel:hover { background-color: #2980b9; color: white; }")

        label_word1_4 = QLabel(selected_blocks_list[0][3], self)
        label_word1_4.setGeometry(150, 100, 50, 40)  # 设置位置和大小
        label_word1_4.setFont(font)
        label_word1_4.mousePressEvent = lambda event, word=selected_blocks_list[0][3],square=self.blank_squares[0]: label_click_handler1(word, square)
        label_word1_4.setStyleSheet(
            "QLabel { border: 2px solid #3498db; padding: 2px; background-color: white; color: #3498db; }"
            "QLabel:hover { background-color: #2980b9; color: white; }")

        label_word1_5 = QLabel(selected_blocks_list[0][4], self)
        label_word1_5.setGeometry(50, 150, 50, 40)  # 设置位置和大小
        label_word1_5.setFont(font)
        label_word1_5.mousePressEvent = lambda event, word=selected_blocks_list[0][4],square=self.blank_squares[0]: label_click_handler1(word, square)
        label_word1_5.setStyleSheet(
            "QLabel { border: 2px solid #3498db; padding: 2px; background-color: white; color: #3498db; }"
            "QLabel:hover { background-color: #2980b9; color: white; }")

        label_word1_6 = QLabel(selected_blocks_list[0][5], self)
        label_word1_6.setGeometry(150, 150, 50, 40)  # 设置位置和大小
        label_word1_6.setFont(font)
        label_word1_6.mousePressEvent = lambda event, word=selected_blocks_list[0][5],square=self.blank_squares[0]: label_click_handler1(word, square)
        label_word1_6.setStyleSheet(
            "QLabel { border: 2px solid #3498db; padding: 2px; background-color: white; color: #3498db; }"
            "QLabel:hover { background-color: #2980b9; color: white; }")

        #方块二文字
        label_word2_1 = QLabel(selected_blocks_list[1][0], self)
        label_word2_1.setGeometry(250, 50, 50, 40)  # 设置位置和大小
        label_word2_1.setFont(font)
        label_word2_1.mousePressEvent = lambda event, word=selected_blocks_list[1][0],square=self.blank_squares[1]: label_click_handler2(word, square)
        label_word2_1.setStyleSheet(
            "QLabel { border: 2px solid #2ecc71; padding: 2px; background-color: white; color: #2ecc71; }"
            "QLabel:hover { background-color: #27ae60; color: white; }")

        label_word2_2 = QLabel(selected_blocks_list[1][1], self)
        label_word2_2.setGeometry(350, 50, 50, 40)  # 设置位置和大小
        label_word2_2.setFont(font)
        label_word2_2.mousePressEvent = lambda event, word=selected_blocks_list[1][1],square=self.blank_squares[1]: label_click_handler2(word, square)
        label_word2_2.setStyleSheet(
            "QLabel { border: 2px solid #2ecc71; padding: 2px; background-color: white; color: #2ecc71; }"
            "QLabel:hover { background-color: #27ae60; color: white; }")

        label_word2_3 = QLabel(selected_blocks_list[1][2], self)
        label_word2_3.setGeometry(250, 100, 50, 40)  # 设置位置和大小
        label_word2_3.setFont(font)
        label_word2_3.mousePressEvent = lambda event, word=selected_blocks_list[1][2],square=self.blank_squares[1]: label_click_handler2(word, square)
        label_word2_3.setStyleSheet(
            "QLabel { border: 2px solid #2ecc71; padding: 2px; background-color: white; color: #2ecc71; }"
            "QLabel:hover { background-color: #27ae60; color: white; }")

        label_word2_4 = QLabel(selected_blocks_list[1][3], self)
        label_word2_4.setGeometry(350, 100, 50, 40)  # 设置位置和大小
        label_word2_4.setFont(font)
        label_word2_4.mousePressEvent = lambda event, word=selected_blocks_list[1][3],square=self.blank_squares[1]: label_click_handler2(word, square)
        label_word2_4.setStyleSheet(
            "QLabel { border: 2px solid #2ecc71; padding: 2px; background-color: white; color: #2ecc71; }"
            "QLabel:hover { background-color: #27ae60; color: white; }")

        label_word2_5 = QLabel(selected_blocks_list[1][4], self)
        label_word2_5.setGeometry(250, 150, 50, 40)  # 设置位置和大小
        label_word2_5.setFont(font)
        label_word2_5.mousePressEvent = lambda event, word=selected_blocks_list[1][4],square=self.blank_squares[1]: label_click_handler2(word, square)
        label_word2_5.setStyleSheet(
            "QLabel { border: 2px solid #2ecc71; padding: 2px; background-color: white; color: #2ecc71; }"
            "QLabel:hover { background-color: #27ae60; color: white; }")

        label_word2_6 = QLabel(selected_blocks_list[1][5], self)
        label_word2_6.setGeometry(350, 150, 50, 40)  # 设置位置和大小
        label_word2_6.setFont(font)
        label_word2_6.mousePressEvent = lambda event, word=selected_blocks_list[1][5],square=self.blank_squares[1]: label_click_handler2(word, square)
        label_word2_6.setStyleSheet(
            "QLabel { border: 2px solid #2ecc71; padding: 2px; background-color: white; color: #2ecc71; }"
            "QLabel:hover { background-color: #27ae60; color: white; }")

        # 方块三文字
        label_word3_1 = QLabel(selected_blocks_list[2][0], self)
        label_word3_1.setGeometry(450, 50, 50, 40)  # 设置位置和大小
        label_word3_1.setFont(font)
        label_word3_1.mousePressEvent = lambda event, word=selected_blocks_list[2][0],square=self.blank_squares[2]: label_click_handler3(word, square)
        label_word3_1.setStyleSheet(
            "QLabel { border: 2px solid #95a5a6; padding: 2px; background-color: white; color: #95a5a6; }"
            "QLabel:hover { background-color: #7f8c8d; color: white; }")

        label_word3_2 = QLabel(selected_blocks_list[2][1], self)
        label_word3_2.setGeometry(550, 50, 50, 40)  # 设置位置和大小
        label_word3_2.setFont(font)
        label_word3_2.mousePressEvent = lambda event, word=selected_blocks_list[2][1],square=self.blank_squares[2]: label_click_handler3(word, square)
        label_word3_2.setStyleSheet(
            "QLabel { border: 2px solid #95a5a6; padding: 2px; background-color: white; color: #95a5a6; }"
            "QLabel:hover { background-color: #7f8c8d; color: white; }")

        label_word3_3 = QLabel(selected_blocks_list[2][2], self)
        label_word3_3.setGeometry(450, 100, 50, 40)  # 设置位置和大小
        label_word3_3.setFont(font)
        label_word3_3.mousePressEvent = lambda event, word=selected_blocks_list[2][2],square=self.blank_squares[2]: label_click_handler3(word, square)
        label_word3_3.setStyleSheet(
            "QLabel { border: 2px solid #95a5a6; padding: 2px; background-color: white; color: #95a5a6; }"
            "QLabel:hover { background-color: #7f8c8d; color: white; }")

        label_word3_4 = QLabel(selected_blocks_list[2][3], self)
        label_word3_4.setGeometry(550, 100, 50, 40)  # 设置位置和大小
        label_word3_4.setFont(font)
        label_word3_4.mousePressEvent = lambda event, word=selected_blocks_list[2][3],square=self.blank_squares[2]: label_click_handler3(word, square)
        label_word3_4.setStyleSheet(
            "QLabel { border: 2px solid #95a5a6; padding: 2px; background-color: white; color: #95a5a6; }"
            "QLabel:hover { background-color: #7f8c8d; color: white; }")

        label_word3_5 = QLabel(selected_blocks_list[2][4], self)
        label_word3_5.setGeometry(450, 150, 50, 40)  # 设置位置和大小
        label_word3_5.setFont(font)
        label_word3_5.mousePressEvent = lambda event, word=selected_blocks_list[2][4],square=self.blank_squares[2]: label_click_handler3(word, square)
        label_word3_5.setStyleSheet(
            "QLabel { border: 2px solid #95a5a6; padding: 2px; background-color: white; color: #95a5a6; }"
            "QLabel:hover { background-color: #7f8c8d; color: white; }")

        label_word3_6 = QLabel(selected_blocks_list[2][5], self)
        label_word3_6.setGeometry(550, 150, 50, 40)  # 设置位置和大小
        label_word3_6.setFont(font)
        label_word3_6.mousePressEvent = lambda event, word=selected_blocks_list[2][5],square=self.blank_squares[2]: label_click_handler3(word, square)
        label_word3_6.setStyleSheet(
            "QLabel { border: 2px solid #95a5a6; padding: 2px; background-color: white; color: #95a5a6; }"
            "QLabel:hover { background-color: #7f8c8d; color: white; }")

        # 方块四文字
        label_word4_1 = QLabel(selected_blocks_list[3][0], self)
        label_word4_1.setGeometry(650, 50, 50, 40)  # 设置位置和大小
        label_word4_1.setFont(font)
        label_word4_1.mousePressEvent = lambda event, word=selected_blocks_list[3][0],square=self.blank_squares[3]: label_click_handler4(word, square)
        label_word4_1.setStyleSheet(
            "QLabel { border: 2px solid #e91e63; padding: 2px; background-color: white; color: #e91e63; }"
            "QLabel:hover { background-color: #d81b60; color: white; }")

        label_word4_2 = QLabel(selected_blocks_list[3][1], self)
        label_word4_2.setGeometry(750, 50, 50, 40)  # 设置位置和大小
        label_word4_2.setFont(font)
        label_word4_2.mousePressEvent = lambda event, word=selected_blocks_list[3][1],square=self.blank_squares[3]: label_click_handler4(word, square)
        label_word4_2.setStyleSheet(
            "QLabel { border: 2px solid #e91e63; padding: 2px; background-color: white; color: #e91e63; }"
            "QLabel:hover { background-color: #d81b60; color: white; }")

        label_word4_3 = QLabel(selected_blocks_list[3][2], self)
        label_word4_3.setGeometry(650, 100, 50, 40)  # 设置位置和大小
        label_word4_3.setFont(font)
        label_word4_3.mousePressEvent = lambda event, word=selected_blocks_list[3][2],square=self.blank_squares[3]: label_click_handler4(word, square)
        label_word4_3.setStyleSheet(
            "QLabel { border: 2px solid #e91e63; padding: 2px; background-color: white; color: #e91e63; }"
            "QLabel:hover { background-color: #d81b60; color: white; }")

        label_word4_4 = QLabel(selected_blocks_list[3][3], self)
        label_word4_4.setGeometry(750, 100, 50, 40)  # 设置位置和大小
        label_word4_4.setFont(font)
        label_word4_4.mousePressEvent = lambda event, word=selected_blocks_list[3][3],square=self.blank_squares[3]: label_click_handler4(word, square)
        label_word4_4.setStyleSheet(
            "QLabel { border: 2px solid #e91e63; padding: 2px; background-color: white; color: #e91e63; }"
            "QLabel:hover { background-color: #d81b60; color: white; }")

        label_word4_5 = QLabel(selected_blocks_list[3][4], self)
        label_word4_5.setGeometry(650, 150, 50, 40)  # 设置位置和大小
        label_word4_5.setFont(font)
        label_word4_5.mousePressEvent = lambda event, word=selected_blocks_list[3][4],square=self.blank_squares[3]: label_click_handler4(word, square)
        label_word4_5.setStyleSheet(
            "QLabel { border: 2px solid #e91e63; padding: 2px; background-color: white; color: #e91e63; }"
            "QLabel:hover { background-color: #d81b60; color: white; }")

        label_word4_6 = QLabel(selected_blocks_list[3][5], self)
        label_word4_6.setGeometry(750, 150, 50, 40)  # 设置位置和大小
        label_word4_6.setFont(font)
        label_word4_6.mousePressEvent = lambda event, word=selected_blocks_list[3][5],square=self.blank_squares[3]: label_click_handler4(word, square)
        label_word4_6.setStyleSheet(
            "QLabel { border: 2px solid #e91e63; padding: 2px; background-color: white; color: #e91e63; }"
            "QLabel:hover { background-color: #d81b60; color: white; }")

        # 创建用于输入信息的文本框

        self.info_input = QTextEdit(self)
        self.info_input.setGeometry(160, 380, 600, 180)  # 设置位置和大小
        self.info_input.setPlaceholderText('在此输入词语意思')  # 设置占位文本
        self.info_input.setFont(font2)
        self.info_input.setStyleSheet(
            "QTextEdit { background-color: #f0f5f5; border: 2px solid #3498db; padding: 8px; border-radius: 10px; }"
            "QTextEdit::placeholder { color: #95a5a6; }"
            "QTextEdit:focus { border: 2px solid #2980b9; }"
            "QTextEdit:hover { border: 2px solid #2980b9; }")
        # 创建提交按钮
        submit_button = QPushButton('提交', self)
        submit_button.setGeometry(280,570,120,50)
        submit_button.clicked.connect(self.on_submit)
        submit_button.setFont(font)
        submit_button.setStyleSheet(
            "QPushButton { border: 2px solid #3498db; padding: 5px; background-color: white; color: #3498db; }"
            "QPushButton:hover { background-color: #2980b9; color: white; }")
        #创建绘制按钮
        submit_draw = QPushButton('绘制', self)
        submit_draw.setGeometry(540, 570, 120, 50)
        submit_draw.clicked.connect(self.show_draw)
        submit_draw.setFont(font)
        submit_draw.setStyleSheet(
            "QPushButton { border: 2px solid #3498db; padding: 5px; background-color: white; color: #3498db; }"
            "QPushButton:hover { background-color: #2980b9; color: white; }")
        self.setLayout(layout)

    def show_draw(self):
        music_source.button_sound.play()
        self.dra_window=DrawingApp()
        self.dra_window.show()

    def on_submit(self):
        music_source.button_sound.play()
        # 获取输入信息和方块文字
        input_text = self.info_input.toPlainText()
        block_texts = ''.join([square.text() for square in self.blank_squares])  # 将文字直接连接在一起

        # 在这里将数据保存到表格中，使用 pandas 的 DataFrame 进行操作
        data = {'词语': [block_texts], '词语意思': [input_text]}
        df = pd.DataFrame(data)
        print(df)
        # 追加数据到 Excel 文件
        excel_file = '出词人.xlsx'  # 请替换为你想要保存的 Excel 文件名
        try:
            existing_df = pd.read_excel(excel_file)
            updated_df = pd.concat([existing_df, df], ignore_index=True)
        except FileNotFoundError:
            updated_df = df

        updated_df.to_excel(excel_file, index=False)

        # 打印输出提交成功信息
        print(f'提交成功！方块文字: {block_texts}, 词语意思: {input_text}')

        # 显示提交成功的提示框
        QMessageBox.information(self, '提示', '提交成功！')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_menu = WordArtistGame()
    main_menu.show()
    sys.exit(app.exec_())