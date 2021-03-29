import json
import os
from data_transformer import translate, enlarge, rotate
import time
from knn import knn
from conf_functions import library_local_outlier_factor, get_conf_LoF, get_conf_ldofs

# Gestures below min confidence are likely to be OOD 
# Recommended min_confidence values for k=5 : (lib_lof: -1.3), (lof: -3), (ldof: -25)
# K should be <= 5
min_confidence = -3																								
k = 5																																						

# Global image_path only used when running program directly
image_path = 'C:\\Users\\trean\\Desktop\\College\\4YP\\2021-ca400-ptreanor-cgorman\\src\\server-side\\test-images\\ood'
output_path = 'C:\\Users\\trean\\Desktop\\College\\4YP\\2021-ca400-ptreanor-cgorman\\src\\server-side\\classifier\\openposeJSON'
json_path = 'C:\\Users\\trean\\Desktop\\College\\4YP\\2021-ca400-ptreanor-cgorman\\src\\server-side\\classifier\\openposeJSON\\image_keypoints.json'

# Write and run OpenPose command
def runOpenPose(image_path=image_path):
	command = 'bin\\OpenPoseDemo.exe --image_dir ' + image_path + ' --hand --net_resolution "-1x320" --write_json ' + output_path + '\n'
	os.chdir('C:\\Users\\trean\\Documents\\openpose_1.6\\openpose')
	os.system(command)


# Extracts keypoint data from JSON into list
def getJsonData():
	with open(json_path, "r") as json_file:
		json_data = json.load(json_file)
		if len(json_data['people']) == 0:
			return "noPeople"
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
	classifier = knn(k)
	classification, nn = classifier.predict(gesture_data)
	conf = get_conf_LoF(gesture_data[0], nn, classifier, k)  
	#conf = get_conf_ldofs(nn)
	#lof = lib_lof()
	#conf = lof.decision_function(gesture_data)[0]
	return classification, conf


def getClass(image_path=image_path):
	# Run OpenPose must run from directory it is in
	current_working_dir = os.getcwd() 
	runOpenPose(image_path)
	os.chdir(current_working_dir)

	gesture_data = getJsonData()
	path = image_path + "\\image.jpg"

	if gesture_data == "noPeople":
		os.remove(path)
		return "OOD"

	# Delete image from server if not running main (ie. debugging)
	if __name__ != '__main__':
		os.remove(path)

	# Default min threshold for displaying in OpenPose is 0.5 (sum of 10.5 for 21 total keypoints), lower value of 5 works better for this application  											  
	min_total = 5                                        																		
	total = 0
	for value in gesture_data[3::3]:	# Every 3rd value is a confidence value for a keypoint, others are x and y coordinates
		total += value
	if total < min_total:
		return "OOD"

	# Delete confidence values 
	del gesture_data[3::3]

	# Check if hand gesture detected by OpenPose
	for value in gesture_data:
		if value == "0":
			return "OOD"

	gesture_data = processGestureData(gesture_data)
	gesture_data = [gesture_data[1:]]
	classification, confidence = classify(gesture_data)
	print(confidence)
	# Check if confidence value is acceptable
	if confidence < min_confidence:
		return "OOD"

	return classification

if __name__ == '__main__':					
	print(getClass())
