# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EditProfile.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QCommandLinkButton, QDateEdit,
    QGridLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSplitter, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_EditProfile(object):
    def setupUi(self, EditProfile):
        if not EditProfile.objectName():
            EditProfile.setObjectName(u"EditProfile")
        EditProfile.resize(387, 334)
        EditProfile.setMinimumSize(QSize(387, 334))
        EditProfile.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(EditProfile)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter_2 = QSplitter(self.centralwidget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Orientation.Vertical)
        self.splitter_2.setHandleWidth(0)
        self.layoutWidget = QWidget(self.splitter_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_main = QLabel(self.layoutWidget)
        self.label_main.setObjectName(u"label_main")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_main.setFont(font)

        self.verticalLayout_3.addWidget(self.label_main)

        self.splitter = QSplitter(self.layoutWidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_name = QLabel(self.layoutWidget1)
        self.label_name.setObjectName(u"label_name")

        self.verticalLayout.addWidget(self.label_name)

        self.label_surname = QLabel(self.layoutWidget1)
        self.label_surname.setObjectName(u"label_surname")

        self.verticalLayout.addWidget(self.label_surname)

        self.label_patronymic = QLabel(self.layoutWidget1)
        self.label_patronymic.setObjectName(u"label_patronymic")

        self.verticalLayout.addWidget(self.label_patronymic)

        self.label_phone = QLabel(self.layoutWidget1)
        self.label_phone.setObjectName(u"label_phone")

        self.verticalLayout.addWidget(self.label_phone)

        self.label_birthday = QLabel(self.layoutWidget1)
        self.label_birthday.setObjectName(u"label_birthday")

        self.verticalLayout.addWidget(self.label_birthday)

        self.splitter.addWidget(self.layoutWidget1)
        self.layoutWidget2 = QWidget(self.splitter)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.entry_name = QLineEdit(self.layoutWidget2)
        self.entry_name.setObjectName(u"entry_name")

        self.verticalLayout_2.addWidget(self.entry_name)

        self.entry_surname = QLineEdit(self.layoutWidget2)
        self.entry_surname.setObjectName(u"entry_surname")

        self.verticalLayout_2.addWidget(self.entry_surname)

        self.entry_patronymic = QLineEdit(self.layoutWidget2)
        self.entry_patronymic.setObjectName(u"entry_patronymic")

        self.verticalLayout_2.addWidget(self.entry_patronymic)

        self.entry_phone = QLineEdit(self.layoutWidget2)
        self.entry_phone.setObjectName(u"entry_phone")

        self.verticalLayout_2.addWidget(self.entry_phone)

        self.date_edit = QDateEdit(self.layoutWidget2)
        self.date_edit.setObjectName(u"date_edit")
        self.date_edit.setCalendarPopup(True)

        self.verticalLayout_2.addWidget(self.date_edit)

        self.splitter.addWidget(self.layoutWidget2)

        self.verticalLayout_3.addWidget(self.splitter)

        self.check_confirm = QCheckBox(self.layoutWidget)
        self.check_confirm.setObjectName(u"check_confirm")

        self.verticalLayout_3.addWidget(self.check_confirm)

        self.but_save = QPushButton(self.layoutWidget)
        self.but_save.setObjectName(u"but_save")

        self.verticalLayout_3.addWidget(self.but_save)

        self.splitter_2.addWidget(self.layoutWidget)
        self.but_return = QCommandLinkButton(self.splitter_2)
        self.but_return.setObjectName(u"but_return")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_return.sizePolicy().hasHeightForWidth())
        self.but_return.setSizePolicy(sizePolicy)
        self.but_return.setMinimumSize(QSize(0, 0))
        self.but_return.setMaximumSize(QSize(100000, 100000))
        self.but_return.setSizeIncrement(QSize(0, 0))
        self.but_return.setBaseSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(9)
        font1.setHintingPreference(QFont.PreferDefaultHinting)
        self.but_return.setFont(font1)
        self.but_return.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.splitter_2.addWidget(self.but_return)

        self.gridLayout.addWidget(self.splitter_2, 0, 0, 1, 1)

        EditProfile.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(EditProfile)
        self.statusbar.setObjectName(u"statusbar")
        EditProfile.setStatusBar(self.statusbar)

        self.retranslateUi(EditProfile)

        QMetaObject.connectSlotsByName(EditProfile)
    # setupUi

    def retranslateUi(self, EditProfile):
        EditProfile.setWindowTitle(QCoreApplication.translate("EditProfile", u"EditProfile", None))
        self.label_main.setText(QCoreApplication.translate("EditProfile", u"\u041b\u0438\u0447\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.label_name.setText(QCoreApplication.translate("EditProfile", u"\u0418\u043c\u044f", None))
        self.label_surname.setText(QCoreApplication.translate("EditProfile", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.label_patronymic.setText(QCoreApplication.translate("EditProfile", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_phone.setText(QCoreApplication.translate("EditProfile", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.label_birthday.setText(QCoreApplication.translate("EditProfile", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.check_confirm.setText(QCoreApplication.translate("EditProfile", u"\u042f \u0434\u0430\u044e \u0441\u043e\u0433\u043b\u0430\u0441\u0438\u0435 \u043d\u0430 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0443 \u043c\u043e\u0438\u0445 \u043f\u0435\u0440\u0441\u043e\u043d\u0430\u043b\u044c\u043d\u044b\u0445 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.but_save.setText(QCoreApplication.translate("EditProfile", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.but_return.setText(QCoreApplication.translate("EditProfile", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.but_return.setDescription("")
    # retranslateUi

