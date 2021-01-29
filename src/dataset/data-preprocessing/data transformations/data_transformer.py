import csv


def translate(hand_gesture):
	x_dif = hand_gesture[1]
	y_dif = hand_gesture[2]
	x = gesture[1::2] 
	y = gesture[2::2]

	hand_gesture = [hand_gesture[0]]
	i = 0 
	while i < len(x):
		#do x thing 
		#add x to new list
		#do y thing 
		#add y to new list 
	print(hand_gesture)
	

	return hand_gesture


def transform_dataset():
	with open("..\\cleaned_dataset.csv", "r", newline='') as dataset:
		csv_reader = csv.reader(dataset)

		with open('transformed_dataset.csv', 'w', newline='') as transformed_dataset:
			csv_writer = csv.writer(transformed_dataset)
			for line in csv_reader:
				#convert coords from string to floats
				line = line[0] + [float(item) for item in line[1:]]
				#translate coordinates
				line = translate(line)
				#enlargement 
				#rotation
			#	csv_writer.writerow(line)



if __name__ == '__main__':					
	transform_dataset()