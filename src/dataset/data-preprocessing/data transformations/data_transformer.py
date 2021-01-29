import csv
from gesture_plotter import plot

def translate(hand_gesture):
	x_dif = hand_gesture[1]
	y_dif = hand_gesture[2]
	x = hand_gesture[1::2] 
	y = hand_gesture[2::2]

	hand_gesture = [hand_gesture[0]]
	i = 0
	while i < len(x):
		x[i] = round(x[i] - x_dif, 3)
		
		hand_gesture.append(x[i])
		y[i] = round(y[i] - y_dif, 3)
		
		hand_gesture.append(y[i])
		i += 1

	return hand_gesture


def transform_dataset():
	with open("..\\cleaned_dataset.csv", "r", newline='') as dataset:
		csv_reader = csv.reader(dataset)

		with open('transformed_dataset.csv', 'w', newline='') as transformed_dataset:
			csv_writer = csv.writer(transformed_dataset)
			for line in csv_reader:
				#convert coords from string to floats
				line = line[0] + [float(item) for item in line[1:]]
				#translate coordinates
				line = translate(line)
				#enlargement 
				#rotation
			#	csv_writer.writerow(line)



if __name__ == '__main__':					
	#transform_dataset()
	test_object = ['palm_108_keypoints', 550.552, 2280.4, 621.377, 2209.57, 678.713, 2125.25, 722.557, 2013.96, 800.128, 1943.13, 638.241, 1990.35, 634.868, 1852.07, 614.632, 1761.01, 587.651, 1673.32, 564.042, 1986.98, 550.552, 1828.46, 543.806, 1720.54, 523.57, 1632.85, 499.962, 1986.98, 496.589, 1835.21, 489.844, 1747.52, 476.353, 1666.57, 439.254, 2003.84, 419.018, 1889.17, 419.018, 1828.46, 419.018, 1757.63]
	
	########### AD HOC TRANSLATION TESTS #############
	test_object = (translate(test_object))
	print(test_object)
	plot(test_object)
