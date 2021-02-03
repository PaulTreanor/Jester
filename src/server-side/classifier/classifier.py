import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn import metrics 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
#from sklearn.cross_validation import train_test_split

def knn():
	model = SVC(probability=True)
	df = pd.read_csv("transformed_dataset.csv")
	x = df.drop(["image_name", "class_name"], axis=1)
	y = df.class_name

	x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 1)

	#more accurate with n is low
	clf = KNeighborsClassifier(n_neighbors=550)
	clf.fit(x_train, y_train)
	y_pred = clf.predict(x_test)

	print("accuracy:", metrics.accuracy_score(y_test, y_pred))

	return clf

if __name__ == "__main__":
	#test_object = ['palm_108_keypoints', '0', '0', '-2.295', '2.521', '-4.111', '5.481', '-5.424', '9.336', '-7.949', '11.868', '-2.519', '10.004', '-2.184', '14.701', '-1.35', '17.766', '-0.292', '20.704', '0.01', '10', '0.721', '15.369', '1.123', '19.028', '1.952', '21.979', '2.189', '9.897', '2.546', '15.053', '2.915', '18.025', '3.503', '20.757', '4.226', '9.227', '5.098', '13.094', '5.195', '15.159', '5.308', '17.568', 'palm']
	test_object = ['peace_7_keypoints', '0', '0', '-2.031', '2.902', '-3.822', '6.485', '-3.108', '10.094', '-0.447', '11.963', '-2.707', '10.535', '-3.939', '14.32', '-4.366', '17.425', '-4.752', '20.21', '-0.001', '10', '0.467', '15.532', '0.921', '18.88', '1.756', '22.048', '1.964', '8.882', '2.199', '12.169', '0.179', '9.861', '-0.978', '7.693', '3.931', '7.764', '3.347', '9.546', '1.486', '8.039', '0.328', '5.872', 'peace']
	test_object = [float(item) for item in test_object[1:-1]]
	clf = knn()
	print(clf.predict([test_object]))
	print(clf.predict_proba([test_object]))


