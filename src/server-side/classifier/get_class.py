import json
import os
from data_transformer import translate, enlarge, rotate
import time
from knn import knn
from conf_functions import lib_lof, get_conf_LoF, get_conf_ldofs

# Gestures below min conf are likely to be OOD 
# Recommended min_conf values for k=5 : (lib_lof: -1.3), (lof: -3), (ldof: -25)
# K should be <= 5
min_conf = -3																								
k = 5																																						

# Global image_path only used when running program directly
image_path = 'C:\\Users\\trean\\Desktop\\College\\4YP\\2021-ca400-ptreanor-cgorman\\src\\server-side\\test-images\\ood'
output_path = 'C:\\Users\\trean\\Desktop\\College\\4YP\\2021-ca400-ptreanor-cgorman\\src\\server-side\\classifier\\openposeJSON'

# Write and run OpenPose command
def runOpenPose(image_path=image_path):
	command = 'bin\\OpenPoseDemo.exe --image_dir ' + image_path + ' --hand --net_resolution "-1x320" --write_json ' + output_path + '\n'
	os.chdir('C:\\Users\\trean\\Documents\\openpose_1.6\\openpose')
	os.system(command)


# Extracts keypoint data from JSON into list
def getJsonData():
	with open('openposeJSON\\image_keypoints.json', "r") as json_file:
		json_data = json.load(json_file)
		first_person = json_data['people'][0]
		gesture_data = first_person['hand_right_keypoints_2d']
		gesture_data.insert(0, "image")
		return gesture_data	


# Carry out tranformations on the line
def processGestureData(gesture_data):
	gesture_data = [gesture_data[0]] + [float(val) for val in gesture_data[1:]]
	gesture_data = translate(gesture_data)
	gesture_data = enlarge(gesture_data)
	gesture_data = rotate(gesture_data)
	return gesture_data


def classify(gesture_data):
	clf = knn(k)
	classification, nn = clf.predict(gesture_data)
	conf = get_conf_LoF(gesture_data[0], nn, clf, k)  
	#conf = get_conf_ldofs(nn)
	#lof = lib_lof()
	#conf = lof.decision_function(gesture_data)[0]
	return classification, conf


def getClass(image_path=image_path):
	# Run OpenPose must run from directory it is in
	cwd = os.getcwd() 
	runOpenPose(image_path)
	os.chdir(cwd)

	gesture_data = getJsonData()

	# Delete image from server
	path = image_path + "\\image.jpg"
	# Don't delete image if ad hoc testing get_class
	if __name__ != '__main__':
		os.remove(path)

	# Default min threshold for displaying in OpenPose is 0.5 (sum of 10.5 for 21 total keypoints), lower value of 5 works better for this application  											  
	min_total = 5                                        																		
	total = 0
	for val in gesture_data[3::3]:
		total += val
	if total < min_total:
		return "OOD"

	# Delete confidence values 
	del gesture_data[3::3]

	# Check if hand gesture detected by OpenPose
	for val in gesture_data:
		if val == "0":
			return "OOD"

	gesture_data = processGestureData(gesture_data)
	gesture_data = [gesture_data[1:]]
	classification, conf = classify(gesture_data)
	print(conf)
	# Check if confidence value is acceptable
	if conf < min_conf:
		return "OOD"

	return classification

if __name__ == '__main__':					
	print(getClass())
