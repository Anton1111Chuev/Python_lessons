import sys
from PyQt6.QtWidgets import QApplication
from lesson8.views import MainWindow


class Control():
    def __init__(self, type_of_view):
        if type_of_view == 1:
            self.app = QApplication(sys.argv)
            self.window = MainWindow()
            self.window.show()
            self.__start_app()
        else:
            print("Не известный тип view проверьте настройку параметра type_of_view")

    def __start_app(self):
        self.app.exec()