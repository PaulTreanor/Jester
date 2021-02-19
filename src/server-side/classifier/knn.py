import pandas as pd 
import csv
import math
from scipy.spatial import distance
#from classifiers.anomoly_detection import get_conf_ldofs
from sklearn.neighbors import LocalOutlierFactor


class knn:
	# CLASS VARIABLES 
	#k = 3
	def __init__(self, k=5):
		self.k = k

	def get_knn(self, gesture_data):
		# nn is list of k nearest neighbours tuples in the form (distance, class_name, feature_coordinates, filename)
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
				file_name = line[0]
				class_name = line[-1]
				features = line[1:-1]
				features = [float(item) for item in features]
				gesture_data = [float(item) for item in gesture_data]
				
				dist = distance.euclidean(features, gesture_data)
				
				# Prevent infinite loop in LoF anomoly detector 
				if dist == 0.0:
					continue

				if len(nn) < self.k:
					nn.append((dist, class_name, features))
				else:
					distance_list = [item[0] for item in nn]
					min_index = distance_list.index(max(distance_list))
					if nn[min_index][0] > dist:
						nn[min_index] = (dist, class_name, features)
			return nn


	def predict(self, gesture_data):	
		# List of k nearest neighbours in the form (distance, classification)
		nn = self.get_knn(gesture_data[0])

		# Get most common class name
		class_list = [item[1] for item in nn]
		classification = max(set(class_list), key=class_list.count)
		#print(conf)
		#print(nn)
		return classification, nn


if __name__ == '__main__':
	gesture_data = ['0', '0', '-2.031', '2.902', '-3.822', '6.485', '-3.108', '10.094', '-0.447', '11.963', '-2.707', '10.535', '-3.939', '14.32', '-4.366', '17.425', '-4.752', '20.21', '-0.001', '10', '0.467', '15.532', '0.921', '18.88', '1.756', '22.048', '1.964', '8.882', '2.199', '12.169', '0.179', '9.861', '-0.978', '7.693', '3.931', '7.764', '3.347', '9.546', '1.486', '8.039', '0.328', '5.872']
	clf = knn()
	print(clf.predict(gesture_data))