import pytest 
from classifiers.knn import knn
from scipy.spatial import distance

# python -m pytest .\conf_function_tests.py 

# Used library LoF function (sk-learn) to get correct test results

##################### CONFIDENCE FUNCTION TESTS ######################

@pytest.mark.lof
def test_palm_lof():
	gesture_data = [[-0.0, 0.0, -3.083, 1.839, -5.395, 4.457, -5.771, 8.398, -4.251, 11.293, -2.659, 10.371, -2.116, 14.151, -1.413, 17.201, -0.734, 19.839, -0.001, 10.0, 0.502, 14.814, 1.013, 18.082, 1.409, 21.15, 2.13, 9.456, 2.537, 14.379, 2.804, 17.044, 2.963, 19.611, 4.133, 8.508, 4.785, 12.385, 4.816, 14.548, 4.442, 16.839]]
	clf = knn()
	classification, confidence = clf.predict(gesture_data)
	assert confidence == -0.05634808892020349

@pytest.mark.lof
def test_ood_lof():
	gesture_data = [[-0.0, 0.0, -2.796, 2.76, -4.841, 5.818, -5.71, 8.82, -6.415, 11.658, -2.579, 9.755, -2.408, 13.612, -4.429, 12.749, -6.317, 11.626, 0.001, 10.0, 0.623, 14.906, 0.798, 18.109, 0.679, 21.41, 2.229, 9.165, 3.114, 13.876, 3.094, 16.818, 3.043, 19.661, 4.065, 8.131, 5.612, 11.539, 5.467, 13.761, 5.062, 15.85]]
	clf = knn()
	classification, confidence = clf.predict(gesture_data)
	assert confidence == -1.3717973576761913

@pytest.mark.lof
def test_thumbs_up_lof():
	gesture_data = [[-0.0, 0.0, -0.78, 3.63, -0.507, 8.196, 0.646, 12.339, -0.04, 16.165, 6.325, 9.12, 6.897, 9.808, 3.531, 7.575, 1.173, 6.182, 7.822, 6.229, 8.399, 6.675, 3.621, 4.761, 2.078, 4.059, 9.071, 3.82, 9.654, 3.78, 5.013, 2.402, 3.174, 2.085, 9.026, 0.227, 9.703, 0.384, 6.161, 0.284, 4.951, 0.023]]
	clf = knn()
	classification, confidence = clf.predict(gesture_data)
	assert confidence == 0.22744789745432348