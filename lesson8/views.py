import sys

from PyQt6.QtCore import Qt, QObject
from PyQt6.QtGui import QAction, QMouseEvent
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QMenu, QPushButton
from lesson8 import design
from lesson8.handler_control import Handler_control


class MainWindow(QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # инициализация дизайна
        self.pushButton_search.clicked.connect(self.searh_data)
        self.pushButton_del.clicked.connect(self.del_data)
        self.pushButton_unload.clicked.connect(self.unload_data)
        self.hadler_control = Handler_control()
        lst_category = self.hadler_control.get_all_category_name()
        self.comboBox.addItems(lst_category)

    def searh_data(self):
        self.label.setText(
            self.hadler_control.get_data(self.lineEdit.text(), self.comboBox.currentText())
        )


    def add_data(text):
        pass


    def del_data(self):
        self.label.setText(
            self.hadler_control.del_person_info(self.lineEdit_2.text())
        )

    def unload_data(self):
        self.label.setText(
            self.hadler_control.save_json()
        )