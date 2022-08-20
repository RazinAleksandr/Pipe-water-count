from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets, QtCore, QtGui
import sys
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 710)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setStyleSheet("")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(1055, 50, 60, 25))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(1055, 95, 60, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(1055, 140, 60, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(1055, 185, 60, 25))
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(1055, 230, 60, 25))
        self.lineEdit_6.setObjectName("lineEdit_6")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(870, 50, 200, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(870, 95, 200, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(870, 140, 220, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(870, 185, 200, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(870, 230, 200, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(870, 318, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(1040, 320, 150, 50))
        self.listWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listWidget.setObjectName("listWidget")

        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 50, 840, 450))
        self.graphicsView.setObjectName("graphicsView")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 610, 500, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")

        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(590, 560, 80, 30))
        self.doubleSpinBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.doubleSpinBox.setSingleStep(0.1)
        self.doubleSpinBox.setObjectName("doubleSpinBox")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(190, 562, 380, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(590, 518, 80, 30))
        self.doubleSpinBox_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.doubleSpinBox_2.setSingleStep(0.1)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(190, 520, 385, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 660, 300, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setObjectName("pushButton_3")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1130, 50, 50, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1130, 95, 40, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(1130, 140, 50, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(1130, 185, 40, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")

        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(1130, 230, 50, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")

        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(0, 10, 1200, 25))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")

        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(1130, 275, 40, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")

        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(1055, 275, 60, 25))
        self.lineEdit_7.setObjectName("lineEdit_7")

        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(870, 275, 200, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")

        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(885, 595, 190, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")

        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(1085, 595, 60, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")

        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(1140, 595, 60, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(880, 630, 280, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(880, 580, 280, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        
        # Graph canvas
        self.new_label = QtWidgets.QLabel(self.centralwidget)
        self.new_label.setScaledContents(True)
        self.new_label.setGeometry(QtCore.QRect(10, 50, 840, 450))
        self.new_label.setStyleSheet('border: 1px solid black')
        self.new_label.setObjectName("new_label")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Setting default values
        self.lineEdit.setText('25')
        self.lineEdit_2.setText('850')
        self.lineEdit_3.setText('52')
        self.lineEdit_4.setText('0.406')
        self.lineEdit_6.setText('1000')
        self.lineEdit_7.setText('1')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Kinematic viscosity"))
        self.label_2.setText(_translate("MainWindow", "Oil density"))
        self.label_3.setText(_translate("MainWindow", "Surface tension"))
        self.label_4.setText(_translate("MainWindow", "Inside diameter"))
        self.label_5.setText(_translate("MainWindow", "Water density"))
        self.pushButton.setText(_translate("MainWindow", "Upload file"))
        self.pushButton_2.setText(_translate("MainWindow", "Draw a graph"))
        self.label_7.setText(_translate("MainWindow", "Threshold to visualize water accumulation:"))
        self.label_8.setText(_translate("MainWindow", "Tilt angle visualization threshold:"))
        self.pushButton_3.setText(_translate("MainWindow", "Save the result in excel format"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p>sSt</p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p>kg/м<span style=\" vertical-align:super;\">3</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p>mN/m </p><p><br/></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p>m</p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p>kg/m<span style=\" vertical-align:super;\">3</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Determining the amount of water in the main oil pipeline</p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p>m/s</p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "Flow rate"))
        self.label_16.setText(_translate("MainWindow", "Total volume of water:"))


# Input file processing
def data_processing(file_name):
	data = pd.read_excel(file_name,
        header=None,
        names=['расстояние от начала трассы',
               'Отметка верха трубопровода'])
	data_drop = data.copy()
	maxim = data.iloc[0, 0]
	for i in range(1, max(data.index)):
	  if data.iloc[i, 0] > maxim:
	    maxim = data.iloc[i, 0]
	  else:
	    data_drop = data_drop.drop(index=i)

	return data_drop


# Creating a list consisting of data in pairs for each
def create_data_pairs(data):
	# Distance from the beginning of the pipe to the beginning of the section, m
	L = data.loc[:, 'расстояние от начала трассы'].to_numpy()
	# Height of the beginning of the section, m
	Z = data.loc[:, 'Отметка верха трубопровода'].to_numpy()
	# Data in L-Z pairs
	LZ = []
	for i in range(len(L)):
		LZ.append([L[i], Z[i]])
	return L, Z, LZ


# Identification of ascending sections of the pipe
def upward_section(LZ):
	sections = {}
	lst = []
	j = 0
	for i in range(len(LZ) - 1):
		if LZ[i][1] <= LZ[i + 1][1]:
			if LZ[i] not in lst:
				lst.append(LZ[i])
			lst.append(LZ[i + 1])
		else:
			if len(lst) > 0:
				sections[j] = lst
			lst = []
			j += 1
	if len(lst) > 0:
		sections[j] = lst
	return sections


# Calculation of the average ascending section length and angles of ascent
def mean_section(sections):
	sections_length = {}
	i = 0 
	for key, value in sections.items():
		if len(value) > 1:
			sections_length[i] = [value[-1][0] - value[0][0]]  # Length of ascending section
			sections_length[i].append(value[0][0])  # Removing the beginning of the ascending section
			
			# Calculation of the angle of ascent of the ascending section
			max_angle = 0
			for j in range(len(value) - 1):
				angle = math.degrees(math.atan((value[j + 1][1] - value[j][1]) / 
								   (value[j + 1][0] - value[j][0])))
				if angle > max_angle:
					max_angle = angle

			sections_length[i].append(max_angle)

			i += 1
	return sections_length


# A function that draws a graph with segmentation
def draw_plot(processed_data, result_df, shape, mean_sections_length, min_water, min_angle):
	bar_data = result_df.iloc[:, [0, 1, -1]]
	bar_data_drop = bar_data.copy()

	# Clearing the data from zero values of water accumulation
	for i in range(0, max(bar_data.index)):
	  if bar_data.iloc[i][-1] == 0:
	  	bar_data_drop = bar_data_drop.drop(index=i)

	bar_data = bar_data_drop

	X = []
	Y = []
	
	for i, row in bar_data.iterrows():
		lin = np.linspace(row[1], row[1] + row[0], int(row[0]) + 1, True).tolist()
		X += lin
		Y += np.full((1,len(lin)), row[-1]).tolist()[0]
	
	# create figure and axis objects with subplots()
	fig, ax = plt.subplots(figsize=shape)

	ax.set_title("Pipeline profile" ,size=15)

	# make first plot
	plt.ylim(0, 250)
	ax.plot(np.array(processed_data.iloc[:,0]),
		 np.array(processed_data.iloc[:,1]),
		 color='black')

	# Paint the ascending sections of the trace profile
	for key, value in mean_sections_length.items():
		if value[2] >= min_angle:
			ax.axvspan(value[1], value[1] + value[0], color="red", alpha=0.3)

	# set x-, y- axis labels
	ax.set_xlabel('Remoteness of the section', 
			fontsize = 14)
	ax.set_ylabel("High marks",
			color='black',
			fontsize=14)
	
	# twin object for two different y-axis on the sample plot
	ax2=ax.twinx()
	
	# make a plot with different y-axis using second axis object
	plt.ylim(min_water, max(Y) * 3.5)  # Range of the axis of the water accumulation
	ax2.bar(X, 
		 Y,
		 width=1,
		 color="blue")
	
	ax2.set_ylabel('Volume of water in the cluster',
				   color="black",
				   fontsize=14)

	# save the plot as a file
	fig.savefig('prof.jpg',
	            format='jpeg',
	            bbox_inches='tight')	
	
	return bar_data


''' Calculation algorithm '''
def raschet_params(Q, d, v):
	# 1 Reynolds number
	Re = 4 * Q / (math.pi * d * v)

	# 2 Relative roughness of pipes
	e = 0.2 * 10 ** (-3) / d

	# 3 Transient Reynolds number
	ReI = 17.5 / e

	# 4 Hydraulic resistance coefficient
	if Re <= ReI:
		A = 0.3164
		m = 0.25
	elif Re > ReI:
		A = 0.206 * e ** 0.15
		m = 0.1

	lam = A / Re ** m

	return lam


# I Checking the possibility of the existence of an accumulation
# of water in the ascending section

# An accumulation exists if the inequality:
def cluster_check(Q, d, v, alpha, g, lam, rv, rn):
	if alpha == 0:
		return 0
	a1 = 4 * Q / (math.pi * d ** 2)
	Kb = 0.1 * (v * 10 ** 6) ** 0.36 * (math.sin(math.radians(alpha))) ** (-0.33)  # Calculation coefficient, 
	                                               				     # where alpha is the angle of ascent of the section
	a2 = Kb * (g * d / lam * (rv / rn - 1) * math.sin(math.radians(alpha))) ** (1/2)
	if a1 < a2:
		V_water = depth_finder(g, Q, rv, rn, alpha, d, v, lam)
		return V_water
	else:
		return 0


# II Determining the volume of water in the upstream section
# 5 Determining the normal flow depth Hh
# above the water accumulation 
# (by successive approximations)
def depth_finder(g, Q, rv, rn, alpha, d, v, lam):
	# The initial approximate value of the desired H
	H = 0.05

	# Finding convergence
	while True:
		if H <= 0.5 * d:
			if 1 - 2 * H / d > 1:
				print('Сходимость не достигнута!', 'H=', H, 'condition=', condition)
				return 0
			theta = math.degrees(math.acos(1 - 2 * H / d))
			Xh = d * math.radians(theta)
			Fh = 0.25 * d ** 2 * (math.radians(theta) - (1 - 2 * H/ d) * math.sin(math.radians(theta)))
		else:
			if 2 * H / d - 1 > 1:
				print('Сходимость не достигнута!', 'H=', H, 'condition=', condition)
				return 0
			theta = math.degrees(math.acos(2 * H / d - 1))
			Xh = d * (math.pi - math.radians(theta))
			Fh = 0.25 * d ** 2 * (math.pi - math.radians(theta) + (2 * H / d - 1) * math.sin(math.radians(theta)))
		
		# F1
		cond_1 = lam * Xh / Fh ** 3
		# F2
		cond_2 = 8 * g / Q ** 2 * (rv / rn - 1) * math.sin(math.radians(alpha))

		condition = abs(cond_2 - cond_1) / cond_2
		
		if condition <= 0.005:
			# 6 Average height of water accumulation
			h_mean = 2 / 3 * (d - H)

			# 7 Calculated length of water accumulation
			l_mean = 30 * d
			# 7.1 Defining a new angle

			H_mean = d - h_mean

			if H_mean <= 0.5 * d:
				if 1 - 2 * H_mean / d > 1:
					return 0, H, 0, 0, 0, 0, 0, 0, 0
				psi = math.degrees(math.acos(1 - 2 * H_mean / d))
				FH_mean = 0.25 * d ** 2 * (math.radians(psi) - (1 - 2 * H_mean/ d) * math.sin(math.radians(psi)))
			else:
				if 2 * H_mean / d - 1 > 1:
					return 0, H, 0, 0, 0, 0, 0, 0, 0
				psi = math.degrees(math.acos(2 * H_mean / d - 1))
				FH_mean = 0.25 * d ** 2 * (math.pi - math.radians(psi) + (2 * H_mean / d - 1) * math.sin(math.radians(psi)))

			V_mean = (math.pi * d ** 2 / 4 - FH_mean) * l_mean

			return V_mean

		else:
			H += 0.0001


def calculate(file_name, v , rn, sigma, d, rv, g, Q, min_water, min_angle):
	data = data_processing(file_name)  # Input file processing and data table creation

	L, Z, LZ = create_data_pairs(data)  # Creating a list containing the data of each point in pairs

	up_sections = upward_section(LZ)  # Creating a dictionary consisting only of ascending sections
	
	print(f'Количество восходящих участков: {len(up_sections)}')

	mean_sections_length = mean_section(up_sections)  # Operations on ascending sections and dictionary creation
	
	lam = raschet_params(Q, d, v)  # Calculation of basic parameters, hydraulic resistance coefficient

	for key, value in mean_sections_length.items():
		mean_sections_length[key].append(cluster_check(Q, d, v, value[-1], g, lam, rv, rn))  # Calculation of water volume in each area

	result_df = pd.DataFrame.from_dict(mean_sections_length, 
						orient='index',
						columns=['Длина участка',
							  'Удаленность участка',
							  'Угол подъема участка',
							  'Объем воды в скоплении'])

	V_itog = round(result_df['Объем воды в скоплении'].sum(), 3)

	draw_plot(data, result_df, (15, 15), mean_sections_length, min_water, min_angle)
	
	return result_df, V_itog


class Application(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(Application, self).__init__()

		self.setupUi(self)
		self.file_names = []
		self.pushButton.clicked.connect(self.browse_folder)
		
		self.listWidget.itemClicked.connect(self.button_enable)

		self.pushButton_2.clicked.connect(lambda: self.graph_build(self.listWidget.currentItem().text(),
																   float(self.lineEdit.text()) * 10 ** (-6),
																   float(self.lineEdit_2.text()),
																   float(self.lineEdit_3.text()) * 10 ** (-3),
																   float(self.lineEdit_4.text()),
																   float(self.lineEdit_6.text()),
																   float(9.8),
																   float(self.lineEdit_7.text())))

		self.pushButton_3.clicked.connect(self.excel_upload)


	# Browse data file
	def browse_folder(self):
		file_name = QtWidgets.QFileDialog.getOpenFileNames(self, 'Select the data file')[0]
		if file_name and file_name not in self.file_names:  # do not continue execution if the user has not selected a file
			self.listWidget.addItem(file_name[0].split('/')[-1])
			self.file_names.append(file_name)


	# Choosing file for calculating
	def button_enable(self):
		self.pushButton_2.setEnabled(True)


	# Calculating and graph build
	def graph_build(self, file_name, v , rn, sigma, d, rv, g, c):
		self.Q = (c * math.pi * d ** 2) / 4

		self.result_df, self.V_itog = calculate(file_name, 
											   		  v, 
													  rn, 
													  sigma, 
													  d, 
													  rv, 
													  g, 
													  self.Q, 
													  float(self.doubleSpinBox.text().replace(',', '.')), 
													  float(self.doubleSpinBox_2.text().replace(',', '.')))
		
		pixmap = QPixmap('prof.jpg')
		self.new_label.setPixmap(pixmap)
		self.label_17.setText(str(self.V_itog))
		self.label_18.setText("<html><head/><body><p>m<span style=\" vertical-align:super;\">3</span></p></body></html>")
		self.pushButton_3.setEnabled(True)


	# Upload result file to excel format
	def excel_upload(self):
		self.result_df.to_excel('result_df.xlsx')


def main():
	app = QtWidgets.QApplication(sys.argv)  
	window = Application()
	window.show()
	app.exec_()


if __name__ == '__main__':
	main()