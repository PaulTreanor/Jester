import pandas as pd 
import csv
from sklearn.neighbors import LocalOutlierFactor
from scipy.spatial import distance
from knn import knn

############ LIBRARY LOF IMPLEMENTATION #############

def lib_lof():
	df = pd.read_csv("transformed_dataset.csv")
	x = df.drop(["image_name", "class_name"], axis=1)
	lof = LocalOutlierFactor(novelty=True)
	lof.fit(x)
	return lof

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

############# LoF ALGORITHM #####################
# Local outlier factor has max accuracy (90% ood detection) when min_conf = -1.3

def rDistance(A, B, clf, k):
	B_nns = clf.get_knn(B[2])
	if len(A) ==3:
		A = A[2]
	k_dist = max([distance.euclidean(B[2], n[2]) for n in B_nns])
	AB_dist = distance.euclidean(A, B[2])
	r_distance = max(k_dist, AB_dist)
	return r_distance

def lrd(A, nn, clf, k):
	r_distance_list = []
	for B in nn:
		B_r_distance = rDistance(A, B, clf, k)
		r_distance_list.append(B_r_distance)
	avg_r_distance = sum(r_distance_list)/k
	lrd = 1.0/avg_r_distance 
	return lrd

def get_conf_LoF(A, nn, clf, k):
	A_lrd = lrd(A, nn, clf, k)
	lrd_list = []
	for B in nn:
		B_nns = clf.get_knn(B[2])	
		B_lrd = lrd(B, B_nns, clf, k)
		lrd_list.append(B_lrd)
	lrd_total = sum(lrd_list)
	divisor = A_lrd*k
	lof = lrd_total/divisor
	lof = -lof
	return lof


