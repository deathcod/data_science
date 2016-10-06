from sklearn.neighbors import NearestNeighbors
import numpy as np
np.set_printoptions(threshold=np.nan)

def nearest_neighbour():
	X_train = np.array([[-1,-1],[-0.5,-1],[-1,-2],[-2,-1],[-3,-2],[1,1],[2,1],[3,2]])
	nbrs = NearestNeighbors(n_neighbors = 2 ,algorithm = 'ball_tree').fit(X_train)

	distances,indices = nbrs.kneighbors(X_train)
	print (indices)
	print (distances)

	#so the above was a unsupervised learning where we created a numpy showing the working of nearest neighbor

def main():
	nearest_neighbour()
	pass

main()