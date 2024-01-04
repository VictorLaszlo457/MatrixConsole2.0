import numpy as np

# Class for creating a matrix using the python np library

class AviMatrix:
    # integer for matrix index and bool for checking if index is empty
	matrix = np.zeros((0,0))

	# Constructor to create and y matrix
	def __init__(self, rows, columns): 
		self.matrix = np.zeros((rows, columns))
	
	# Display the matrix
	def display(self, matrix):
		if (len(matrix.shape)) == 2: 
			for i in matrix.shape[0]: 
				for j in matrix.shape[1]:
					print(self.matrix(i,j) + " ")