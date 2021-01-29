import csv
from gesture_plotter import plot
import math

#euclidean distance
def dist(p1, p2):
	return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)


def translate(hand_gesture):
	x_dif = hand_gesture[1]
	y_dif = hand_gesture[2]
	x = hand_gesture[1::2] 
	y = hand_gesture[2::2]

	#can remove [i] within the while loop I think#####################
	hand_gesture = [hand_gesture[0]]
	i = 0
	while i < len(x):
		x[i] = round(x[i] - x_dif, 3)	
		hand_gesture.append(x[i])

		y[i] = round(y[i] - y_dif, 3)		
		hand_gesture.append(y[i])
		i += 1
	return hand_gesture


def enlarge(hand_gesture):  ##########################add rounding to this shit ...or leave it to the end? 
	x = hand_gesture[1::2] 
	y = hand_gesture[2::2]
	# find the scale factor 
	# we want to normalise the distances between point 0 and point 9 to 10 units
	p_0 = (x[0], y[0])
	p_9 = (x[9], y[9])
	scale_factor = 10/dist(p_0, p_9)

	i = 1
	while i < len(hand_gesture):
		hand_gesture[i] = hand_gesture[i]*scale_factor
		i +=1
	return hand_gesture
 

def rotate(hand_gesture):
	x = hand_gesture[1::2] 
	y = hand_gesture[2::2]
	hand_gesture = [hand_gesture[0]]
	#how much does it need to be rotated by? 
	p_9 = (x[9], y[9])
	dotproduct = sum((a*b) for a, b in zip((0,10), p_9))

	degrees = math.acos(dotproduct / 100)
	#degrees = degrees * math.pi / 180

	#rotate it by that much 
	i = 0
	while i < len(x):
		#rotate x and y
		tmp = x[i]
		x[i] = math.cos(degrees) * x[i] - math.sin(degrees) * y[i]
		y[i] = math.sin(degrees) * tmp + math.cos(degrees) * y[i]
		#add x and y to list 
		hand_gesture.extend([x[i], y[i]])
		i+=1
	return hand_gesture




def transform_dataset():
	with open("..\\cleaned_dataset.csv", "r", newline='') as dataset:
		csv_reader = csv.reader(dataset)

		with open('transformed_dataset.csv', 'w', newline='') as transformed_dataset:
			csv_writer = csv.writer(transformed_dataset)
			csv_writer.writerow(next(csv_reader))
			firstline = True
			for line in csv_reader:
				if firstline:    #skip first line
					firstline = False
					continue
				#convert coords from string to floats
				line = [line[0]] + [float(item) for item in line[1:]]
				#translate coordinates
				line = translate(line)
				#enlargement 
				line = enlarge(line)
				#rotation
				line = rotate(line)
				csv_writer.writerow(line)



if __name__ == '__main__':					
	transform_dataset()
	
	############ AD HOC TRANSLATION TESTS ###############
	#test_object = ['palm_108_keypoints', 550.552, 2280.4, 621.377, 2209.57, 678.713, 2125.25, 722.557, 2013.96, 800.128, 1943.13, 638.241, 1990.35, 634.868, 1852.07, 614.632, 1761.01, 587.651, 1673.32, 564.042, 1986.98, 550.552, 1828.46, 543.806, 1720.54, 523.57, 1632.85, 499.962, 1986.98, 496.589, 1835.21, 489.844, 1747.52, 476.353, 1666.57, 439.254, 2003.84, 419.018, 1889.17, 419.018, 1828.46, 419.018, 1757.63]
	#test_object = translate(test_object)
	#print(test_object)
	#plot(test_object)

	############## AD HOC ENLARGEMENT TESTS ##############
	#test_object = ['palm_108_keypoints', 0.0, 0.0, 70.825, -70.83, 128.161, -155.15, 172.005, -266.44, 249.576, -337.27, 87.689, -290.05, 84.316, -428.33, 64.08, -519.39, 37.099, -607.08, 13.49, -293.42, 0.0, -451.94, -6.746, -559.86, -26.982, -647.55, -50.59, -293.42, -53.963, -445.19, -60.708, -532.88, -74.199, -613.83, -111.298, -276.56, -131.534, -391.23, -131.534, -451.94, -131.534, -522.77]
	#test_object = enlarge(test_object)
	#print(test_object)
	#plot(test_object)

	############### AD HOC ROTATION TESTS ###############
	#test_object = ['palm_108_keypoints', 0.0, 0.0, 2.411228507145167, -2.411398731536776, 4.363225650606873, -5.282062871635336, 5.855889295750152, -9.070917380074244, 8.496784552054532, -11.48231611161102, 2.985361335164879, -9.87471695725317, 2.8705279605852723, -14.582442731598862, 2.1815958028642757, -17.682569351586704, 1.2630309408623868, -20.667964731629908, 0.45926540856178333, -9.989448197197811, 0.0, -15.386242308777788, -0.22966674915921353, -19.060365577272055, -0.9185989068802104, -22.045760957315256, -1.7223303943024924, -9.989448197197811, -1.837163768882099, -15.156439380105287, -2.0667964731629906, -18.141834760148488, -2.526095926603096, -20.89776766030241, -3.789126867465483, -9.415451548691387, -4.47805902518648, -13.319377745858155, -4.47805902518648, -15.386242308777788, -4.47805902518648, -17.797641040314563]
	#plot(test_object)
	#test_object = rotate(test_object)
	#print(test_object)
	#plot(test_object)