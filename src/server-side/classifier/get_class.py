import json
import os
from data_transformer import translate, enlarge, rotate
from classifier import classify
import time

# Gestures below min conf are likely to be OOD 
min_conf = 0

# Global to allow for easier and faster testing
image_path = 'C:\\Users\\trean\\Desktop\\College\\4YP\\2021-ca400-ptreanor-cgorman\\src\\server-side\\image'
output_path = 'C:\\Users\\trean\\Desktop\\College\\4YP\\2021-ca400-ptreanor-cgorman\\src\\server-side\\classifier\\openposeJSON'

def runOpenPose(image_path=image_path):
	# Openpose command 
	command = 'bin\\OpenPoseDemo.exe --image_dir ' + image_path + ' --hand --net_resolution "-1x320" --write_json ' + output_path + '\n'
	# Go to openpose directory - or it won't run 
	os.chdir('C:\\Users\\trean\\Documents\\openpose_1.6\\openpose')
	# Run command 
	os.system(command)


# Extracts keypoint data from JSON into list
def getJsonData():
	with open('openposeJSON\\image_keypoints.json', "r") as json_file:
		json_data = json.load(json_file)
		first_person = json_data['people'][0]
		gesture_data = first_person['hand_right_keypoints_2d']
		gesture_data.insert(0, "image")
		return gesture_data	


def getClass(image_path=image_path):
	# Run OpenPose from different directory 
	cwd = os.getcwd() 
	runOpenPose(image_path)
	os.chdir(cwd)

	gesture_data = getJsonData()

	# Check OpenPose confidence values meet minimum value                          maybve a sum value would work well for this 
	min_total = 5                                        # Placeholder 
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

	gesture_data = [gesture_data[0]] + [float(val) for val in gesture_data[1:]]
	
	# Carry out tranformations on the line
	gesture_data = translate(gesture_data)
	gesture_data = enlarge(gesture_data)
	gesture_data = rotate(gesture_data)

	# Put line into classifier 
	classification, conf = classify(gesture_data)

	#print(conf)
	# Check if confidence value is acceptable
	#if conf < min_conf():
	#	return "OOD"

	# Delete image from server 
	#os.remove(image_path + 'image.jpg')

	return classification




if __name__ == '__main__':					
	print(getClass())