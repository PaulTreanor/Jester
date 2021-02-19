import json
import os
from data_transformer import translate, enlarge, rotate
import time
from knn import knn
from conf_functions import lib_lof
from conf_functions import get_conf_LoF


# Gestures below min conf are likely to be OOD 
#min_conf = -1.3			#(works well with library LoF)
# min_conf = -25		#(works with ldof from scratch)			
min_conf = -1.3																								
k = 5																																							

# Global paths only used when running program directly
image_path = 'C:\\Users\\trean\\Desktop\\College\\4YP\\2021-ca400-ptreanor-cgorman\\src\\server-side\\image'
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


def processGestureData(gesture_data):
	gesture_data = [gesture_data[0]] + [float(val) for val in gesture_data[1:]]
	# Carry out tranformations on the line
	gesture_data = translate(gesture_data)
	gesture_data = enlarge(gesture_data)
	gesture_data = rotate(gesture_data)
	
	return gesture_data


def classify(gesture_data):
	clf = knn(k)
	classification, nn = clf.predict(gesture_data)
	conf = get_conf_LoF(gesture_data[0], nn, k)

	#lof = lib_lof()
	#conf = lof.decision_function(gesture_data)[0]
	return classification, conf

def getClass(image_path=image_path):
	# Run OpenPose from it's own directory or it won't work
	cwd = os.getcwd() 
	runOpenPose(image_path)
	os.chdir(cwd)

	gesture_data = getJsonData()

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
	#print(gesture_data)

	classification, conf = classify(gesture_data)

	# Check if confidence value is acceptable
	if conf < min_conf:
		return "OOD"

	# Delete image from server 
	#os.remove(image_path + 'image.jpg')
	return classification


if __name__ == '__main__':					
	print(getClass())