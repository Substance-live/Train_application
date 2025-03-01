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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSplitter, QVBoxLayout,
    QWidget)
import res

class Ui_Profile(object):
    def setupUi(self, Profile):
        if not Profile.objectName():
            Profile.setObjectName(u"Profile")
        Profile.resize(307, 383)
        self.centralwidget = QWidget(Profile)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.label_image_2 = QLabel(self.splitter)
        self.label_image_2.setObjectName(u"label_image_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_image_2.sizePolicy().hasHeightForWidth())
        self.label_image_2.setSizePolicy(sizePolicy)
        self.label_image_2.setMinimumSize(QSize(0, 104))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(True)
        self.label_image_2.setFont(font)
        self.label_image_2.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
#if QT_CONFIG(accessibility)
        self.label_image_2.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.label_image_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_image_2.setStyleSheet(u"image: url(:/icon/data/image/default_user.png);")
        self.label_image_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.splitter.addWidget(self.label_image_2)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.but_edit = QPushButton(self.layoutWidget)
        self.but_edit.setObjectName(u"but_edit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.but_edit.sizePolicy().hasHeightForWidth())
        self.but_edit.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(9)
        self.but_edit.setFont(font1)

        self.verticalLayout.addWidget(self.but_edit)

        self.but_orders = QPushButton(self.layoutWidget)
        self.but_orders.setObjectName(u"but_orders")
        sizePolicy1.setHeightForWidth(self.but_orders.sizePolicy().hasHeightForWidth())
        self.but_orders.setSizePolicy(sizePolicy1)
        self.but_orders.setFont(font1)

        self.verticalLayout.addWidget(self.but_orders)

        self.but_timetable = QPushButton(self.layoutWidget)
        self.but_timetable.setObjectName(u"but_timetable")
        sizePolicy1.setHeightForWidth(self.but_timetable.sizePolicy().hasHeightForWidth())
        self.but_timetable.setSizePolicy(sizePolicy1)
        self.but_timetable.setFont(font1)

        self.verticalLayout.addWidget(self.but_timetable)

        self.but_logout = QPushButton(self.layoutWidget)
        self.but_logout.setObjectName(u"but_logout")
        sizePolicy1.setHeightForWidth(self.but_logout.sizePolicy().hasHeightForWidth())
        self.but_logout.setSizePolicy(sizePolicy1)
        self.but_logout.setFont(font1)

        self.verticalLayout.addWidget(self.but_logout)

        self.splitter.addWidget(self.layoutWidget)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)

        Profile.setCentralWidget(self.centralwidget)

        self.retranslateUi(Profile)

        QMetaObject.connectSlotsByName(Profile)
    # setupUi

    def retranslateUi(self, Profile):
        Profile.setWindowTitle(QCoreApplication.translate("Profile", u"Profile", None))
        self.label_image_2.setText("")
        self.but_edit.setText(QCoreApplication.translate("Profile", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u0440\u043e\u0444\u0438\u043b\u044c", None))
        self.but_orders.setText(QCoreApplication.translate("Profile", u"\u041c\u043e\u0438 \u0431\u0438\u043b\u0435\u0442\u044b", None))
        self.but_timetable.setText(QCoreApplication.translate("Profile", u"\u0420\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0438 \u0446\u0435\u043d\u044b", None))
        self.but_logout.setText(QCoreApplication.translate("Profile", u"\u0412\u044b\u0439\u0442\u0438 \u0438\u0437 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430", None))
    # retranslateUi

