import json
import os
from data_transformer import translate, enlarge, rotate
from classifier import classify
import time

def runOpenPose():
	image_path = 'C:\\Users\\trean\\Desktop\\College\\4YP\\2021-ca400-ptreanor-cgorman\\src\\server-side\\image'
	output_path = 'C:\\Users\\trean\\Desktop\\College\\4YP\\2021-ca400-ptreanor-cgorman\\src\\server-side\\classifier\\openposeJSON'
	# Openpose command 
	command = 'bin\\OpenPoseDemo.exe --image_dir ' + image_path + ' --hand --net_resolution "-1x320" --write_json ' + output_path + '\n'
	# Go to openpose directory - or it won't run 
	os.chdir('C:\\Users\\trean\\Documents\\openpose_1.6\\openpose')
	# Run command 
	os.system(command)


# Extracts keypoint data from JSON into list
def getJsonData():
	with open('openposeJSON\image_keypoints.json', "r") as json_file:
		json_data = json.load(json_file)
		first_person = json_data['people'][0]
		gesture_data = first_person['hand_right_keypoints_2d']
		gesture_data.insert(0, "image")
		return gesture_data	


def getClass():

	cwd = os.getcwd() 

	runOpenPose()

	os.chdir(cwd)


	gesture_data = getJsonData()

	# Delete confidence values 
	del gesture_data[3::3]


	# Check if hand gesture detected by OpenPose
	for val in gesture_data:
		if val == "0":
			return "OOD"

	gesture_data = [gesture_data[0]] + [float(val) for val in gesture_data[1:]]
	
	# Carry out tranformations on the line
	gesture_data = translate(gesture_data)
	gesture_data = enlarge(gesture_data)
	gesture_data = rotate(gesture_data)

	# Put line into classifier 
	classification = classify(gesture_data)

	# Check if confidence value is acceptable

	# Delete image from server 

	return classification




if __name__ == '__main__':					
	print(getClass())