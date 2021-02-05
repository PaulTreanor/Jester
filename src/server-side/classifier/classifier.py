import pandas as pd 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import LocalOutlierFactor

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
	classification = clf.predict([gesture_data[1:]])
	conf = lof.decision_function([gesture_data[1:]])
	return classification[0], conf[0]


if __name__ == "__main__":
	test_object = ['peace_7_keypoints', '0', '0', '-2.031', '2.902', '-3.822', '6.485', '-3.108', '10.094', '-0.447', '11.963', '-2.707', '10.535', '-3.939', '14.32', '-4.366', '17.425', '-4.752', '20.21', '-0.001', '10', '0.467', '15.532', '0.921', '18.88', '1.756', '22.048', '1.964', '8.882', '2.199', '12.169', '0.179', '9.861', '-0.978', '7.693', '3.931', '7.764', '3.347', '9.546', '1.486', '8.039', '0.328', '5.872', 'peace']
	test_object = [float(item) for item in test_object[1:-1]]
	clf = knn()
	print(clf.predict([test_object]))


