import pandas as pd 

class knn:
	def __init__(self, k=5):
		self.k = k
		self.features = []
		self.classifications = []


	# Creating fit method so the classifier can be classed from same method as the library classifier, which uses a fit method
	# both paramaters are pd dataframes
	def fit(features, classifications):
		self.features = features 
		self.classifications = classifications



	def predict(gesture_data):	# Gesture data will be list of lists	
		return classification