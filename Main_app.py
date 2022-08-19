import design  # This is the file of current app design
import utils  # This is the file of calculating functions
import sys
import math
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets


class Application(QtWidgets.QMainWindow, design.Ui_MainWindow):
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
		file_name = QtWidgets.QFileDialog.getOpenFileNames(self, 'Выберите файл с данными')[0]
		if file_name and file_name not in self.file_names:  # do not continue execution if the user has not selected a file
			self.listWidget.addItem(file_name[0].split('/')[-1])
			self.file_names.append(file_name)


	# Choosing file for calculating
	def button_enable(self):
		self.pushButton_2.setEnabled(True)


	# Calculating and graph build
	def graph_build(self, file_name, v , rn, sigma, d, rv, g, c):
		self.Q = (c * math.pi * d ** 2) / 4

		self.result_df, self.V_itog = utils.calculate(file_name, 
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
		self.label_18.setText("<html><head/><body><p>м<span style=\" vertical-align:super;\">3</span></p></body></html>")
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
