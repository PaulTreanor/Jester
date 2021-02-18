from scipy.spatial import distance

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

def rDistance(A, B):
	from classifiers.knn import knn 

	k=5
	B_clf = knn()
	B_nns = B_clf.get_knn(B[2])
	print(len(B[2]), "\n", len(B_nns[0][2]))
	k_dist = max([distance.euclidean(B[2], n[2]) for n in B_nns])
	AB_dist = distance.euclidean(A, B[2])
	r_distance = max(k_dist, AB_dist)
	print("finished rDistance")
	return r_distance

def lrd(A, nn):
	k = 5
	r_distance_list = []
	for B in nn:
		try:
			B_r_distance = rDistance(A, B)
			r_distance_list.append(B_r_distance)
		except Exception:
			pass
	lrd = 1/(sum(r_distance_list) / k) 											# K is class variable
	return lrd

def get_conf_LoF(A, nn):
	from classifiers.knn import knn
	k = 5
	A_lrd = lrd(A, nn)
	lrd_list = []
	for B in nn:
		B_clf = knn()
		B_nns = B_clf.get_knn(B[2])	
		B_lrd = lrd(B, B_nns)
		lrd_list.append(B_lrd)
	lrd_total = sum(lrd_list)
	divisor = lrd(A)*k
	lof = lrd_total/divisor
	return lof