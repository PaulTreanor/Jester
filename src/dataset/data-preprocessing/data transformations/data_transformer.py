import csv


def transform_dataset():
	with open("..\\cleaned_dataset.csv", "r", newline='') as dataset:
		csv_reader = csv.reader(dataset)

		with open('transformed_dataset.csv', 'w', newline='') as transformed_dataset:
			csv_writer = csv.writer(transformed_dataset)
			for line in csv_reader:
				#translation
				#enlargement 
				#rotation
				csv_writer.writerow(line)



if __name__ == '__main__':					
	transform_dataset()