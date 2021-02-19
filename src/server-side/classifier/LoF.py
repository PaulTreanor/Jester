import pandas as pd 
import csv
from sklearn.neighbors import LocalOutlierFactor



def lib_lof():
	df = pd.read_csv("transformed_dataset.csv")
	x = df.drop(["image_name", "class_name"], axis=1)
	y = df.class_name

	# Find conf value to recognise OOD images
	lof = LocalOutlierFactor(novelty=True)
	lof.fit(x)

	return lof
