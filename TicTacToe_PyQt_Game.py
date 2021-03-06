# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tictactoe-pyqt.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(580, 558)
        MainWindow.setWindowOpacity(20.0)
        MainWindow.setToolTipDuration(-1)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.l1 = QtWidgets.QLabel(self.centralwidget)
        self.l1.setGeometry(QtCore.QRect(50, 210, 21, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(28)

        font.setWeight(75)
        self.l1.setFont(font)
        self.l1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.l1.setStyleSheet("border-color: rgb(85, 0, 255);")
        self.l1.setObjectName("l1")
        self.b3 = QtWidgets.QPushButton(self.centralwidget)
        self.b3.setGeometry(QtCore.QRect(340, 80, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.b3.setFont(font)
        self.b3.setText("")
        self.b3.setObjectName("b3")
        self.b5 = QtWidgets.QPushButton(self.centralwidget)
        self.b5.setGeometry(QtCore.QRect(240, 180, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.b5.setFont(font)
        self.b5.setText("")
        self.b5.setObjectName("b5")
        self.b4 = QtWidgets.QPushButton(self.centralwidget)
        self.b4.setGeometry(QtCore.QRect(140, 180, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.b4.setFont(font)
        self.b4.setText("")
        self.b4.setObjectName("b4")
        self.b6 = QtWidgets.QPushButton(self.centralwidget)
        self.b6.setGeometry(QtCore.QRect(340, 180, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.b6.setFont(font)
        self.b6.setText("")
        self.b6.setObjectName("b6")
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(140, 80, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.b1.setFont(font)
        self.b1.setText("")
        self.b1.setObjectName("b1")
        self.b2 = QtWidgets.QPushButton(self.centralwidget)
        self.b2.setGeometry(QtCore.QRect(240, 80, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.b2.setFont(font)
        self.b2.setText("")
        self.b2.setObjectName("b2")
        self.b7 = QtWidgets.QPushButton(self.centralwidget)
        self.b7.setGeometry(QtCore.QRect(140, 280, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.b7.setFont(font)
        self.b7.setText("")
        self.b7.setObjectName("b7")
        self.b8 = QtWidgets.QPushButton(self.centralwidget)
        self.b8.setGeometry(QtCore.QRect(240, 280, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.b8.setFont(font)
        self.b8.setText("")
        self.b8.setObjectName("b8")
        self.b9 = QtWidgets.QPushButton(self.centralwidget)
        self.b9.setGeometry(QtCore.QRect(340, 280, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.b9.setFont(font)
        self.b9.setText("")
        self.b9.setObjectName("b9")
        self.l2 = QtWidgets.QPushButton(self.centralwidget)
        self.l2.setGeometry(QtCore.QRect(240, 400, 101, 41))
        self.l2.setObjectName("l2")
        self.l3 = QtWidgets.QPushButton(self.centralwidget)
        self.l3.setGeometry(QtCore.QRect(240, 460, 101, 41))
        self.l3.setObjectName("l3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 20, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 580, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.blist = [
            self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7,
            self.b8, self.b9
        ]
        self.c = 0

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GuguGaga"))
        self.l1.setText(_translate("MainWindow", ""))
        self.l2.setText(_translate("MainWindow", "START"))
        self.l3.setText(_translate("MainWindow", "RESET"))
        self.label.setText(_translate("MainWindow", "TicTacToe"))

    def user_input(self):
        self.l1.setText("X")
        self.l1.adjustSize()
        self.b1.clicked.connect(lambda: self.click_status(self.b1))
        self.b2.clicked.connect(lambda: self.click_status(self.b2))
        self.b3.clicked.connect(lambda: self.click_status(self.b3))
        self.b4.clicked.connect(lambda: self.click_status(self.b4))
        self.b5.clicked.connect(lambda: self.click_status(self.b5))
        self.b6.clicked.connect(lambda: self.click_status(self.b6))
        self.b7.clicked.connect(lambda: self.click_status(self.b7))
        self.b8.clicked.connect(lambda: self.click_status(self.b8))
        self.b9.clicked.connect(lambda: self.click_status(self.b9))

    def click_status(self, b):

        if self.c % 2 == 0:
            ch = "X"
            b.setText(ch)
            self.l1.setText("O")
            self.l1.adjustSize()
            self.c = self.c + 1
            if self.check(self.blist, ch) == 1:
                self.label.setText("X won")
                self.label.adjustSize()
                self.setbtn()
                self.l3.clicked.connect(self.reset)
        elif self.c % 2 != 0:
            ch = "O"
            b.setText(ch)
            self.l1.setText("X")
            self.l1.adjustSize()
            self.c = self.c + 1
            if self.check(self.blist, ch) == 1:
                self.label.setText("O won")
                self.label.adjustSize()
                self.setbtn()
                self.l3.clicked.connect(self.reset)
        elif self.c == 9:
            self.l1.setText("Its a TIE")
            self.setbtn()
            self.l3.clicked.connect(self.reset)

    def setbtn(self):
        for i in range(0, 9):
            self.blist[i].setEnabled(False)

    def check(self, b, ch):
        if ((b[0].text() == b[1].text() == b[2].text() == ch)
                or (b[3].text() == b[4].text() == b[5].text() == ch)
                or (b[6].text() == b[7].text() == b[8].text() == ch)
                or (b[0].text() == b[4].text() == b[8].text() == ch)
                or (b[6].text() == b[4].text() == b[2].text() == ch)
                or (b[0].text() == b[3].text() == b[6].text() == ch)
                or (b[1].text() == b[4].text() == b[7].text() == ch)
                or (b[2].text() == b[5].text() == b[8].text() == ch)):
            return 1
        else:
            return 0

    def start(self):
        self.l2.clicked.connect(self.user_input)

    def reset(self):
        for i in range(0, 9):
            self.blist[i].setEnabled(True)
            self.blist[i].setText("")
        self.l1.setText("")
        self.label.setText("TicTacToe")
        self.label.adjustSize()
        self.c = 0
        self.l2.clicked.connect(self.user_input)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.start()
    sys.exit(app.exec_())
