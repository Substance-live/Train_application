# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Profile.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(507, 300)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_photo = QLabel(self.centralwidget)
        self.label_photo.setObjectName(u"label_photo")
        self.label_photo.setGeometry(QRect(30, 30, 111, 101))
        font = QFont()
        font.setPointSize(19)
        self.label_photo.setFont(font)
        self.label_photo.setLayoutDirection(Qt.LeftToRight)
        self.label_photo.setAlignment(Qt.AlignCenter)
        self.label_user = QLabel(self.centralwidget)
        self.label_user.setObjectName(u"label_user")
        self.label_user.setGeometry(QRect(190, 60, 161, 51))
        self.label_data = QLabel(self.centralwidget)
        self.label_data.setObjectName(u"label_data")
        self.label_data.setGeometry(QRect(190, 110, 141, 41))
        self.but_view_1 = QPushButton(self.centralwidget)
        self.but_view_1.setObjectName(u"but_view_1")
        self.but_view_1.setGeometry(QRect(130, 190, 93, 28))
        self.but_view_2 = QPushButton(self.centralwidget)
        self.but_view_2.setObjectName(u"but_view_2")
        self.but_view_2.setGeometry(QRect(240, 190, 93, 28))
        self.but_task_1 = QPushButton(self.centralwidget)
        self.but_task_1.setObjectName(u"but_task_1")
        self.but_task_1.setGeometry(QRect(360, 190, 93, 28))
        self.but_notification = QPushButton(self.centralwidget)
        self.but_notification.setObjectName(u"but_notification")
        self.but_notification.setGeometry(QRect(470, 10, 31, 28))
        self.but_logout = QPushButton(self.centralwidget)
        self.but_logout.setObjectName(u"but_logout")
        self.but_logout.setGeometry(QRect(442, 260, 51, 28))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_photo.setText(QCoreApplication.translate("MainWindow", u"\u0424\u041e\u0422\u041e", None))
        self.label_user.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c:******", None))
        self.label_data.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f:******", None))
        self.but_view_1.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 1", None))
        self.but_view_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 2", None))
        self.but_task_1.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0440\u043e\u0441 1", None))
        self.but_notification.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.but_logout.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
    # retranslateUi

