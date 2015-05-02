# -*- coding: utf-8 -*-
#!/usr/bin/python2

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Mon May 26 00:12:10 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 544)
        MainWindow.setMaximumSize(QtCore.QSize(800, 554))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(_fromUtf8(""))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        self.title = QtGui.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(16, 0, 180, 80))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName(_fromUtf8("title"))
        self.about = QtGui.QLabel(self.centralwidget)
        self.about.setGeometry(QtCore.QRect(14, 56, 100, 30))
        self.about.setAlignment(QtCore.Qt.AlignCenter)
        self.about.setObjectName(_fromUtf8("about"))
        self.buttonAbout = QtGui.QPushButton(self.centralwidget)
        self.buttonAbout.setGeometry(QtCore.QRect(110, 58, 24, 24))
        self.buttonAbout.setAutoDefault(False)
        self.buttonAbout.setDefault(False)
        self.buttonAbout.setFlat(False)
        self.buttonAbout.setObjectName(_fromUtf8("buttonAbout"))
        self.buttonConfigure = QtGui.QPushButton(self.centralwidget)
        self.buttonConfigure.setGeometry(QtCore.QRect(145, 58, 24, 24))
        self.buttonConfigure.setAutoDefault(False)
        self.buttonConfigure.setDefault(False)
        self.buttonConfigure.setFlat(False)
        self.buttonConfigure.setObjectName(_fromUtf8("buttonConfigure"))
        self.buttonConfigure.setIcon(QtGui.QIcon("/usr/share/nvidiux/img/conf.png"))
        self.buttonConfigure.setIconSize(QtCore.QSize(16,16))
        
        self.groupBoxProfile = QtGui.QGroupBox(self.centralwidget)
        self.groupBoxProfile.setGeometry(QtCore.QRect(6, 86, 198,65 ))
        self.groupBoxProfile.setStyleSheet(_fromUtf8("QGroupBox \n"
	"{ \n"
	"border: 2px solid SlateGrey;\n"
	"border-radius: 10px;\n"
	"}"))
        self.groupBoxProfile.setTitle(_fromUtf8(""))
        self.groupBoxProfile.setObjectName(_fromUtf8("groupBoxProfile"))
        self.buttonLoadProfile = QtGui.QPushButton(self.groupBoxProfile)
        self.buttonLoadProfile.setGeometry(QtCore.QRect(4,18, 90, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(40)
        self.buttonLoadProfile.setFont(font)
        self.buttonLoadProfile.setAutoDefault(False)
        self.buttonLoadProfile.setDefault(False)
        self.buttonLoadProfile.setFlat(False)
        self.buttonLoadProfile.setObjectName(_fromUtf8("buttonLoadProfile"))
        self.buttonSaveProfile = QtGui.QPushButton(self.groupBoxProfile)
        self.buttonSaveProfile.setGeometry(QtCore.QRect(104, 18, 90, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(40)
        self.buttonSaveProfile.setFont(font)
        self.buttonSaveProfile.setAutoDefault(False)
        self.buttonSaveProfile.setDefault(False)
        self.buttonSaveProfile.setFlat(False)
        self.buttonSaveProfile.setObjectName(_fromUtf8("buttonLoadProfile"))
        self.labelProfile = QtGui.QLabel(self.groupBoxProfile)
        self.labelProfile.setGeometry(QtCore.QRect(75, 2, 50, 20))
        self.labelProfile.setAlignment(QtCore.Qt.AlignCenter)
        self.labelProfile.setObjectName(_fromUtf8("LabelProfil"))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelProfile.setFont(font) 
        self.groupBoxMonitor = QtGui.QGroupBox(self.centralwidget)
        self.groupBoxMonitor.setGeometry(QtCore.QRect(210, 86, 198,65 ))
        self.groupBoxMonitor.setStyleSheet(_fromUtf8("QGroupBox \n"
	"{ \n"
	"border: 2px solid SlateGrey;\n"
	"border-radius: 10px;\n"
	"}"))
        self.groupBoxMonitor.setTitle(_fromUtf8(""))
        self.groupBoxMonitor.setObjectName(_fromUtf8("groupBoxMonitor"))
        self.buttonStartMonitor = QtGui.QPushButton(self.groupBoxMonitor)
        self.buttonStartMonitor.setGeometry(QtCore.QRect(4,18, 90, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(40)
        self.buttonStartMonitor.setFont(font)
        self.buttonStartMonitor.setAutoDefault(False)
        self.buttonStartMonitor.setDefault(False)
        self.buttonStartMonitor.setFlat(False)
        self.buttonStartMonitor.setObjectName(_fromUtf8("buttonStartMonitor"))
        self.buttonConfigureMonitor = QtGui.QPushButton(self.groupBoxMonitor)
        self.buttonConfigureMonitor.setGeometry(QtCore.QRect(104, 18, 90, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(40)
        self.buttonConfigureMonitor.setFont(font)
        self.buttonConfigureMonitor.setAutoDefault(False)
        self.buttonConfigureMonitor.setDefault(False)
        self.buttonConfigureMonitor.setFlat(False)
        self.buttonConfigureMonitor.setEnabled(True)
        self.buttonConfigureMonitor.setObjectName(_fromUtf8("ButtonConfigureProfile"))
        self.labelMonitor = QtGui.QLabel(self.groupBoxMonitor)
        self.labelMonitor.setGeometry(QtCore.QRect(50, 2, 100, 20))
        self.labelMonitor.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMonitor.setObjectName(_fromUtf8("labelMonitor"))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelMonitor.setFont(font)
        
        self.groupBoxInfoGpu = QtGui.QGroupBox(self.centralwidget)
        self.groupBoxInfoGpu.setGeometry(QtCore.QRect(34, 156, 346,316))
        self.groupBoxInfoGpu.setStyleSheet(_fromUtf8("QGroupBox \n"
	"{ \n"
	"border: 2px solid MediumBlue;\n"
	"border-radius: 20px;\n"
	"}"))
        self.groupBoxInfoGpu.setTitle(_fromUtf8(""))
        self.groupBoxInfoGpu.setObjectName(_fromUtf8("groupBoxInfoGpu"))
       
        
        self.groupBoxOverclock = QtGui.QGroupBox(self.centralwidget)
        self.groupBoxOverclock.setGeometry(QtCore.QRect(406, 156, 386,316))
        self.groupBoxOverclock.setStyleSheet(_fromUtf8("QGroupBox \n"
	"{ \n"
	"border: 2px solid MediumBlue;\n"
	"border-radius: 20px;\n"
	"}"))
        self.groupBoxOverclock.setTitle(_fromUtf8(""))
        self.groupBoxOverclock.setObjectName(_fromUtf8("groupBoxOverclock"))
        
        self.VitesseGpu = QtGui.QLabel(self.groupBoxOverclock)
        self.VitesseGpu.setGeometry(QtCore.QRect(10, 0, 130, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Liberation Serif"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.VitesseGpu.setFont(font)
        self.VitesseGpu.setObjectName(_fromUtf8("VitesseGpu"))
        self.label_Dfreq_Gpu = QtGui.QLabel(self.groupBoxOverclock)
        self.label_Dfreq_Gpu.setGeometry(QtCore.QRect(130, 12, 90, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_Dfreq_Gpu.setFont(font)
        self.label_Dfreq_Gpu.setObjectName(_fromUtf8("label_Dfreq_Gpu"))
        self.lcdGPU = QtGui.QLCDNumber(self.groupBoxOverclock)
        self.lcdGPU.setGeometry(QtCore.QRect(220, 12, 72, 30))
        self.lcdGPU.setDigitCount(6)
        self.lcdGPU.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdGPU.setObjectName(_fromUtf8("lcdGPU"))
        self.labelMhzGpu = QtGui.QLabel(self.groupBoxOverclock)
        self.labelMhzGpu.setGeometry(QtCore.QRect(300, 12, 40, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelMhzGpu.setFont(font)
        self.labelMhzGpu.setObjectName(_fromUtf8("labelMhzGpu"))
        self.SliderGpu = QtGui.QSlider(self.groupBoxOverclock)
        self.SliderGpu.setGeometry(QtCore.QRect(5, 45, 370, 26))
        self.SliderGpu.setStyleSheet(_fromUtf8("color: rgb(205, 0, 0);"))
        self.SliderGpu.setSingleStep(2)
        self.SliderGpu.setOrientation(QtCore.Qt.Horizontal)
        self.SliderGpu.setObjectName(_fromUtf8("SliderGpu"))
        
       
        self.VitesseShader = QtGui.QLabel(self.groupBoxOverclock)
        self.VitesseShader.setGeometry(QtCore.QRect(10, 70, 130, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Liberation Serif"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.VitesseShader.setFont(font)
        self.VitesseShader.setObjectName(_fromUtf8("VitesseShader"))
        self.label_Dfreq_Shader = QtGui.QLabel(self.groupBoxOverclock)
        self.label_Dfreq_Shader.setGeometry(QtCore.QRect(130, 82, 90, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_Dfreq_Shader.setFont(font)
        self.label_Dfreq_Shader.setObjectName(_fromUtf8("label_Dfreq_Shader"))
        self.lcdShader = QtGui.QLCDNumber(self.groupBoxOverclock)
        self.lcdShader.setGeometry(QtCore.QRect(220, 82, 72, 30))
        self.lcdShader.setDigitCount(6)
        self.lcdShader.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdShader.setProperty("intValue", 0)
        self.lcdShader.setObjectName(_fromUtf8("lcdShader"))
        self.labelMhzShader = QtGui.QLabel(self.groupBoxOverclock)
        self.labelMhzShader.setGeometry(QtCore.QRect(300, 82, 40, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelMhzShader.setFont(font)
        self.labelMhzShader.setObjectName(_fromUtf8("labelMhzShader"))
        self.SliderShader = QtGui.QSlider(self.groupBoxOverclock)
        self.SliderShader.setEnabled(True)
        self.SliderShader.setGeometry(QtCore.QRect(5, 115, 370, 26))
        self.SliderShader.setAutoFillBackground(False)
        self.SliderShader.setStyleSheet(_fromUtf8("color: rgb(205, 0, 0);"))
        self.SliderShader.setSingleStep(2)
        self.SliderShader.setSliderPosition(0)
        self.SliderShader.setOrientation(QtCore.Qt.Horizontal)
        self.SliderShader.setTickInterval(2)
        self.SliderShader.setObjectName(_fromUtf8("SliderShader"))
        self.Memoire = QtGui.QLabel(self.groupBoxOverclock)
        self.Memoire.setGeometry(QtCore.QRect(10, 140, 130, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Liberation Serif"))
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.Memoire.setFont(font)
        self.Memoire.setObjectName(_fromUtf8("Memoire"))
        self.label_Dfreq_Mem = QtGui.QLabel(self.groupBoxOverclock)
        self.label_Dfreq_Mem.setGeometry(QtCore.QRect(130, 152, 90, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_Dfreq_Mem.setFont(font)
        self.label_Dfreq_Mem.setObjectName(_fromUtf8("label_Dfreq_Mem"))
        self.lcdMem = QtGui.QLCDNumber(self.groupBoxOverclock)
        self.lcdMem.setGeometry(QtCore.QRect(220, 152, 72, 30))
        self.lcdMem.setDigitCount(6)
        self.lcdMem.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdMem.setObjectName(_fromUtf8("lcdMem"))
        self.labelMhzMem = QtGui.QLabel(self.groupBoxOverclock)
        self.labelMhzMem.setGeometry(QtCore.QRect(300, 152, 40, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelMhzMem.setFont(font)
        self.labelMhzMem.setObjectName(_fromUtf8("labelMhzMem")) 
        self.SliderMem = QtGui.QSlider(self.groupBoxOverclock)
        self.SliderMem.setGeometry(QtCore.QRect(5, 185, 370, 26))
        self.SliderMem.setStyleSheet(_fromUtf8("color: rgb(205, 0, 0);"))
        self.SliderMem.setSingleStep(2)
        self.SliderMem.setOrientation(QtCore.Qt.Horizontal)
        self.SliderMem.setObjectName(_fromUtf8("SliderMem"))
        
        self.buttonReset = QtGui.QPushButton(self.groupBoxOverclock)
        self.buttonReset.setGeometry(QtCore.QRect(35, 215, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.buttonReset.setFont(font)
        self.buttonReset.setAutoDefault(False)
        self.buttonReset.setDefault(False)
        self.buttonReset.setFlat(False)
        self.buttonReset.setObjectName(_fromUtf8("buttonReset"))
        self.buttonApply = QtGui.QPushButton(self.groupBoxOverclock)
        self.buttonApply.setGeometry(QtCore.QRect(205, 215, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.buttonApply.setFont(font)
        self.buttonApply.setStyleSheet(_fromUtf8(""))
        self.buttonApply.setDefault(False)
        self.buttonApply.setObjectName(_fromUtf8("buttonApply"))
        
        
        self.labelFan = QtGui.QLabel(self.groupBoxOverclock)
        self.labelFan.setGeometry(QtCore.QRect(28, 265, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.labelFan.setFont(font)
        self.labelFan.setObjectName(_fromUtf8("labelFan"))
        
        self.labelFanVitesse = QtGui.QLabel(self.groupBoxOverclock)
        self.labelFanVitesse.setGeometry(QtCore.QRect(80, 266, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelFanVitesse.setFont(font)
        self.labelFanVitesse.setObjectName(_fromUtf8("labelFanVitesse"))
        
        self.SliderFan = QtGui.QSlider(self.groupBoxOverclock)
        self.SliderFan.setEnabled(True)
        self.SliderFan.setGeometry(QtCore.QRect(5, 285, 370, 26))
        self.SliderFan.setAutoFillBackground(False)
        self.SliderFan.setStyleSheet(_fromUtf8("color: rgb(205, 0, 0);"))
        self.SliderFan.setSingleStep(2)
        self.SliderFan.setSliderPosition(0)
        self.SliderFan.setOrientation(QtCore.Qt.Horizontal)
        self.SliderFan.setTickInterval(2)
        self.SliderFan.setObjectName(_fromUtf8("SliderFan"))
        self.checkBoxFan = QtGui.QCheckBox(self.groupBoxOverclock)
        self.checkBoxFan.setEnabled(True)
        self.checkBoxFan.setGeometry(QtCore.QRect(8, 271, 20, 20))
        self.checkBoxFan.setCheckable(True)
        self.checkBoxFan.setChecked(False)
        self.checkBoxFan.setObjectName(_fromUtf8("checkBoxOptimus"))

        self.nomGpu = QtGui.QLabel(self.centralwidget)
        self.nomGpu.setGeometry(QtCore.QRect(0, 155, 400, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 158, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.nomGpu.setAlignment(QtCore.Qt.AlignCenter)
        self.nomGpu.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.nomGpu.setFont(font)
        self.nomGpu.setObjectName(_fromUtf8("nomGpu"))
        self.Message = QtGui.QLabel(self.centralwidget)
        self.Message.setGeometry(QtCore.QRect(250, 470, 300,60))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 158, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.Message.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Message.setFont(font)
        self.Message.setText(_fromUtf8(""))
        self.Message.setAlignment(QtCore.Qt.AlignCenter)
        self.Message.setObjectName(_fromUtf8("Message"))
        
        
        
        
        self.checkBoxOptimus = QtGui.QCheckBox(self.centralwidget)
        self.checkBoxOptimus.setEnabled(False)
        self.checkBoxOptimus.setGeometry(QtCore.QRect(130, 190, 100, 22))
        self.checkBoxOptimus.setCheckable(True)
        self.checkBoxOptimus.setChecked(False)
        self.checkBoxOptimus.setObjectName(_fromUtf8("checkBoxOptimus"))
        self.checkBoxSli = QtGui.QCheckBox(self.centralwidget)
        self.checkBoxSli.setEnabled(False)
        self.checkBoxSli.setGeometry(QtCore.QRect(220, 190, 50, 22))
        self.checkBoxSli.setCheckable(True)
        self.checkBoxSli.setObjectName(_fromUtf8("checkBoxSli"))
        self.checkBoxVaapi = QtGui.QCheckBox(self.centralwidget)
        self.checkBoxVaapi.setEnabled(False)
        self.checkBoxVaapi.setGeometry(QtCore.QRect(60, 190, 70, 22))
        self.checkBoxVaapi.setCheckable(True)
        self.checkBoxVaapi.setObjectName(_fromUtf8("checkBoxVaapi"))
        self.checkBoxVSync = QtGui.QCheckBox(self.centralwidget)
        self.checkBoxVSync.setEnabled(True)
        self.checkBoxVSync.setGeometry(QtCore.QRect(270, 190, 100, 22))
        self.checkBoxVSync.setCheckable(True)
        self.checkBoxVSync.setChecked(False)
        self.checkBoxVSync.setObjectName(_fromUtf8("checkBoxVSync"))
        
        
        
        self.listWidgetGpu = QtGui.QListWidget(self.centralwidget)
        self.listWidgetGpu.setGeometry(QtCore.QRect(220, 10, 300, 60))
        self.listWidgetGpu.setStyleSheet(_fromUtf8("background-color: rgb(207, 255, 233);"))
        self.listWidgetGpu.setObjectName(_fromUtf8("listWidgetGpu"))
        self.PiloteVersion = QtGui.QLabel(self.centralwidget)
        self.PiloteVersion.setGeometry(QtCore.QRect(5, 200, 200, 65))
        self.PiloteVersion.setStyleSheet(_fromUtf8("border-color: rgb(0, 0, 0);"))
        self.PiloteVersion.setAlignment(QtCore.Qt.AlignCenter)
        self.PiloteVersion.setMargin(2)
        self.PiloteVersion.setObjectName(_fromUtf8("PiloteVersion"))
        self.OpenGlSupport = QtGui.QLabel(self.centralwidget)
        self.OpenGlSupport.setGeometry(QtCore.QRect(210, 200, 200, 65))
        self.OpenGlSupport.setAlignment(QtCore.Qt.AlignCenter)
        self.OpenGlSupport.setMargin(2)
        self.OpenGlSupport.setObjectName(_fromUtf8("OpenGlSupport"))
        self.MemGpu = QtGui.QLabel(self.centralwidget)
        self.MemGpu.setGeometry(QtCore.QRect(5, 270, 200, 65))
        self.MemGpu.setAlignment(QtCore.Qt.AlignCenter)
        self.MemGpu.setMargin(2)
        self.MemGpu.setObjectName(_fromUtf8("MemGpu"))
        self.CudaCore = QtGui.QLabel(self.centralwidget)
        self.CudaCore.setGeometry(QtCore.QRect(210, 270, 200, 65))
        self.CudaCore.setAlignment(QtCore.Qt.AlignCenter)
        self.CudaCore.setMargin(2)
        self.CudaCore.setObjectName(_fromUtf8("CudaCore"))
        self.UGPU = QtGui.QLabel(self.centralwidget)
        self.UGPU.setGeometry(QtCore.QRect(210, 400, 200, 65))
        self.UGPU.setAlignment(QtCore.Qt.AlignCenter)
        self.UGPU.setMargin(2)
        self.UGPU.setObjectName(_fromUtf8("UGPU"))
        self.UMem = QtGui.QLabel(self.centralwidget)
        self.UMem.setGeometry(QtCore.QRect(210, 340, 200, 65))
        self.UMem.setAlignment(QtCore.Qt.AlignCenter)
        self.UMem.setMargin(2)
        self.UMem.setObjectName(_fromUtf8("UMem"))
        self.UPCIE = QtGui.QLabel(self.centralwidget)
        self.UPCIE.setGeometry(QtCore.QRect(5, 400, 200, 65))
        self.UPCIE.setAlignment(QtCore.Qt.AlignCenter)
        self.UPCIE.setMargin(2)
        self.UPCIE.setObjectName(_fromUtf8("UPCIE"))
        self.Temp = QtGui.QLabel(self.centralwidget)
        self.Temp.setGeometry(QtCore.QRect(5, 340, 200, 65))
        self.Temp.setAlignment(QtCore.Qt.AlignCenter)
        self.Temp.setMargin(2)
        self.Temp.setObjectName(_fromUtf8("Temp"))
        self.label_Img = QtGui.QLabel(self.centralwidget)
        self.label_Img.setGeometry(QtCore.QRect(554, 5, 241, 140))
        self.label_Img.setObjectName(_fromUtf8("label_Img"))
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFichier = QtGui.QMenu(self.menubar)
        self.menuFichier.setObjectName(_fromUtf8("menuFichier"))
        self.menuMonitor = QtGui.QMenu(self.menubar)
        self.menuMonitor.setObjectName(_fromUtf8("menuMonitor"))
        #~ self.menuAide = QtGui.QMenu(self.menubar)
        #~ self.menuAide.setObjectName(_fromUtf8("menuAide"))
        MainWindow.setMenuBar(self.menubar)
        
        self.actionLoadProfile = QtGui.QAction(MainWindow)
        self.actionLoadProfile.setObjectName(_fromUtf8("actionLoadProfile"))
        self.actionSaveProfile = QtGui.QAction(MainWindow)
        self.actionSaveProfile.setObjectName(_fromUtf8("actionSaveProfile"))
        self.actionPref = QtGui.QAction(MainWindow)
        self.actionPref.setObjectName(_fromUtf8("actionPref"))
        self.actionQuitter = QtGui.QAction(MainWindow)
        self.actionQuitter.setObjectName(_fromUtf8("actionQuitter"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionStartMonitor = QtGui.QAction(MainWindow)
        self.actionStartMonitor.setObjectName(_fromUtf8("actionStartMonitor"))
        self.actionConfigureMonitor = QtGui.QAction(MainWindow)
        self.actionConfigureMonitor.setObjectName(_fromUtf8("actionConfigureMonitor"))
        
        self.menuFichier.addAction(self.actionLoadProfile)
        self.menuFichier.addAction(self.actionSaveProfile)
        self.menuFichier.addAction(self.actionPref)
        self.menuFichier.addAction(self.actionAbout)
        self.menuFichier.addAction(self.actionQuitter)
        self.menuMonitor.addAction(self.actionStartMonitor)
        self.menuMonitor.addAction(self.actionConfigureMonitor)
        
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuMonitor.menuAction())
        #~ self.menubar.addAction(self.menuAide.menuAction())
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Nvidiux", None))
        self.Memoire.setText(_translate("MainWindow", "Mémoire", None))
        self.VitesseShader.setText(_translate("MainWindow", "Shader", None))
        self.VitesseGpu.setText(_translate("MainWindow", "Gpu", None))
        self.title.setText(_translate("MainWindow", "Nvidiux", None))
        self.buttonReset.setText(_translate("MainWindow", "Reset", None))
        self.buttonApply.setText(_translate("MainWindow", "Appliquer", None))
        self.about.setText(_translate("MainWindow", "Version XXX", None))
        self.buttonAbout.setText(_translate("MainWindow", "i", None))
        self.labelFanVitesse.setText(_translate("MainWindow", "Auto",None))
        self.labelFan.setText(_translate("MainWindow", "Fan", None))
        self.buttonStartMonitor.setText(_translate("MainWindow", "Start", None))
        self.buttonConfigureMonitor.setText(_translate("MainWindow", "Configurer", None))
        self.labelMonitor.setText(_translate("MainWindow", "Moniteur", None))
        self.buttonLoadProfile.setText(_translate("MainWindow", "Charger", None))
        self.buttonSaveProfile.setText(_translate("MainWindow", "Enregister", None))
        self.labelProfile.setText(_translate("MainWindow", "Profil", None))
        self.nomGpu.setText(_translate("MainWindow", "Nom gpu", None))
        self.labelMhzGpu.setText(_translate("MainWindow", "Mhz", None))
        self.labelMhzShader.setText(_translate("MainWindow", "Mhz", None))
        self.labelMhzMem.setText(_translate("MainWindow", "Mhz", None))
        self.checkBoxOptimus.setText(_translate("MainWindow", "Optimus", None))
        self.checkBoxSli.setText(_translate("MainWindow", "Sli", None))
        self.checkBoxVaapi.setText(_translate("MainWindow", "Vaapi", None))
        self.checkBoxVSync.setText(_translate("MainWindow", "VSync", None))
        self.PiloteVersion.setText(_translate("MainWindow", "Version pilote", None))
        self.OpenGlSupport.setText(_translate("MainWindow", "OpenGl Support", None))
        self.MemGpu.setText(_translate("MainWindow", "Mem Gpu", None))
        self.CudaCore.setText(_translate("MainWindow", "Cudacore", None))
        self.UGPU.setText(_translate("MainWindow", "Gpu utilisation", None))
        self.UMem.setText(_translate("MainWindow", "Mem utilisation", None))
        self.UPCIE.setText(_translate("MainWindow", "Pcie utili", None))
        self.Temp.setText(_translate("MainWindow", "Temp", None))
        self.label_Img.setText(_translate("MainWindow", "Img", None))
        self.label_Dfreq_Gpu.setText(_translate("MainWindow", "Gpu", None))
        self.label_Dfreq_Shader.setText(_translate("MainWindow", "Shader", None))
        self.label_Dfreq_Mem.setText(_translate("MainWindow", "Mem", None))
        self.menuFichier.setTitle(_translate("MainWindow", "Fichier", None))
        #~ self.menuAide.setTitle(_translate("MainWindow", "Aide", None))
        self.menuMonitor.setTitle(_translate("MainWindow", "Moniteur", None))
        self.actionQuitter.setText(_translate("MainWindow", "Quitter", None))
        self.actionStartMonitor.setText(_translate("MainWindow", "Start", None))
        self.actionConfigureMonitor.setText(_translate("MainWindow", "Configurer", None))
        self.actionAbout.setText(_translate("MainWindow", "A Propos", None))
        self.actionPref.setText(_translate("MainWindow", "Préférences", None))
        self.actionLoadProfile.setText(_translate("MainWindow", "Charger", None))
        self.actionSaveProfile.setText(_translate("MainWindow", "Enregistrer", None))
       
        
