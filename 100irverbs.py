#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore
from gui_verbs import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys
import csv
import random
 
class mywindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.pushButton_2.clicked.connect(self.btnClicked_2)
        self.ui.lineEdit.setMaxLength(16)
        self.ui.lineEdit_2.setMaxLength(16)
        self.ui.lineEdit_3.setMaxLength(16)
        self.ui.lineEdit_4.setMaxLength(16)
        self.ui.lineEdit_5.setMaxLength(16)
        self.ui.lineEdit_5.setReadOnly(True)
        self.ui.lineEdit_6.setMaxLength(16)
        self.ui.lineEdit_6.setReadOnly(True)
        self.ui.lineEdit_7.setMaxLength(16)
        self.ui.lineEdit_7.setReadOnly(True)
        self.ui.lineEdit_8.setMaxLength(16)
        self.ui.lineEdit_8.setReadOnly(True)
        self.ui.lineEdit_9.setReadOnly(True)

    def btnClicked(self):
        global randomline 
        randomline = [] #рандомная строка из списка
        verbs = str()
        random_number_line = random.randint(1, 99)
        random_number_word = random.randint(1, 4)
    
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()
        self.ui.lineEdit_5.clear()
        self.ui.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.lineEdit_6.clear()
        self.ui.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.lineEdit_7.clear()
        self.ui.lineEdit_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.lineEdit_8.clear()
        self.ui.lineEdit_8.setStyleSheet("background-color: rgb(255, 255, 255);")

        with open("100IRverbs.csv") as file:
            lines = file.readlines()
        lines = ' '.join(lines[random_number_line:random_number_line+1])
        randomline = lines.split(';')
        randomline = [line.rstrip() for line in randomline]
        verbs = randomline[random_number_word]

        self.ui.lineEdit_9.setText(verbs)
        # Если не использовать, то часть текста исчезнет.
        self.ui.lineEdit_9.adjustSize()
    
    def btnClicked_2(self):
        self.ui.lineEdit_5.setText(randomline[1])
        self.ui.lineEdit_6.setText(randomline[2])
        self.ui.lineEdit_7.setText(randomline[3])
        self.ui.lineEdit_8.setText(randomline[4])
        YouVersion = [self.ui.lineEdit, self.ui.lineEdit_2, self.ui.lineEdit_3, self.ui.lineEdit_4]
        TrueVersion = [self.ui.lineEdit_5, self.ui.lineEdit_6, self.ui.lineEdit_7, self.ui.lineEdit_8]

        for i in YouVersion:
            for j in TrueVersion:
                if i.text() != j.text():
                    i.setStyleSheet("background-color: rgb(255, 0, 0);")
        # Если не использовать, то часть текста исчезнет.
        j.adjustSize()

    def keyPressEvent(self, e):
        q = str()
        if e.key() == QtCore.Qt.Key_1:
            q = self.ui.lineEdit_9.text()
            self.ui.lineEdit.setText(q)

        elif e.key() == QtCore.Qt.Key_2:
            q = self.ui.lineEdit_9.text()
            self.ui.lineEdit_2.setText(q)

        elif e.key() == QtCore.Qt.Key_3:
            q = self.ui.lineEdit_9.text()
            self.ui.lineEdit_3.setText(q)

        elif e.key() == QtCore.Qt.Key_4:
            q = self.ui.lineEdit_9.text()
            self.ui.lineEdit_4.setText(q)

app = QtWidgets.QApplication([])
application = mywindow()
application.show()
 
sys.exit(app.exec())