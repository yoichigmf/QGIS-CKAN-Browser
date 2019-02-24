# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ckan_browser_dialog_disclaimer.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CKANBrowserDisclaimer(object):
    def setupUi(self, CKANBrowserDisclaimer):
        CKANBrowserDisclaimer.setObjectName("CKANBrowserDisclaimer")
        CKANBrowserDisclaimer.resize(394, 290)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CKANBrowserDisclaimer.sizePolicy().hasHeightForWidth())
        CKANBrowserDisclaimer.setSizePolicy(sizePolicy)
        CKANBrowserDisclaimer.setMinimumSize(QtCore.QSize(0, 0))
        CKANBrowserDisclaimer.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gridLayout = QtWidgets.QGridLayout(CKANBrowserDisclaimer)
        self.gridLayout.setObjectName("gridLayout")
        self.IDC_lblLogo = QtWidgets.QLabel(CKANBrowserDisclaimer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IDC_lblLogo.sizePolicy().hasHeightForWidth())
        self.IDC_lblLogo.setSizePolicy(sizePolicy)
        self.IDC_lblLogo.setMinimumSize(QtCore.QSize(60, 60))
        self.IDC_lblLogo.setMaximumSize(QtCore.QSize(60, 60))
        self.IDC_lblLogo.setText("")
        self.IDC_lblLogo.setObjectName("IDC_lblLogo")
        self.gridLayout.addWidget(self.IDC_lblLogo, 0, 0, 1, 1)
        self.IDC_lblTitle = QtWidgets.QLabel(CKANBrowserDisclaimer)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.IDC_lblTitle.setFont(font)
        self.IDC_lblTitle.setObjectName("IDC_lblTitle")
        self.gridLayout.addWidget(self.IDC_lblTitle, 0, 1, 1, 1)
        self.button_box = QtWidgets.QDialogButtonBox(CKANBrowserDisclaimer)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.button_box.setObjectName("button_box")
        self.gridLayout.addWidget(self.button_box, 2, 1, 1, 1)
        self.IDC_brInfo = QtWidgets.QTextBrowser(CKANBrowserDisclaimer)
        self.IDC_brInfo.setObjectName("IDC_brInfo")
        self.gridLayout.addWidget(self.IDC_brInfo, 1, 0, 1, 2)

        self.retranslateUi(CKANBrowserDisclaimer)
        self.button_box.accepted.connect(CKANBrowserDisclaimer.accept)
        self.button_box.rejected.connect(CKANBrowserDisclaimer.reject)
        QtCore.QMetaObject.connectSlotsByName(CKANBrowserDisclaimer)

    def retranslateUi(self, CKANBrowserDisclaimer):
        _translate = QtCore.QCoreApplication.translate
        CKANBrowserDisclaimer.setWindowTitle(_translate("CKANBrowserDisclaimer", "dlg_dsc_dlg_title"))
        self.IDC_lblTitle.setText(_translate("CKANBrowserDisclaimer", "dlg_dsc_title"))

