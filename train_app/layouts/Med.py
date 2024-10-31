# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Med.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_Med(object):
    def setupUi(self, Med):
        if not Med.objectName():
            Med.setObjectName(u"Med")
        Med.resize(181, 144)
        self.centralwidget = QWidget(Med)
        self.centralwidget.setObjectName(u"centralwidget")
        self.entry_id = QLineEdit(self.centralwidget)
        self.entry_id.setObjectName(u"entry_id")
        self.entry_id.setGeometry(QRect(30, 50, 113, 22))
        self.label_1 = QLabel(self.centralwidget)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(30, 10, 151, 31))
        self.but_ok = QPushButton(self.centralwidget)
        self.but_ok.setObjectName(u"but_ok")
        self.but_ok.setGeometry(QRect(40, 80, 93, 28))
        Med.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Med)
        self.statusbar.setObjectName(u"statusbar")
        Med.setStatusBar(self.statusbar)

        self.retranslateUi(Med)

        QMetaObject.connectSlotsByName(Med)
    # setupUi

    def retranslateUi(self, Med):
        Med.setWindowTitle(QCoreApplication.translate("Med", u"MainWindow", None))
        self.label_1.setText(QCoreApplication.translate("Med", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 id \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430", None))
        self.but_ok.setText(QCoreApplication.translate("Med", u"\u043e\u043a", None))
    # retranslateUi

