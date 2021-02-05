import pandas as pd 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import LocalOutlierFactor
import csv

def knn():
	df = pd.read_csv("transformed_dataset.csv")
	x = df.drop(["image_name", "class_name"], axis=1)
	y = df.class_name

	# Accuracy drops slighty if k > 5
	clf = KNeighborsClassifier(n_neighbors=4)
	clf.fit(x, y)

	# Find conf value to recognise OOD images
	lof = LocalOutlierFactor(novelty=True)
	lof.fit(x)

	return clf, lof


def classify(gesture_data):
	clf, lof = knn()
	classification = clf.predict(gesture_data)
	conf = lof.decision_function(gesture_data)
	return classification[0], conf[0]


# Lowest classification confidence value in the dataset will be the max value of min conf 
# Confidence values will be slightly different for various classifiers (even if values are normalised to be between 0 and 1), so this must be rerun when a new one is built
def find_min_conf():
	with open("transformed_dataset.csv", "r", newline='') as dataset:
		csv_reader = csv.reader(dataset)

		#for line in dataset 
			#classify it
			#find conf
			#record name of file 
			#save min conf and file name for inspection 


		max_min_conf = ("line name", 100000)      #max value of min_conf
		firstline = True
		for line in csv_reader:
			# Skip header line 
			if firstline:    
				firstline = False
				continue
			del line[-1]
			line_name = line[0]
			line = [float(item) for item in line[1:]]
			line = [line]
			#print(line)

			classification, conf = classify(line)
			if conf < max_min_conf[1]:
				max_min_conf = (line_name, conf)

	print(max_min_conf[0] + str(max_min_conf[1]))




if __name__ == "__main__":
#	test_object = ['peace_7_keypoints', '0', '0', '-2.031', '2.902', '-3.822', '6.485', '-3.108', '10.094', '-0.447', '11.963', '-2.707', '10.535', '-3.939', '14.32', '-4.366', '17.425', '-4.752', '20.21', '-0.001', '10', '0.467', '15.532', '0.921', '18.88', '1.756', '22.048', '1.964', '8.882', '2.199', '12.169', '0.179', '9.861', '-0.978', '7.693', '3.931', '7.764', '3.347', '9.546', '1.486', '8.039', '0.328', '5.872', 'peace']
#	test_object = [float(item) for item in test_object[1:-1]]
#	clf = knn()
#	print(clf.predict([test_object]))
	find_min_conf()

