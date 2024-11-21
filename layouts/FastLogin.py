# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FastLogin.ui'
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

class Ui_FastLogin(object):
    def setupUi(self, FastLogin):
        if not FastLogin.objectName():
            FastLogin.setObjectName(u"FastLogin")
        FastLogin.resize(463, 492)
        self.centralwidget = QWidget(FastLogin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 10, 421, 451))
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
        self.label_image.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
#if QT_CONFIG(accessibility)
        self.label_image.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.label_image.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_image.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_image)

        self.label_note = QLabel(self.layoutWidget)
        self.label_note.setObjectName(u"label_note")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_note.sizePolicy().hasHeightForWidth())
        self.label_note.setSizePolicy(sizePolicy1)
        self.label_note.setMinimumSize(QSize(418, 62))
        self.label_note.setMaximumSize(QSize(16777215, 16777215))
        self.label_note.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_note.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_note)

        self.entry_email = QLineEdit(self.layoutWidget)
        self.entry_email.setObjectName(u"entry_email")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.entry_email.sizePolicy().hasHeightForWidth())
        self.entry_email.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        self.entry_email.setFont(font2)
        self.entry_email.setClearButtonEnabled(False)

        self.verticalLayout.addWidget(self.entry_email)

        self.but_send_messenge = QPushButton(self.layoutWidget)
        self.but_send_messenge.setObjectName(u"but_send_messenge")
        sizePolicy2.setHeightForWidth(self.but_send_messenge.sizePolicy().hasHeightForWidth())
        self.but_send_messenge.setSizePolicy(sizePolicy2)
        self.but_send_messenge.setFont(font)

        self.verticalLayout.addWidget(self.but_send_messenge)

        self.but_login = QPushButton(self.layoutWidget)
        self.but_login.setObjectName(u"but_login")
        sizePolicy2.setHeightForWidth(self.but_login.sizePolicy().hasHeightForWidth())
        self.but_login.setSizePolicy(sizePolicy2)
        self.but_login.setFont(font)

        self.verticalLayout.addWidget(self.but_login)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.but_registr = QPushButton(self.layoutWidget)
        self.but_registr.setObjectName(u"but_registr")
        sizePolicy2.setHeightForWidth(self.but_registr.sizePolicy().hasHeightForWidth())
        self.but_registr.setSizePolicy(sizePolicy2)
        self.but_registr.setMaximumSize(QSize(16777215, 16777215))
        self.but_registr.setFont(font)

        self.horizontalLayout.addWidget(self.but_registr)


        self.verticalLayout.addLayout(self.horizontalLayout)

        FastLogin.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(FastLogin)
        self.statusbar.setObjectName(u"statusbar")
        FastLogin.setStatusBar(self.statusbar)

        self.retranslateUi(FastLogin)

        QMetaObject.connectSlotsByName(FastLogin)
    # setupUi

    def retranslateUi(self, FastLogin):
        FastLogin.setWindowTitle(QCoreApplication.translate("FastLogin", u"FastLogin", None))
        self.label_image.setText(QCoreApplication.translate("FastLogin", u"\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430", None))
        self.label_note.setText(QCoreApplication.translate("FastLogin", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u043f\u043e\u0447\u0442\u0443, \u043a\u043e\u0442\u043e\u0440\u0443\u044e \u0443\u043a\u0430\u0437\u044b\u0432\u0430\u043b\u0438 \u043f\u0440\u0438 \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438, \u0447\u0442\u043e\u0431\u044b \u043f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u043a\u043e\u0434 \u0434\u043b\u044f \u0431\u044b\u0441\u0442\u0440\u043e\u0433\u043e \u0432\u0445\u043e\u0434\u0430 \u0432 \u0430\u043a\u043a\u0430\u0443\u043d\u0442.", None))
        self.entry_email.setPlaceholderText(QCoreApplication.translate("FastLogin", u"\u0410\u0434\u0440\u0435\u0441 \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u043e\u0439 \u043f\u043e\u0447\u0442\u044b", None))
        self.but_send_messenge.setText(QCoreApplication.translate("FastLogin", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u043a\u043e\u0434", None))
        self.but_login.setText(QCoreApplication.translate("FastLogin", u"\u0412\u043e\u0439\u0442\u0438 \u0441 \u043f\u0430\u0440\u043e\u043b\u0435\u043c", None))
        self.label.setText(QCoreApplication.translate("FastLogin", u"\u041d\u0435\u0442 \u043f\u0440\u043e\u0444\u0438\u043b\u044f?", None))
        self.but_registr.setText(QCoreApplication.translate("FastLogin", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u0443\u0439\u0442\u0435\u0441\u044c, \u044d\u0442\u043e \u043b\u0435\u0433\u043a\u043e!", None))
    # retranslateUi

