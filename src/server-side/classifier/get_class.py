

import os





def getClass():

	image_path = 'C:\\Users\\trean\\Desktop\\College\\4YP\\2021-ca400-ptreanor-cgorman\\src\\server-side\\image'
	output_path = 'C:\\Users\\trean\\Desktop\\College\\4YP\2021-ca400-ptreanor-cgorman\\src\\server-side\\classifier\\openposeJSON'

	# Write openpose command 

	command = 'C:\\Users\\trean\\Documents\\openpose_1.6\\openpose\\bin\\OpenPoseDemo.exe --image_dir ' + image_path + ' --hand --net_resolution "-1x320" --write_json ' + output_path + '\n'

	# Run command 
	os.system(command)
	# Read in json					######## Might start the program from here 
		# Change format 
		# Save line as list 

	# Is hand gesture detected 
	
	# Carry out tranformations on the line

	# Put line into classifier 

	# Check if confidence value is acceptable

	# Delete image from server 


	classification = "herlo"

	return classification




if __name__ == '__main__':					
	print(getClass())