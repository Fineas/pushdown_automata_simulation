# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'get_machine_info.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pd_aut import *

class Ui_Dialog2(object):
    def setupUi2(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 600)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 20, 231, 41))
        self.label.setAutoFillBackground(False)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setPixmap(QtGui.QPixmap("frame.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(410, 400, 161, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 24, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 24, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 24, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButton.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.getData)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(40, 70, 231, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 180, 231, 51))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(40, 290, 231, 51))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(300, 290, 271, 51))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(40, 400, 171, 51))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.background = QtWidgets.QLabel(Dialog)
        self.background.setGeometry(QtCore.QRect(0, 0, 601, 601))
        self.background.setAutoFillBackground(False)
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("frame.png"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(620, 640, 241, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 24, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 24, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 24, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButton_2.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setDefault(True)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_9 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_9.setGeometry(QtCore.QRect(690, 300, 231, 51))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_10.setGeometry(QtCore.QRect(690, 370, 231, 51))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 130, 231, 41))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 240, 231, 41))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(300, 20, 281, 41))
        self.label_4.setAutoFillBackground(False)
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(300, 240, 271, 41))
        self.label_5.setAutoFillBackground(False)
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.lineEdit_7 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_7.setGeometry(QtCore.QRect(230, 400, 171, 51))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 350, 371, 41))
        self.label_6.setAutoFillBackground(False)
        self.label_6.setTextFormat(QtCore.Qt.RichText)
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(300, 70, 271, 161))
        self.plainTextEdit.setMaximumBlockCount(9)
        self.plainTextEdit.setPlaceholderText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.background.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_5.raise_()
        self.lineEdit_6.raise_()
        self.pushButton_2.raise_()
        self.lineEdit_9.raise_()
        self.lineEdit_10.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.lineEdit_7.raise_()
        self.label_6.raise_()
        self.plainTextEdit.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def getData(self):
        '''
        Parse Input
        '''
        states = self.lineEdit.text().split(',')
        print("States=",states)
        symbols = self.lineEdit_2.text().split(',')
        print("Symbols=",symbols)
        stack_symbols = self.lineEdit_3.text().split(',')
        print("Stack Symbols=",stack_symbols)
        final_states = self.lineEdit_5.text()
        print("Final States=",final_states)
        start_state = self.lineEdit_6.text()
        print("Start State=",start_state)
        stack_start = self.lineEdit_7.text()
        print("Stack Start=",stack_start)
        transitions = self.plainTextEdit.toPlainText().replace('epsilon','ε').split('\n')
        for i in range(len(transitions)):
            transitions[i] = transitions[i].split(':')
            for j in range(1,len(transitions[i])):
                transitions[i][j] = transitions[i][j].split(',')
        print("Transitions=",transitions)

        final_trans = dict()
        for i in range(len(transitions)):
            a = []
            for j in range(1,len(transitions[i])):
                a.append(transitions[i][j])
            final_trans[transitions[i][0]] = a
        print("final trans=",final_trans)

        '''
        Start Machine
        '''
        
        input1 = 'ababbaba'
        input2 = 'abababab'
        input3 = 'aaabbbc'

        simulation = pd_automata(input1,
                            states,
                            symbols,
                            stack_symbols,
                            final_trans,
                            start_state,
                            stack_start,
                            final_states,
                            [[start_state,0]])
        simulation.start_automata()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Simulation"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:xx-large; font-weight:600;\">SET OF STATES</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "SIMULATE"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "ex: Q1, Q2, Q3, ..."))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "ex: a, b, c, d, ..."))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog", "ex: z0, a, b, c, ..."))
        self.lineEdit_5.setPlaceholderText(_translate("Dialog", "ex: Q4, Q5 ..."))
        self.lineEdit_6.setPlaceholderText(_translate("Dialog", "ex: S"))
        self.pushButton_2.setText(_translate("Dialog", "SIMULATE"))
        self.lineEdit_9.setPlaceholderText(_translate("Dialog", "ex: z0, a, b, c, ..."))
        self.lineEdit_10.setPlaceholderText(_translate("Dialog", "ex: z0, a, b, c, ..."))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:xx-large; font-weight:600;\">INPUT ALPHABET</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:xx-large; font-weight:600;\">STACK SYMBOLS</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:xx-large; font-weight:600;\">TRANSITION FUNCTION</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:xx-large; font-weight:600;\">ACCEPTING STATES</span></p></body></html>"))
        self.lineEdit_7.setPlaceholderText(_translate("Dialog", "ex: z0"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:xx-large; font-weight:600;\">INITIAL STATE | STACK SYMBOL</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
