# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'exam_culcul.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
# import files_rc

class Ui_Culculator(object):
    def setupUi(self, Culculator):
        if not Culculator.objectName():
            Culculator.setObjectName(u"Culculator")
        Culculator.resize(300, 500)
        Culculator.setMinimumSize(QSize(300, 500))
        icon = QIcon()
        icon.addFile(u":/icons/Users/79119/Downloads/calculate_FILL0_wght400_GRAD0_opsz48 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        Culculator.setWindowIcon(icon)
        Culculator.setStyleSheet(u"QWidget {\n"
"	color: white;\n"
"	background-color: #121212;\n"
"	font-family: Rubik;\n"
"	font-size: 16pt;\n"
"	font-weight: 600;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #666;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #888;\n"
"}")
        self.centralwidget = QWidget(Culculator)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QtWidget {\n"
"    color: white;\n"
"    background-color: #121212;\n"
"    font-family: Rubik;\n"
"    font-size: 16pt;\n"
"    font-weight: 600;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_temp = QLabel(self.centralwidget)
        self.lbl_temp.setObjectName(u"lbl_temp")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_temp.sizePolicy().hasHeightForWidth())
        self.lbl_temp.setSizePolicy(sizePolicy)
        self.lbl_temp.setStyleSheet(u"color: #888")
        self.lbl_temp.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.lbl_temp)

        self.le_entry = QLineEdit(self.centralwidget)
        self.le_entry.setObjectName(u"le_entry")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le_entry.sizePolicy().hasHeightForWidth())
        self.le_entry.setSizePolicy(sizePolicy1)
        self.le_entry.setStyleSheet(u"font-size: 40pt;\n"
"border: none;")
        self.le_entry.setMaxLength(12)
        self.le_entry.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.le_entry.setReadOnly(True)

        self.verticalLayout.addWidget(self.le_entry)

        self.Layout_butt = QGridLayout()
        self.Layout_butt.setObjectName(u"Layout_butt")
        self.btn_ce = QPushButton(self.centralwidget)
        self.btn_ce.setObjectName(u"btn_ce")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_ce.sizePolicy().hasHeightForWidth())
        self.btn_ce.setSizePolicy(sizePolicy2)

        self.Layout_butt.addWidget(self.btn_ce, 0, 1, 1, 1)

        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy2.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy2)

        self.Layout_butt.addWidget(self.btn_5, 2, 1, 1, 1)

        self.btn_plus = QPushButton(self.centralwidget)
        self.btn_plus.setObjectName(u"btn_plus")
        sizePolicy2.setHeightForWidth(self.btn_plus.sizePolicy().hasHeightForWidth())
        self.btn_plus.setSizePolicy(sizePolicy2)

        self.Layout_butt.addWidget(self.btn_plus, 3, 3, 1, 1)

        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy2.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy2)

        self.Layout_butt.addWidget(self.btn_3, 3, 2, 1, 1)

        self.btn_multi = QPushButton(self.centralwidget)
        self.btn_multi.setObjectName(u"btn_multi")
        sizePolicy2.setHeightForWidth(self.btn_multi.sizePolicy().hasHeightForWidth())
        self.btn_multi.setSizePolicy(sizePolicy2)

        self.Layout_butt.addWidget(self.btn_multi, 1, 3, 1, 1)

        self.btn_equal = QPushButton(self.centralwidget)
        self.btn_equal.setObjectName(u"btn_equal")
        sizePolicy2.setHeightForWidth(self.btn_equal.sizePolicy().hasHeightForWidth())
        self.btn_equal.setSizePolicy(sizePolicy2)

        self.Layout_butt.addWidget(self.btn_equal, 4, 3, 1, 1)

        self.btn_minus = QPushButton(self.centralwidget)
        self.btn_minus.setObjectName(u"btn_minus")
        sizePolicy2.setHeightForWidth(self.btn_minus.sizePolicy().hasHeightForWidth())
        self.btn_minus.setSizePolicy(sizePolicy2)

        self.Layout_butt.addWidget(self.btn_minus, 2, 3, 1, 1)

        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy2.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy2)

        self.Layout_butt.addWidget(self.btn_9, 1, 2, 1, 1)

        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy2.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy2)

        self.Layout_butt.addWidget(self.btn_8, 1, 1, 1, 1)

        self.btn_slash = QPushButton(self.centralwidget)
        self.btn_slash.setObjectName(u"btn_slash")
        sizePolicy2.setHeightForWidth(self.btn_slash.sizePolicy().hasHeightForWidth())
        self.btn_slash.setSizePolicy(sizePolicy2)

        self.Layout_butt.addWidget(self.btn_slash, 0, 3, 1, 1)

        self.btn_point = QPushButton(self.centralwidget)
        self.btn_point.setObjectName(u"btn_point")
        sizePolicy2.setHeightForWidth(self.btn_point.sizePolicy().hasHeightForWidth())
        self.btn_point.setSizePolicy(sizePolicy2)

        self.Layout_butt.addWidget(self.btn_point, 4, 2, 1, 1)

        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy2.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy2)

        self.Layout_butt.addWidget(self.btn_6, 2, 2, 1, 1)

        self.btn_backspc = QPushButton(self.centralwidget)
        self.btn_backspc.setObjectName(u"btn_backspc")
        sizePolicy2.setHeightForWidth(self.btn_backspc.sizePolicy().hasHeightForWidth())
        self.btn_backspc.setSizePolicy(sizePolicy2)
        icon1 = QIcon()
        icon1.addFile(u":/icons/Users/79119/Downloads/backspace_FILL0_wght400_GRAD0_opsz48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_backspc.setIcon(icon1)
        self.btn_backspc.setIconSize(QSize(24, 24))

        self.Layout_butt.addWidget(self.btn_backspc, 0, 2, 1, 1)

        self.btn_c = QPushButton(self.centralwidget)
        self.btn_c.setObjectName(u"btn_c")
        sizePolicy2.setHeightForWidth(self.btn_c.sizePolicy().hasHeightForWidth())
        self.btn_c.setSizePolicy(sizePolicy2)
        self.btn_c.setCursor(QCursor(Qt.PointingHandCursor))

        self.Layout_butt.addWidget(self.btn_c, 0, 0, 1, 1)

        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy2.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy2)

        self.Layout_butt.addWidget(self.btn_7, 1, 0, 1, 1)

        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy2.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy2)

        self.Layout_butt.addWidget(self.btn_4, 2, 0, 1, 1)

        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy2.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy2)

        self.Layout_butt.addWidget(self.btn_1, 3, 0, 1, 1)

        self.btn_sign = QPushButton(self.centralwidget)
        self.btn_sign.setObjectName(u"btn_sign")
        sizePolicy2.setHeightForWidth(self.btn_sign.sizePolicy().hasHeightForWidth())
        self.btn_sign.setSizePolicy(sizePolicy2)

        self.Layout_butt.addWidget(self.btn_sign, 4, 0, 1, 1)

        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy2.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy2)

        self.Layout_butt.addWidget(self.btn_2, 3, 1, 1, 1)

        self.btn_0 = QPushButton(self.centralwidget)
        self.btn_0.setObjectName(u"btn_0")
        sizePolicy2.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy2)

        self.Layout_butt.addWidget(self.btn_0, 4, 1, 1, 1)


        self.verticalLayout.addLayout(self.Layout_butt)

        Culculator.setCentralWidget(self.centralwidget)

        self.retranslateUi(Culculator)

        QMetaObject.connectSlotsByName(Culculator)
    # setupUi

    def retranslateUi(self, Culculator):
        Culculator.setWindowTitle(QCoreApplication.translate("Culculator", u"Culculator", None))
        self.lbl_temp.setText(QCoreApplication.translate("Culculator", u"234+56.4=", None))
        self.le_entry.setText(QCoreApplication.translate("Culculator", u"0", None))
        self.btn_ce.setText(QCoreApplication.translate("Culculator", u"CE", None))
