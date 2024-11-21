# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mail_message.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_mail_message(object):
    def setupUi(self, mail_message):
        if not mail_message.objectName():
            mail_message.setObjectName(u"mail_message")
        mail_message.resize(331, 112)
        self.widget = QWidget(mail_message)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 10, 300, 81))
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.pushButton)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.pushButton_2)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.lineEdit)


        self.retranslateUi(mail_message)

        QMetaObject.connectSlotsByName(mail_message)
    # setupUi

    def retranslateUi(self, mail_message):
        mail_message.setWindowTitle(QCoreApplication.translate("mail_message", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("mail_message", u"\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u043e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u043d\u043e \u043d\u0430 \u0432\u0430\u0448\u0443 \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u0443\u044e \u043f\u043e\u0447\u0442\u0443", None))
        self.pushButton.setText(QCoreApplication.translate("mail_message", u"\u041e\u043a", None))
        self.pushButton_2.setText(QCoreApplication.translate("mail_message", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u043d\u043e\u0432\u044b\u0439 \u043a\u043e\u0434", None))
    # retranslateUi

