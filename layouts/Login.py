# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(408, 437)
        self.centralwidget = QWidget(Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 10, 366, 401))
        font = QFont()
        font.setPointSize(10)
        self.layoutWidget.setFont(font)
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_image = QLabel(self.layoutWidget)
        self.label_image.setObjectName(u"label_image")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_image.sizePolicy().hasHeightForWidth())
        self.label_image.setSizePolicy(sizePolicy)
        self.label_image.setMinimumSize(QSize(0, 104))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(28)
        font1.setBold(True)
        font1.setItalic(True)
        self.label_image.setFont(font1)
        self.label_image.setContextMenuPolicy(Qt.NoContextMenu)
#if QT_CONFIG(accessibility)
        self.label_image.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.label_image.setLayoutDirection(Qt.LeftToRight)
        self.label_image.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_image)

        self.entry_login = QLineEdit(self.layoutWidget)
        self.entry_login.setObjectName(u"entry_login")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.entry_login.sizePolicy().hasHeightForWidth())
        self.entry_login.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        self.entry_login.setFont(font2)
        self.entry_login.setClearButtonEnabled(False)

        self.verticalLayout.addWidget(self.entry_login)

        self.entry_passwd = QLineEdit(self.layoutWidget)
        self.entry_passwd.setObjectName(u"entry_passwd")
        sizePolicy1.setHeightForWidth(self.entry_passwd.sizePolicy().hasHeightForWidth())
        self.entry_passwd.setSizePolicy(sizePolicy1)
        self.entry_passwd.setFont(font)

        self.verticalLayout.addWidget(self.entry_passwd)

        self.but_recovery = QPushButton(self.layoutWidget)
        self.but_recovery.setObjectName(u"but_recovery")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.but_recovery.sizePolicy().hasHeightForWidth())
        self.but_recovery.setSizePolicy(sizePolicy2)
        self.but_recovery.setMaximumSize(QSize(16777215, 16777215))
        self.but_recovery.setFont(font)
        self.but_recovery.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout.addWidget(self.but_recovery)

        self.but_login = QPushButton(self.layoutWidget)
        self.but_login.setObjectName(u"but_login")
        sizePolicy1.setHeightForWidth(self.but_login.sizePolicy().hasHeightForWidth())
        self.but_login.setSizePolicy(sizePolicy1)
        self.but_login.setFont(font)

        self.verticalLayout.addWidget(self.but_login)

        self.but_alter_login = QPushButton(self.layoutWidget)
        self.but_alter_login.setObjectName(u"but_alter_login")
        sizePolicy1.setHeightForWidth(self.but_alter_login.sizePolicy().hasHeightForWidth())
        self.but_alter_login.setSizePolicy(sizePolicy1)
        self.but_alter_login.setFont(font)

        self.verticalLayout.addWidget(self.but_alter_login)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.but_registr = QPushButton(self.layoutWidget)
        self.but_registr.setObjectName(u"but_registr")
        sizePolicy1.setHeightForWidth(self.but_registr.sizePolicy().hasHeightForWidth())
        self.but_registr.setSizePolicy(sizePolicy1)
        self.but_registr.setMaximumSize(QSize(16777215, 16777215))
        self.but_registr.setFont(font)

        self.horizontalLayout.addWidget(self.but_registr)


        self.verticalLayout.addLayout(self.horizontalLayout)

        Login.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Login)
        self.statusbar.setObjectName(u"statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Login", None))
        self.label_image.setText(QCoreApplication.translate("Login", u"\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430", None))
        self.entry_login.setPlaceholderText(QCoreApplication.translate("Login", u"\u0410\u0434\u0440\u0435\u0441 \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u043e\u0439 \u043f\u043e\u0447\u0442\u044b", None))
        self.entry_passwd.setPlaceholderText(QCoreApplication.translate("Login", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.but_recovery.setText(QCoreApplication.translate("Login", u"\u041d\u0435 \u043f\u043e\u043c\u043d\u044e \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.but_login.setText(QCoreApplication.translate("Login", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.but_alter_login.setText(QCoreApplication.translate("Login", u"\u0411\u044b\u0441\u0442\u0440\u044b\u0439 \u0432\u0445\u043e\u0434 \u0431\u0435\u0437 \u043f\u0430\u0440\u043e\u043b\u044f", None))
        self.label.setText(QCoreApplication.translate("Login", u"\u041d\u0435\u0442 \u043f\u0440\u043e\u0444\u0438\u043b\u044f?", None))
        self.but_registr.setText(QCoreApplication.translate("Login", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u0443\u0439\u0442\u0435\u0441\u044c, \u044d\u0442\u043e \u043b\u0435\u0433\u043a\u043e!", None))
    # retranslateUi

