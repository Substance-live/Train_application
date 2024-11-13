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
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSplitter, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_EditProfile(object):
    def setupUi(self, EditProfile):
        if not EditProfile.objectName():
            EditProfile.setObjectName(u"EditProfile")
        EditProfile.resize(387, 334)
        EditProfile.setMinimumSize(QSize(387, 334))
        EditProfile.setMaximumSize(QSize(387, 334))
        self.centralwidget = QWidget(EditProfile)
        self.centralwidget.setObjectName(u"centralwidget")
        self.splitter_2 = QSplitter(self.centralwidget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setGeometry(QRect(20, 13, 351, 321))
        self.splitter_2.setOrientation(Qt.Orientation.Vertical)
        self.splitter_2.setHandleWidth(0)
        self.layoutWidget = QWidget(self.splitter_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout_3.addWidget(self.label)

        self.splitter = QSplitter(self.layoutWidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(self.layoutWidget1)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.splitter.addWidget(self.layoutWidget1)
        self.layoutWidget2 = QWidget(self.splitter)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.layoutWidget2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.layoutWidget2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_2.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.layoutWidget2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout_2.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(self.layoutWidget2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.verticalLayout_2.addWidget(self.lineEdit_4)

        self.dateEdit = QDateEdit(self.layoutWidget2)
        self.dateEdit.setObjectName(u"dateEdit")

        self.verticalLayout_2.addWidget(self.dateEdit)

        self.splitter.addWidget(self.layoutWidget2)

        self.verticalLayout_3.addWidget(self.splitter)

        self.checkBox = QCheckBox(self.layoutWidget)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_3.addWidget(self.checkBox)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_3.addWidget(self.pushButton)

        self.splitter_2.addWidget(self.layoutWidget)
        self.commandLinkButton = QCommandLinkButton(self.splitter_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commandLinkButton.sizePolicy().hasHeightForWidth())
        self.commandLinkButton.setSizePolicy(sizePolicy)
        self.commandLinkButton.setMinimumSize(QSize(0, 0))
        self.commandLinkButton.setMaximumSize(QSize(100000, 100000))
        self.commandLinkButton.setSizeIncrement(QSize(0, 0))
        self.commandLinkButton.setBaseSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(9)
        font1.setHintingPreference(QFont.PreferDefaultHinting)
        self.commandLinkButton.setFont(font1)
        self.commandLinkButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.splitter_2.addWidget(self.commandLinkButton)
        EditProfile.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(EditProfile)
        self.statusbar.setObjectName(u"statusbar")
        EditProfile.setStatusBar(self.statusbar)

        self.retranslateUi(EditProfile)

        QMetaObject.connectSlotsByName(EditProfile)
    # setupUi

    def retranslateUi(self, EditProfile):
        EditProfile.setWindowTitle(QCoreApplication.translate("EditProfile", u"EditProfile", None))
        self.label.setText(QCoreApplication.translate("EditProfile", u"\u041b\u0438\u0447\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.label_2.setText(QCoreApplication.translate("EditProfile", u"\u0418\u043c\u044f", None))
        self.label_3.setText(QCoreApplication.translate("EditProfile", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_4.setText(QCoreApplication.translate("EditProfile", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.label_5.setText(QCoreApplication.translate("EditProfile", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.label_6.setText(QCoreApplication.translate("EditProfile", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.checkBox.setText(QCoreApplication.translate("EditProfile", u"\u042f \u0434\u0430\u044e \u0441\u043e\u0433\u043b\u0430\u0441\u0438\u0435 \u043d\u0430 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0443 \u043c\u043e\u0438\u0445 \u043f\u0435\u0440\u0441\u043e\u043d\u0430\u043b\u044c\u043d\u044b\u0445 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.pushButton.setText(QCoreApplication.translate("EditProfile", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.commandLinkButton.setText(QCoreApplication.translate("EditProfile", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.commandLinkButton.setDescription("")
    # retranslateUi