#if QT_CONFIG(shortcut)
        self.btn_ce.setShortcut(QCoreApplication.translate("Culculator", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.btn_5.setText(QCoreApplication.translate("Culculator", u"5", None))
#if QT_CONFIG(shortcut)
        self.btn_5.setShortcut(QCoreApplication.translate("Culculator", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.btn_plus.setText(QCoreApplication.translate("Culculator", u"+", None))
#if QT_CONFIG(shortcut)
        self.btn_plus.setShortcut(QCoreApplication.translate("Culculator", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.btn_3.setText(QCoreApplication.translate("Culculator", u"3", None))
#if QT_CONFIG(shortcut)
        self.btn_3.setShortcut(QCoreApplication.translate("Culculator", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.btn_multi.setText(QCoreApplication.translate("Culculator", u"*", None))
#if QT_CONFIG(shortcut)
        self.btn_multi.setShortcut(QCoreApplication.translate("Culculator", u"*", None))
#endif // QT_CONFIG(shortcut)
        self.btn_equal.setText(QCoreApplication.translate("Culculator", u"=", None))
#if QT_CONFIG(shortcut)
        self.btn_equal.setShortcut(QCoreApplication.translate("Culculator", u"=", None))
#endif // QT_CONFIG(shortcut)
        self.btn_minus.setText(QCoreApplication.translate("Culculator", u"-", None))
#if QT_CONFIG(shortcut)
        self.btn_minus.setShortcut(QCoreApplication.translate("Culculator", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.btn_9.setText(QCoreApplication.translate("Culculator", u"9", None))
#if QT_CONFIG(shortcut)
        self.btn_9.setShortcut(QCoreApplication.translate("Culculator", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.btn_8.setText(QCoreApplication.translate("Culculator", u"8", None))
#if QT_CONFIG(shortcut)
        self.btn_8.setShortcut(QCoreApplication.translate("Culculator", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.btn_slash.setText(QCoreApplication.translate("Culculator", u"/", None))
#if QT_CONFIG(shortcut)
        self.btn_slash.setShortcut(QCoreApplication.translate("Culculator", u"/", None))
#endif // QT_CONFIG(shortcut)
        self.btn_point.setText(QCoreApplication.translate("Culculator", u".", None))
#if QT_CONFIG(shortcut)
        self.btn_point.setShortcut(QCoreApplication.translate("Culculator", u".", None))
#endif // QT_CONFIG(shortcut)
        self.btn_6.setText(QCoreApplication.translate("Culculator", u"6", None))
#if QT_CONFIG(shortcut)
        self.btn_6.setShortcut(QCoreApplication.translate("Culculator", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.btn_backspc.setText(QCoreApplication.translate("Culculator", u"->", None))
#if QT_CONFIG(shortcut)
        self.btn_backspc.setShortcut(QCoreApplication.translate("Culculator", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.btn_c.setText(QCoreApplication.translate("Culculator", u"C", None))
        self.btn_7.setText(QCoreApplication.translate("Culculator", u"7", None))
#if QT_CONFIG(shortcut)
        self.btn_7.setShortcut(QCoreApplication.translate("Culculator", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.btn_4.setText(QCoreApplication.translate("Culculator", u"4", None))
#if QT_CONFIG(shortcut)
        self.btn_4.setShortcut(QCoreApplication.translate("Culculator", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.btn_1.setText(QCoreApplication.translate("Culculator", u"1", None))
#if QT_CONFIG(shortcut)
        self.btn_1.setShortcut(QCoreApplication.translate("Culculator", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.btn_sign.setText(QCoreApplication.translate("Culculator", u"+/-", None))
        self.btn_2.setText(QCoreApplication.translate("Culculator", u"2", None))
#if QT_CONFIG(shortcut)
        self.btn_2.setShortcut(QCoreApplication.translate("Culculator", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.btn_0.setText(QCoreApplication.translate("Culculator", u"0", None))
#if QT_CONFIG(shortcut)
        self.btn_0.setShortcut(QCoreApplication.translate("Culculator", u"0", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

