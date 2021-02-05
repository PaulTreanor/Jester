import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn import metrics 
from sklearn.neighbors import KNeighborsClassifier

########## To FIND OUT WHAT VALUES OF K ARE THE MOST ACCURATE IN KNN ##############

def knn(k):
	df = pd.read_csv("..\\transformed_dataset.csv")
	x = df.drop(["image_name", "class_name"], axis=1)
	y = df.class_name

	x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 1)

	clf = KNeighborsClassifier(n_neighbors=k)
	clf.fit(x_train, y_train)

	y_pred = clf.predict(x_test)

	accuracy = metrics.accuracy_score(y_test, y_pred)
	print(str(k) + " accuracy: " + str(accuracy))
	return clf, accuracy


def find_best_k():
	k = 1
	max_accuracy = 0
	best_k = 0
	while k < 100:
		clf, accuracy = knn(k)
		if accuracy > max_accuracy:
			max_accuracy = accuracy
			best_k = k
		k +=1
	print(best_k)


if __name__ == "__main__":
	find_best_k()

