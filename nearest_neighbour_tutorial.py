import numpy as np
np.set_printoptions(threshold=np.nan)
X_train = np.array([[-1,-1],[-0.5,-1],[-1,-2],[-2,-1],[-3,-2],[1,1],[2,1],[3,2]])

def nearest_neighbor():
	from sklearn.neighbors import NearestNeighbors
	global X_train
	nbrs = NearestNeighbors(n_neighbors = 3 ,algorithm = 'ball_tree').fit(X_train)
	#change the value of n_neighbors to see effect
	distances,indices = nbrs.kneighbors(X_train)
	print (indices) # x-->y graph
	print (distances) # x :: distance to y
	print nbrs.kneighbors_graph(X_train).toarray() # adjacant matix
	#so the above was a unsupervised learning where we created a numpy showing the working of nearest neighbor

def KDTree():
	#right now I dont know much details I will come here later
	from sklearn.neighbors import KDTree
	global X_train
	kdt = KDTree(X_train,leaf_size = 30 , metric = 'euclidean')
	distances,indices = kdt.query(X_train,k = 2 )
	print indices
	print distances
	pass

def nearest_centriod_classifier():
	from sklearn.neighbors.nearest_centroid import NearestCentroid
	global X_train
	y_train = np.array([1,1,1,1,2,3,4,5])
	clf = NearestCentroid()
	clf.fit(X_train,y_train)
	print clf.predict([[2,4]])
	pass

def main():
	#nearest_neighbor()
	#KDTree()
	nearest_centriod_classifier()
	pass

main()