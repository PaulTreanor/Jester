import pandas as pd 
import csv
import math
from scipy.spatial import distance

#euclian distance of lines
def get_distance(line_feeature, gesure_features):
	## listy contains (x-y)**2, (x1-y1)**2 part of euclidian distance function, before summing and squarerooting
	listy = []
	for x,y in zip(line_feeature, gesure_features):
		listy.append((x + y)**2)
	distance = math.sqrt(sum(listy))
	return distance 

class knn:
	def __init__(self, k=5):
		self.k = k



	# Creating fit method so the classifier can be classed from same method as the library classifier, which uses a fit method
	# both paramaters are pd dataframes
	#def fit(features, classifications):
	#	self.features = features 
	#	self.classifications = classifications




	def get_knn(self, gesture_data):
		#nn is list of k nearest neighbours tuples in the form (distance, class_name)
		nn = []
		# Note: CSV path needs to change if calling from __main__
		with open("transformed_dataset.csv", "r", newline="") as dataset:
			csv_reader = csv.reader(dataset)
			# Skip header line
			first_line = True
			for line in csv_reader:
				if first_line:    
					first_line = False
					continue
				class_name = line[-1]
				features = line[1:-1]
				features = [float(item) for item in features]
				gesture_data = [float(item) for item in gesture_data]

			
				#distance = get_distance(features, gesture_data)
				dist = distance.euclidean(features, gesture_data)
				
				if len(nn) < self.k:
					nn.append((dist, class_name))
				else:
					distance_list = [item[0] for item in nn]
					min_index = distance_list.index(max(distance_list))
					if nn[min_index][0] > dist:
						nn[min_index] = (dist, class_name)
			return nn


	def predict(self, gesture_data):	# Gesture data will be list of lists	
		# List of k nearest neighbours in the form (distance, classification)
		nn = self.get_knn(gesture_data[0])
		print(nn)
		# Get most common class name (what do if 2 have same # of occurances?)
		class_list = [item[1] for item in nn]
		most_freq_class = max(set(class_list), key=class_list.count)
		return most_freq_class, 1   #hard coding conf value for now



if __name__ == '__main__':
	gesture_data = ['0', '0', '-2.031', '2.902', '-3.822', '6.485', '-3.108', '10.094', '-0.447', '11.963', '-2.707', '10.535', '-3.939', '14.32', '-4.366', '17.425', '-4.752', '20.21', '-0.001', '10', '0.467', '15.532', '0.921', '18.88', '1.756', '22.048', '1.964', '8.882', '2.199', '12.169', '0.179', '9.861', '-0.978', '7.693', '3.931', '7.764', '3.347', '9.546', '1.486', '8.039', '0.328', '5.872']
	clf = knn(5)
	print(clf.predict(gesture_data))