# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import imgs

class Ui_MainWindow(object):
    def table_window(self,data):

        from table import  Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window,data)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(879, 601)
        MainWindow.setMinimumSize(QtCore.QSize(879, 601))
        MainWindow.setMaximumSize(QtCore.QSize(879, 601))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setGeometry(QtCore.QRect(0, 0, 921, 621))
        self.main_frame.setStyleSheet("background-color: #0a1931;\n"
"font: 14pt \".AppleSystemUIFont\";\n"
"border-radius:5px")
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.comboBox = QtWidgets.QComboBox(self.main_frame)
        self.comboBox.setGeometry(QtCore.QRect(270, 40, 241, 41))
        self.comboBox.setStyleSheet("background-color:#fff;\n"
"font: 14pt \".AppleSystemUIFont\";\n"
"border-radius:5px;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.go_btn = QtWidgets.QPushButton(self.main_frame)
        self.go_btn.setGeometry(QtCore.QRect(560, 50, 81, 31))
        self.go_btn.setStyleSheet("#go_btn{\n"
"background-color: rgb(219,68,55) ;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 57 14pt \"Google Sans\";\n"
"border-radius:7px;\n"
"}\n"
"#go_btn:hover{\n"
"background-color:#ffc947;\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.go_btn.setObjectName("go_btn")
        self.stackedWidget = QtWidgets.QStackedWidget(self.main_frame)
        self.stackedWidget.setGeometry(QtCore.QRect(60, 110, 771, 461))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.category_frame = QtWidgets.QFrame(self.page)
        self.category_frame.setGeometry(QtCore.QRect(50, 50, 191, 341))
        self.category_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.category_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.category_frame.setObjectName("category_frame")
        self.label = QtWidgets.QLabel(self.category_frame)
        self.label.setGeometry(QtCore.QRect(10, 0, 181, 291))
        self.label.setStyleSheet("background-image: url(:/newPrefix/images/thehundred.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.action_btn = QtWidgets.QPushButton(self.category_frame)
        self.action_btn.setGeometry(QtCore.QRect(20, 310, 161, 26))
        self.action_btn.setStyleSheet("#action_btn{\n"
"background-color: rgb(219,68,55);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 57 14pt \"Google Sans\";\n"
"border-radius:7px;\n"
"}\n"
"#action_btn:hover{\n"
"background-color:#ffc947;\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.action_btn.setObjectName("action_btn")
        self.category_frame_3 = QtWidgets.QFrame(self.page)
        self.category_frame_3.setGeometry(QtCore.QRect(530, 50, 191, 341))
        self.category_frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.category_frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.category_frame_3.setObjectName("category_frame_3")
        self.label_4 = QtWidgets.QLabel(self.category_frame_3)
        self.label_4.setGeometry(QtCore.QRect(10, 0, 181, 291))
        self.label_4.setStyleSheet("background-image: url(:/newPrefix/images/friends.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.sitcom_btn = QtWidgets.QPushButton(self.category_frame_3)
        self.sitcom_btn.setGeometry(QtCore.QRect(20, 310, 161, 26))
        self.sitcom_btn.setStyleSheet("#sitcom_btn{\n"
"background-color: rgb(219,68,55);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 57 14pt \"Google Sans\";\n"
"border-radius:7px;\n"
"}\n"
"#sitcom_btn:hover{\n"
"background-color:#ffc947;\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.sitcom_btn.setObjectName("sitcom_btn")
        self.category_frame_2 = QtWidgets.QFrame(self.page)
        self.category_frame_2.setGeometry(QtCore.QRect(290, 50, 191, 341))
        self.category_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.category_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.category_frame_2.setObjectName("category_frame_2")
        self.label_2 = QtWidgets.QLabel(self.category_frame_2)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 181, 291))
        self.label_2.setStyleSheet("background-image: url(:/newPrefix/images/strangerthings.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.sci_btn = QtWidgets.QPushButton(self.category_frame_2)
        self.sci_btn.setGeometry(QtCore.QRect(20, 310, 161, 26))
        self.sci_btn.setStyleSheet("#sci_btn{\n"
"background-color: rgb(219,68,55);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 57 14pt \"Google Sans\";\n"
"border-radius:7px;\n"
"}\n"
"#sci_btn:hover{\n"
"background-color:#ffc947;\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.sci_btn.setObjectName("sci_btn")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.category_frame_5 = QtWidgets.QFrame(self.page_2)
        self.category_frame_5.setGeometry(QtCore.QRect(530, 50, 191, 341))
        self.category_frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.category_frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.category_frame_5.setObjectName("category_frame_5")
        self.label_6 = QtWidgets.QLabel(self.category_frame_5)
        self.label_6.setGeometry(QtCore.QRect(10, 0, 181, 291))
        self.label_6.setStyleSheet("background-image: url(:/newPrefix/images/siliconvalley.png);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.sitcom_btn_2 = QtWidgets.QPushButton(self.category_frame_5)
        self.sitcom_btn_2.setGeometry(QtCore.QRect(20, 310, 161, 26))
        self.sitcom_btn_2.setStyleSheet("#sitcom_btn_2{\n"
"background-color: rgb(219,68,55);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 57 14pt \"Google Sans\";\n"
"border-radius:7px;\n"
"}\n"
"#sitcom_btn_2:hover{\n"
"background-color:#ffc947;\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.sitcom_btn_2.setObjectName("sitcom_btn_2")
        self.category_frame_4 = QtWidgets.QFrame(self.page_2)
        self.category_frame_4.setGeometry(QtCore.QRect(50, 50, 191, 341))
        self.category_frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.category_frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.category_frame_4.setObjectName("category_frame_4")
        self.label_5 = QtWidgets.QLabel(self.category_frame_4)
        self.label_5.setGeometry(QtCore.QRect(10, 0, 181, 291))
        self.label_5.setStyleSheet("background-image: url(:/newPrefix/images/legacies.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.action_btn_2 = QtWidgets.QPushButton(self.category_frame_4)
        self.action_btn_2.setGeometry(QtCore.QRect(20, 310, 161, 26))
        self.action_btn_2.setStyleSheet("#action_btn_2{\n"
"background-color: rgb(219,68,55);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 57 14pt \"Google Sans\";\n"
"border-radius:7px;\n"
"}\n"
"#action_btn_2:hover{\n"
"background-color:#ffc947;\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.action_btn_2.setObjectName("action_btn_2")
        self.category_frame_6 = QtWidgets.QFrame(self.page_2)
        self.category_frame_6.setGeometry(QtCore.QRect(290, 50, 191, 341))
        self.category_frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.category_frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.category_frame_6.setObjectName("category_frame_6")
        self.label_7 = QtWidgets.QLabel(self.category_frame_6)
        self.label_7.setGeometry(QtCore.QRect(10, 0, 181, 291))
        self.label_7.setStyleSheet("background-image: url(:/newPrefix/images/strangerthings.png);\n"
"background-image: url(:/newPrefix/images/titans.png);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.sci_btn_3 = QtWidgets.QPushButton(self.category_frame_6)
        self.sci_btn_3.setGeometry(QtCore.QRect(20, 310, 161, 26))
        self.sci_btn_3.setStyleSheet("#sci_btn_3{\n"
"background-color: rgb(219,68,55);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 57 14pt \"Google Sans\";\n"
"border-radius:7px;\n"
"}\n"
"#sci_btn_3:hover{\n"
"background-color:#ffc947;\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.sci_btn_3.setObjectName("sci_btn_3")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.category_frame_7 = QtWidgets.QFrame(self.page_3)
        self.category_frame_7.setGeometry(QtCore.QRect(300, 50, 191, 341))
        self.category_frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.category_frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.category_frame_7.setObjectName("category_frame_7")
        self.label_8 = QtWidgets.QLabel(self.category_frame_7)
        self.label_8.setGeometry(QtCore.QRect(10, 0, 181, 291))
        self.label_8.setStyleSheet("background-image: url(:/newPrefix/images/loki.png);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.sci_btn_4 = QtWidgets.QPushButton(self.category_frame_7)
        self.sci_btn_4.setGeometry(QtCore.QRect(20, 310, 161, 26))
        self.sci_btn_4.setStyleSheet("#sci_btn_4{\n"
"background-color: rgb(219,68,55);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 57 14pt \"Google Sans\";\n"
"border-radius:7px;\n"
"}\n"
"#sci_btn_4:hover{\n"
"background-color:#ffc947;\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.sci_btn_4.setObjectName("sci_btn_4")
        self.category_frame_8 = QtWidgets.QFrame(self.page_3)
        self.category_frame_8.setGeometry(QtCore.QRect(540, 50, 191, 341))
        self.category_frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.category_frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.category_frame_8.setObjectName("category_frame_8")
        self.label_9 = QtWidgets.QLabel(self.category_frame_8)
        self.label_9.setGeometry(QtCore.QRect(10, 0, 181, 291))
        self.label_9.setStyleSheet("background-image: url(:/newPrefix/images/wandavision.png);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.sitcom_btn_3 = QtWidgets.QPushButton(self.category_frame_8)
        self.sitcom_btn_3.setGeometry(QtCore.QRect(20, 310, 161, 26))
        self.sitcom_btn_3.setStyleSheet("#sitcom_btn_3{\n"
"background-color: rgb(219,68,55);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 57 14pt \"Google Sans\";\n"
"border-radius:7px;\n"
"}\n"
"#sitcom_btn_3:hover{\n"
"background-color:#ffc947;\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.sitcom_btn_3.setObjectName("sitcom_btn_3")
        self.category_frame_9 = QtWidgets.QFrame(self.page_3)
        self.category_frame_9.setGeometry(QtCore.QRect(60, 50, 191, 341))
        self.category_frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.category_frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.category_frame_9.setObjectName("category_frame_9")
        self.label_10 = QtWidgets.QLabel(self.category_frame_9)
        self.label_10.setGeometry(QtCore.QRect(10, 0, 181, 291))
        self.label_10.setStyleSheet("background-image: url(:/newPrefix/images/legacies.png);\n"
"background-image: url(:/newPrefix/images/falcon.png);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.action_btn_3 = QtWidgets.QPushButton(self.category_frame_9)
        self.action_btn_3.setGeometry(QtCore.QRect(20, 310, 161, 26))
        self.action_btn_3.setStyleSheet("#action_btn_3{\n"
"background-color: rgb(219,68,55);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 57 14pt \"Google Sans\";\n"
"border-radius:7px;\n"
"}\n"
"#action_btn_3:hover{\n"
"background-color:#ffc947;\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.action_btn_3.setObjectName("action_btn_3")
        self.stackedWidget.addWidget(self.page_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.go_btn.clicked.connect(self.change_page)

        from TvshowsData import get_Netflix_action_data,get_HBO_action_data,get_Disney_action_data,get_Netflix_scifi_data,get_HBO_scifi_data,get_Disney_scifi_data,get_Netflix_sitcom_data,get_HBO_sitcom_data,get_Disney_sitcom_data

        self.action_btn.clicked.connect(lambda:self.table_window(get_Netflix_action_data()))
        self.action_btn_2.clicked.connect(lambda:self.table_window(get_HBO_action_data()))
        self.action_btn_3.clicked.connect(lambda:self.table_window(get_Disney_action_data()))

        self.sci_btn.clicked.connect(lambda:self.table_window(get_Netflix_scifi_data()))
        self.sci_btn_3.clicked.connect(lambda:self.table_window(get_HBO_scifi_data()))
        self.sci_btn_4.clicked.connect(lambda:self.table_window(get_Disney_scifi_data()))

        self.sitcom_btn.clicked.connect(lambda:self.table_window(get_Netflix_sitcom_data()))
        self.sitcom_btn_2.clicked.connect(lambda:self.table_window(get_HBO_sitcom_data()))
        self.sitcom_btn_3.clicked.connect(lambda:self.table_window(get_Disney_sitcom_data()))
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Netflix"))
        self.comboBox.setItemText(1, _translate("MainWindow", "HBO"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Disney+"))
        self.go_btn.setText(_translate("MainWindow", "Go"))
        self.action_btn.setText(_translate("MainWindow", "Action and Adventure"))
        self.sitcom_btn.setText(_translate("MainWindow", "Sitcom"))
        self.sci_btn.setText(_translate("MainWindow", "Sci Fi"))
        self.sitcom_btn_2.setText(_translate("MainWindow", "Comedy"))
        self.action_btn_2.setText(_translate("MainWindow", "Action and Adventure"))
        self.sci_btn_3.setText(_translate("MainWindow", "Sci Fi"))
        self.sci_btn_4.setText(_translate("MainWindow", "Sci Fi"))
        self.sitcom_btn_3.setText(_translate("MainWindow", "Sitcom"))
        self.action_btn_3.setText(_translate("MainWindow", "Action and Adventure"))


    def change_page(self):
            current_combo = self.comboBox.currentIndex()
            self.stackedWidget.setCurrentIndex(current_combo)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
