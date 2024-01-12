import numpy as np
from random import randint

# Class for generating a random matrix according to the level of difficulty
def random_matrix_generation_level(level):
	rand_matrix = np.zeros((1,1))
	# At level 0, matrices are only nx1 or 1xm  
	if (int(level)==0):
		# Randomly generate 1 or 2. 
		# If output 1, then generate row matrix. If output 2, then generate column matrix 
		# Create a row matrix
		row_or_col = randint(1,2)
		if (int(row_or_col) == 1):
			num_row = randint(1,7)
			rand_matrix = np.zeros((num_row, 1))
			# Update the values of the matrix with random integers
			for i in range(num_row):
				rand_matrix[i][0] = randint(1,100)
		# Create a column matrix
		else: 
			num_col = randint(1,7)
			rand_matrix = np.zeros((1, num_col))
			# Update the values of the matrix with random integers
			for i in range(num_col):
				rand_matrix[0][i] = randint(1,25)
	# At level 1, matrices are only small, square matrices
	if (int(level)==1):
		num_row = randint(1,3)
		num_col = num_row
		rand_matrix = np.zeros((num_row, num_col))
		# Update the values of the matrix with random integers
		for i in range(num_row):
			for j in range(num_col):
				rand_matrix[i][j] = randint(1,100)
	# At level 2, matrices are large square matrices
	if (int(level)==2):
		num_row = randint(3,6)
		num_col = num_row
		rand_matrix = np.zeros((num_row, num_col))
		# Update the values of the matrix with random integers
		for i in range(num_row):
			for j in range(num_col):
				rand_matrix[i][j] = randint(1,100)
	# At level 3, matrices may be differing dimensions of multiplication and just larger for addition and subtraction
	if (int(level)==3):
		num_row = randint(1,6)
		num_col = randint(1,6)
		rand_matrix = np.zeros((num_row, num_col))
		# Update the values of the matrix with random integers
		for i in range(num_row):
			for j in range(num_col):
				rand_matrix[i][j] = randint(1,100)
	print(rand_matrix)
	print(rand_matrix.shape)
	return rand_matrix


class AviMatrix:
    # integer for matrix index and bool for checking if index is empty
	matrix = np.zeros((0,0))

	def main():
		#random_matrix_generation_level(2) 
		random_matrix_generation_level(3) 
	
	if __name__ == "__main__":
		main()

	# Display the matrix
	# def display(self, matrix):
	# 	if (len(matrix.shape)) == 2: 
	# 		for i in matrix.shape[0]: 
	# 			for j in matrix.shape[1]:
	# 				print(self.matrix(i,j) + " ")
