# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StaffTable.ui'
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

class Ui_StaffTable(object):
    def setupUi(self, StaffTable):
        if not StaffTable.objectName():
            StaffTable.setObjectName(u"StaffTable")
        StaffTable.resize(715, 460)
        self.table = QTableWidget(StaffTable)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(20, 20, 671, 331))
        self.but_reload = QPushButton(StaffTable)
        self.but_reload.setObjectName(u"but_reload")
        self.but_reload.setGeometry(QRect(300, 380, 261, 51))
        self.but_return = QPushButton(StaffTable)
        self.but_return.setObjectName(u"but_return")
        self.but_return.setGeometry(QRect(580, 380, 111, 51))
        self.comboBox_kurs = QComboBox(StaffTable)
        self.comboBox_kurs.setObjectName(u"comboBox_kurs")
        self.comboBox_kurs.setGeometry(QRect(32, 360, 101, 22))
        self.comboBox_category = QComboBox(StaffTable)
        self.comboBox_category.setObjectName(u"comboBox_category")
        self.comboBox_category.setGeometry(QRect(32, 390, 101, 22))
        self.label_kurs = QLabel(StaffTable)
        self.label_kurs.setObjectName(u"label_kurs")
        self.label_kurs.setGeometry(QRect(170, 360, 81, 20))
        self.label_category = QLabel(StaffTable)
        self.label_category.setObjectName(u"label_category")
        self.label_category.setGeometry(QRect(154, 390, 91, 20))
        self.label_category_2 = QLabel(StaffTable)
        self.label_category_2.setObjectName(u"label_category_2")
        self.label_category_2.setGeometry(QRect(184, 420, 61, 20))
        self.lineEdit = QLineEdit(StaffTable)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 420, 101, 22))

        self.retranslateUi(StaffTable)

        QMetaObject.connectSlotsByName(StaffTable)
    # setupUi

    def retranslateUi(self, StaffTable):
        StaffTable.setWindowTitle(QCoreApplication.translate("StaffTable", u"Form", None))
        self.but_reload.setText(QCoreApplication.translate("StaffTable", u"\u0421\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.but_return.setText(QCoreApplication.translate("StaffTable", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.label_kurs.setText(QCoreApplication.translate("StaffTable", u"\u0422\u0438\u043f \u0431\u0440\u0438\u0433\u0430\u0434\u044b", None))
        self.label_category.setText(QCoreApplication.translate("StaffTable", u"\u0413\u043b\u0430\u0432\u0430 \u0431\u0440\u0438\u0433\u0430\u0434\u044b", None))
        self.label_category_2.setText(QCoreApplication.translate("StaffTable", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
    # retranslateUi

