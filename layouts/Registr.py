# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Registr.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_Registr(object):
    def setupUi(self, Registr):
        if not Registr.objectName():
            Registr.setObjectName(u"Registr")
        Registr.resize(417, 386)
        self.centralwidget = QWidget(Registr)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(21, 21, 381, 341))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_image = QLabel(self.layoutWidget)
        self.label_image.setObjectName(u"label_image")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_image.sizePolicy().hasHeightForWidth())
        self.label_image.setSizePolicy(sizePolicy)
        self.label_image.setMinimumSize(QSize(0, 104))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        self.label_image.setFont(font)
#if QT_CONFIG(accessibility)
        self.label_image.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.label_image.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_image.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_image, 0, 0, 1, 2)

        self.entry_mail = QLineEdit(self.layoutWidget)
        self.entry_mail.setObjectName(u"entry_mail")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.entry_mail.sizePolicy().hasHeightForWidth())
        self.entry_mail.setSizePolicy(sizePolicy1)
        self.entry_mail.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(9)
        self.entry_mail.setFont(font1)
        self.entry_mail.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.entry_mail, 1, 0, 1, 2)

        self.check_confirm = QCheckBox(self.layoutWidget)
        self.check_confirm.setObjectName(u"check_confirm")
        sizePolicy1.setHeightForWidth(self.check_confirm.sizePolicy().hasHeightForWidth())
        self.check_confirm.setSizePolicy(sizePolicy1)
        self.check_confirm.setFont(font1)
        self.check_confirm.setTristate(False)

        self.gridLayout.addWidget(self.check_confirm, 2, 0, 1, 2)

        self.but_registr = QPushButton(self.layoutWidget)
        self.but_registr.setObjectName(u"but_registr")
        sizePolicy1.setHeightForWidth(self.but_registr.sizePolicy().hasHeightForWidth())
        self.but_registr.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(12)
        self.but_registr.setFont(font2)

        self.gridLayout.addWidget(self.but_registr, 3, 0, 1, 2)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)

        self.but_login = QPushButton(self.layoutWidget)
        self.but_login.setObjectName(u"but_login")
        sizePolicy1.setHeightForWidth(self.but_login.sizePolicy().hasHeightForWidth())
        self.but_login.setSizePolicy(sizePolicy1)
        self.but_login.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setPointSize(10)
        self.but_login.setFont(font3)

        self.gridLayout.addWidget(self.but_login, 4, 1, 1, 1)

        Registr.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Registr)
        self.statusbar.setObjectName(u"statusbar")
        Registr.setStatusBar(self.statusbar)

        self.retranslateUi(Registr)

        QMetaObject.connectSlotsByName(Registr)
    # setupUi

    def retranslateUi(self, Registr):
        Registr.setWindowTitle(QCoreApplication.translate("Registr", u"Registr", None))
        self.label_image.setText(QCoreApplication.translate("Registr", u"\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430", None))
        self.entry_mail.setPlaceholderText(QCoreApplication.translate("Registr", u"\u0410\u0434\u0440\u0435\u0441 \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u043e\u0439 \u043f\u043e\u0447\u0442\u044b", None))
        self.check_confirm.setText(QCoreApplication.translate("Registr", u"\u0414\u0430\u044e \u0441\u043e\u0433\u043b\u0430\u0441\u0438\u0435 \u043d\u0430 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0443 \u043f\u0435\u0440\u0441\u043e\u043d\u0430\u043b\u044c\u043d\u044b\u0445 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.but_registr.setText(QCoreApplication.translate("Registr", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
        self.label.setText(QCoreApplication.translate("Registr", u"\u0423\u0436\u0435 \u0435\u0441\u0442\u044c \u0430\u043a\u043a\u0430\u0443\u043d\u0442 ?", None))
        self.but_login.setText(QCoreApplication.translate("Registr", u"\u0412\u043e\u0439\u0442\u0438", None))
    # retranslateUi

