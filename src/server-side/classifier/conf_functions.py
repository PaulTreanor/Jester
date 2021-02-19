from __future__ import division
import pandas as pd 
import csv
from sklearn.neighbors import LocalOutlierFactor
from scipy.spatial import distance
from knn import knn

############# SIMPLE KNN ANOMOLY DETECTION ALGORITHMS #####################

def get_conf_knn(nn):
	distances = [item[0] for item in nn]
	avg_dist = sum(distances)/len(distances)
	return avg_dist


def get_conf_kth_nn(nn):
	distances = [item[0] for item in nn]
	return max(distances)

############# LDoF ALGORITHM #####################

# Local distance outlier factor has max accuracy (90% ood detection) when min_conf = -25
def get_conf_ldofs(nn):
	knn_avg = get_conf_knn(nn)
	knn_inner_distances = []
	for item in nn:
		neighbours = [line[0] for line in nn if line != item]
		distances = [distance.euclidean(item[0], line) for line in neighbours]
		knn_inner_distances += distances
	knn_inner_distance_avg = sum(knn_inner_distances)/len(knn_inner_distances)
	ldof = knn_avg/knn_inner_distance_avg
	return ldof


############ LIBRARY LOF #############

def lib_lof():
	df = pd.read_csv("transformed_dataset.csv")
	x = df.drop(["image_name", "class_name"], axis=1)
	y = df.class_name

	# Find conf value to recognise OOD images
	lof = LocalOutlierFactor(novelty=True)
	lof.fit(x)

	return lof




############# LoF ALGORITHM #####################

def rDistance(A, B, k):
	B_clf = knn()
	B_nns = B_clf.get_knn(B[2])
#	print(len(B[2]), "\n", len(B_nns[0][2]))
	if len(A) ==3:
		A = A[2]
	
	k_dist = max([distance.euclidean(B[2], n[2]) for n in B_nns])
	AB_dist = distance.euclidean(A, B[2])
	r_distance = max(k_dist, AB_dist)
	#print(r_distance)
	return r_distance

def lrd(A, nn, k):
	r_distance_list = []
	for B in nn:
		try:
			B_r_distance = rDistance(A, B, k)
			######an error is thrown here 
			#if nn[0][0] == 19.616942983044023:
			#	print("dsafkiljfdsakljfdsakljsfdaklfdsakljfdsakljkljfdsadskljfakljfds")
			r_distance_list.append(B_r_distance)
		except Exception:
			continue
	avg_r_distance = sum(r_distance_list)/k
	lrd = 1.0/avg_r_distance 
	return lrd

def get_conf_LoF(A, nn, k):
	A_lrd = lrd(A, nn, k)
	lrd_list = []
	for B in nn:
		B_clf = knn()
		B_nns = B_clf.get_knn(B[2])	
		#print("B_nns: ", B_nns)
		B_lrd = lrd(B, B_nns, k)
		lrd_list.append(B_lrd)
	lrd_total = sum(lrd_list)
	divisor = A_lrd*k
	lof = lrd_total/divisor
	print(lof)
	return lof