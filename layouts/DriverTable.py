# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DriverTable.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_DriverTable(object):
    def setupUi(self, DriverTable):
        if not DriverTable.objectName():
            DriverTable.setObjectName(u"DriverTable")
        DriverTable.resize(715, 434)
        self.table = QTableWidget(DriverTable)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(20, 20, 671, 331))
        self.but_reload = QPushButton(DriverTable)
        self.but_reload.setObjectName(u"but_reload")
        self.but_reload.setGeometry(QRect(300, 370, 261, 51))
        self.but_return = QPushButton(DriverTable)
        self.but_return.setObjectName(u"but_return")
        self.but_return.setGeometry(QRect(580, 370, 111, 51))
        self.comboBox_kurs = QComboBox(DriverTable)
        self.comboBox_kurs.setObjectName(u"comboBox_kurs")
        self.comboBox_kurs.setGeometry(QRect(32, 360, 101, 22))
        self.label_kurs = QLabel(DriverTable)
        self.label_kurs.setObjectName(u"label_kurs")
        self.label_kurs.setGeometry(QRect(170, 360, 81, 20))
        self.label_category_2 = QLabel(DriverTable)
        self.label_category_2.setObjectName(u"label_category_2")
        self.label_category_2.setGeometry(QRect(170, 390, 61, 20))
        self.lineEdit = QLineEdit(DriverTable)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 390, 101, 22))

        self.retranslateUi(DriverTable)

        QMetaObject.connectSlotsByName(DriverTable)
    # setupUi

    def retranslateUi(self, DriverTable):
        DriverTable.setWindowTitle(QCoreApplication.translate("DriverTable", u"Form", None))
        self.but_reload.setText(QCoreApplication.translate("DriverTable", u"\u0421\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.but_return.setText(QCoreApplication.translate("DriverTable", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.label_kurs.setText(QCoreApplication.translate("DriverTable", u"\u0422\u0438\u043f \u043f\u043e\u0435\u0437\u0434\u0430", None))
        self.label_category_2.setText(QCoreApplication.translate("DriverTable", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
    # retranslateUi

