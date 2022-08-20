import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


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