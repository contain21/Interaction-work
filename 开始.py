import sys
from PyQt5.QtWidgets import QApplication
from 主菜单 import*

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_menu = MainMenu()
    main_menu.show()
    music_source.bgm.play(loops=-1)
    sys.exit(app.exec_())