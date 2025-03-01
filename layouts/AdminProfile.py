# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AdminProfile.ui'
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

class Ui_AdminProfile(object):
    def setupUi(self, AdminProfile):
        if not AdminProfile.objectName():
            AdminProfile.setObjectName(u"AdminProfile")
        AdminProfile.resize(302, 390)
        self.centralwidget = QWidget(AdminProfile)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.label_image_2 = QLabel(self.splitter)
        self.label_image_2.setObjectName(u"label_image_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_image_2.sizePolicy().hasHeightForWidth())
        self.label_image_2.setSizePolicy(sizePolicy1)
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
        self.but_users = QPushButton(self.layoutWidget)
        self.but_users.setObjectName(u"but_users")
        sizePolicy.setHeightForWidth(self.but_users.sizePolicy().hasHeightForWidth())
        self.but_users.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(9)
        self.but_users.setFont(font1)

        self.verticalLayout.addWidget(self.but_users)

        self.but_flight = QPushButton(self.layoutWidget)
        self.but_flight.setObjectName(u"but_flight")
        sizePolicy.setHeightForWidth(self.but_flight.sizePolicy().hasHeightForWidth())
        self.but_flight.setSizePolicy(sizePolicy)
        self.but_flight.setFont(font1)

        self.verticalLayout.addWidget(self.but_flight)

        self.but_logout = QPushButton(self.layoutWidget)
        self.but_logout.setObjectName(u"but_logout")
        sizePolicy.setHeightForWidth(self.but_logout.sizePolicy().hasHeightForWidth())
        self.but_logout.setSizePolicy(sizePolicy)
        self.but_logout.setFont(font1)

        self.verticalLayout.addWidget(self.but_logout)

        self.splitter.addWidget(self.layoutWidget)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)

        AdminProfile.setCentralWidget(self.centralwidget)

        self.retranslateUi(AdminProfile)

        QMetaObject.connectSlotsByName(AdminProfile)
    # setupUi

    def retranslateUi(self, AdminProfile):
        AdminProfile.setWindowTitle(QCoreApplication.translate("AdminProfile", u"AdminProfile", None))
        self.label_image_2.setText("")
        self.but_users.setText(QCoreApplication.translate("AdminProfile", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 \u0438 \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439", None))
        self.but_flight.setText(QCoreApplication.translate("AdminProfile", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 \u0438 \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0440\u0435\u0439\u0441\u043e\u0432", None))
        self.but_logout.setText(QCoreApplication.translate("AdminProfile", u"\u0412\u044b\u0439\u0442\u0438 \u0438\u0437 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430", None))
    # retranslateUi

