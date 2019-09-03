# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import math

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(471, 377)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        
        self.pushButton_LBD = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_LBD.setGeometry(QtCore.QRect(20, 60, 161, 41))
        self.pushButton_LBD.setObjectName("pushButton_LBD")
        self.pushButton_LBD.clicked.connect(self.listbangunDatar)
        
        self.pushButton_KBD = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_KBD.setGeometry(QtCore.QRect(20, 120, 161, 41))
        self.pushButton_KBD.setObjectName("pushButton_KBD")
        self.pushButton_KBD.clicked.connect(self.kelilingBangunDatar)

        self.comboBox_Menu = QtWidgets.QComboBox(self.centralWidget)
        self.comboBox_Menu.setGeometry(QtCore.QRect(20, 180, 161, 31))
        self.comboBox_Menu.setObjectName("comboBox_Menu")
        
        self.insert_Data1 = QtWidgets.QLineEdit(self.centralWidget)
        self.insert_Data1.setGeometry(QtCore.QRect(200, 80, 101, 25))
        self.insert_Data1.setObjectName("insert_Data1")
        
        self.label_insert_Data1 = QtWidgets.QLabel(self.centralWidget)
        self.label_insert_Data1.setGeometry(QtCore.QRect(200, 50, 68, 17))
        self.label_insert_Data1.setObjectName("label_insert_Data1")
        
        self.label_insert_Data2 = QtWidgets.QLabel(self.centralWidget)
        self.label_insert_Data2.setGeometry(QtCore.QRect(350, 50, 68, 17))
        self.label_insert_Data2.setObjectName("label_insert_Data2")
        
        self.insert_Data2 = QtWidgets.QLineEdit(self.centralWidget)
        self.insert_Data2.setGeometry(QtCore.QRect(350, 80, 101, 25))
        self.insert_Data2.setObjectName("insert_Data2")
        
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(10, 240, 461, 41))
        self.label_4.setObjectName("label_4")
        
        self.label_rumusTitle = QtWidgets.QLabel(self.centralWidget)
        self.label_rumusTitle.setGeometry(QtCore.QRect(310, 160, 68, 17))
        self.label_rumusTitle.setObjectName("label_rumusTitle")
        
        self.line = QtWidgets.QFrame(self.centralWidget)
        self.line.setGeometry(QtCore.QRect(190, 160, 20, 81))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralWidget)
        self.line_2.setGeometry(QtCore.QRect(200, 150, 271, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_rumus = QtWidgets.QLabel(self.centralWidget)
        self.label_rumus.setGeometry(QtCore.QRect(210, 200, 261, 17))
        self.label_rumus.setObjectName("label_rumus")
        self.pushButton_process = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_process.setGeometry(QtCore.QRect(280, 120, 90, 25))
        self.pushButton_process.setObjectName("pushButton_process")
        self.line_3 = QtWidgets.QFrame(self.centralWidget)
        self.line_3.setGeometry(QtCore.QRect(0, 230, 471, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_TitleApp = QtWidgets.QLabel(self.centralWidget)
        self.label_TitleApp.setGeometry(QtCore.QRect(10, 0, 451, 41))
        self.label_TitleApp.setObjectName("label_TitleApp")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(10, 310, 121, 17))
        self.label_2.setObjectName("label_2")
        self.line_4 = QtWidgets.QFrame(self.centralWidget)
        self.line_4.setGeometry(QtCore.QRect(0, 280, 621, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_LBD.setText(_translate("MainWindow", "Luas Bangun Datar"))
        self.pushButton_KBD.setText(_translate("MainWindow", "Keliling Bangun Datar"))
        self.label_insert_Data1.setText(_translate("MainWindow", ""))
        self.label_insert_Data2.setText(_translate("MainWindow", ""))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Hasil</span></p></body></htmlRumus"))
        self.label_rumusTitle.setText(_translate("MainWindow", "Rumus"))
        self.pushButton_process.setText(_translate("MainWindow", "PushButton"))
        self.label_TitleApp.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Tugas PBO </span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic;\">Bima Rizal Faisol</span></p></body></html>"))

        self.comboBox_Menu.currentTextChanged.connect(self.label)
    
    def listbangunDatar(self,):
        self.comboBox_Menu.clear()
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        bangunDatar = ['-- Pilih Luas --', 'Persegi', 'Persegi Panjang',
                       'Jajargenjang', 'Segitiga', 'Lingkaran', 'Trapesium', 'Layang-Layang']
        for i in range(len(bangunDatar)):
            self.comboBox_Menu.addItem("")
            self.comboBox_Menu.setItemText(
                i, _translate("MainWindow", bangunDatar[i]))

    def kelilingBangunDatar(self,):
        self.comboBox_Menu.clear()
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        keliling = ['-- Pilih Keliling --', 'K Persegi',
                    'K Persegi Panjang', 'K Jajargenjang']
        for i in range(len(keliling)):
            self.comboBox_Menu.addItem("")
            self.comboBox_Menu.setItemText(
                i, _translate("MainWindow", keliling[i]))

    def label(self, value):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        if self.label_4.clear() == None:
            null = ''
        if value == 'Persegi':
            self.label_insert_Data1.setText(_translate("MainWindow", "Sisi"))
            self.label_insert_Data2.setText(_translate("MainWindow", "Sisi"))
            self.label_rumus.setText(_translate("MainWindow", "Sisi x Sisi"))
            self.pushButton_process.clicked.connect(self.luasPersegi)
            self.label_4.setText(_translate(
                "MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Hasil : {}</span></p></body></html>".format(null)))
        elif value == 'Persegi Panjang':
            self.label_insert_Data1.setText(
                _translate("MainWindow", "Panjang"))
            self.label_insert_Data2.setText(_translate("MainWindow", "Lebar"))
            self.label_rumus.setText(_translate(
                "MainWindow", "Panjang x Lebar"))
            self.pushButton_process.clicked.connect(self.luasPersegiPanjang)
            self.label_4.setText(_translate(
                "MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Hasil : {}</span></p></body></html>".format(null)))
        elif value == 'Jajargenjang':
            self.label_insert_Data1.setText(_translate("MainWindow", "Alas"))
            self.label_insert_Data2.setText(_translate("MainWindow", "Tinggi"))
            self.label_rumus.setText(_translate("MainWindow", "Alas x Tinggi"))
            self.pushButton_process.clicked.connect(self.luasJajargenjang)
            self.label_4.setText(_translate(
                "MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Hasil : {}</span></p></body></html>".format(null)))
        elif value == 'Segitiga':
            self.label_insert_Data1.setText(_translate("MainWindow", "Alas"))
            self.label_insert_Data2.setText(_translate("MainWindow", "Tinggi"))
            self.label_rumus.setText(_translate(
                "MainWindow", "1/2 x Alas x Tinggi"))
            self.pushButton_process.clicked.connect(self.luasSegitiga)
            self.label_4.setText(_translate(
                "MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Hasil : {}</span></p></body></html>".format(null)))
        elif value == 'Lingkaran':
            self.label_insert_Data1.setText(_translate("MainWindow", "r**2"))
            self.label_insert_Data2.setText(_translate("MainWindow", ""))
            self.label_rumus.setText(_translate("MainWindow", "πr**2 "))
            self.pushButton_process.clicked.connect(self.luasLingkaran)
            self.label_4.setText(_translate(
                "MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Hasil : {}</span></p></body></html>".format(null)))
        elif value == 'Trapesium':
            self.label_insert_Data1.setText(
                _translate("MainWindow", "Panjang sisi sejajar"))
            self.label_insert_Data2.setText(_translate("MainWindow", "Tinggi"))
            self.label_rumus.setText(_translate(
                "MainWindow", "1/2 x Panjang sisi sejajar x Tinggi"))
            self.pushButton_process.clicked.connect(self.luasTrapesium)
            self.label_4.setText(_translate(
                "MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Hasil : {}</span></p></body></html>".format(null)))
        elif value == 'Layang-Layang':
            self.label_insert_Data1.setText(_translate("MainWindow", "alas"))
            self.label_insert_Data2.setText(_translate("MainWindow", "Tinggi"))
            self.label_rumus.setText(_translate("MainWindow", "1/2 x d1 x d2"))
            self.pushButton_process.clicked.connect(self.luasLayangLayang)
            self.label_4.setText(_translate(
                "MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Hasil : {}</span></p></body></html>".format(null)))
        elif value == 'K Persegi':
            self.label_insert_Data1.setText(_translate("MainWindow", "Sisi"))
            self.label_insert_Data2.setText(_translate("MainWindow", ""))
            self.label_rumus.setText(_translate("MainWindow", "4 x S"))
            self.pushButton_process.clicked.connect(self.kelilingPersegi)
            self.label_4.setText(_translate(
                "MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Hasil : {}</span></p></body></html>".format(null)))
        elif value == 'K Persegi Panjang':
            self.label_insert_Data1.setText(
                _translate("MainWindow", "Panjang"))
            self.label_insert_Data2.setText(_translate("MainWindow", "Lebar"))
            self.label_rumus.setText(_translate("MainWindow", "2 x (P + L)"))
            self.pushButton_process.clicked.connect(
                self.kelilingPersegiPanjang)
            self.label_4.setText(_translate(
                "MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Hasil : {}</span></p></body></html>".format(null)))
        elif value == 'K Jajargenjang':
            self.label_insert_Data1.setText(_translate("MainWindow", "Sisi"))
            self.label_insert_Data2.setText(_translate("MainWindow", ""))
            self.label_rumus.setText(_translate("MainWindow", "4 x S"))
            self.pushButton_process.clicked.connect(self.kelilingJajargenjang)
            self.label_4.setText(_translate(
                "MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Hasil : {}</span></p></body></html>".format(null)))

    def luasPersegi(self):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        hasil = float(self.insert_Data1.text())*float(self.insert_Data2.text())
        self.label_4.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Hasil : {}</span></p></body></html>".format(hasil)))

    def luasPersegiPanjang(self):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        hasil = float(self.insert_Data1.text())*float(self.insert_Data2.text())
        self.label_4.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Hasil : {}</span></p></body></html>".format(hasil)))

    def luasJajargenjang(self):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        hasil = float(self.insert_Data1.text())*float(self.insert_Data2.text())
        self.label_4.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Hasil : {}</span></p></body></html>".format(hasil)))

    def luasSegitiga(self):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        hasil = 1/2*float(self.insert_Data1.text()) * \
            float(self.insert_Data2.text())
        self.label_4.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Hasil : {}</span></p></body></html>".format(hasil)))

    def luasLingkaran(self):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        hasil = math.pi*float(self.insert_Data1.text())**2
        self.label_4.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Hasil : {}</span></p></body></html>".format(hasil)))

    def luasTrapesium(self):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        hasil = 1/2*float(self.insert_Data1.text()) * \
            float(self.insert_Data2.text())
        self.label_4.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Hasil : {}</span></p></body></html>".format(hasil)))

    def luasLayangLayang(self):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        hasil = 1/2*float(self.insert_Data1.text()) * \
            float(self.insert_Data2.text())
        self.label_4.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Hasil : {}</span></p></body></html>".format(hasil)))

    def kelilingPersegi(self):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        hasil = 4*float(self.insert_Data1.text())
        self.label_4.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Hasil : {}</span></p></body></html>".format(hasil)))

    def kelilingPersegiPanjang(self):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        hasil = 2*(float(self.insert_Data1.text()) +
                   float(self.insert_Data2.text()))
        self.label_4.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Hasil : {}</span></p></body></html>".format(hasil)))

    def kelilingJajargenjang(self):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        hasil = 4*(float(self.insert_Data1.text()))
        self.label_4.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Hasil : {}</span></p></body></html>".format(hasil)))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

