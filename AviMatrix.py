import numpy as np
from random import randint

# Class for generating a random matrix according to the level of difficulty and operation type
# Since complexity increases exponentially as matrices grow larger when performing matrix multiplication
# Operation type should be accounted for when generating matrices according to difficulty
# Levels: 1,2,3
# Operations: "add", "sub", "mul"
def random_matrix_generation_level(level, operation):
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
		if (str(operation) == "mul"):
			num_row = randint(1,3)
		elif (str(operation) == "add" or str(operation) == "sub"):
			num_row = randint(3,6)
		num_col = num_row
		rand_matrix = np.zeros((num_row, num_col))
		# Update the values of the matrix with random integers
		for i in range(num_row):
			for j in range(num_col):
				rand_matrix[i][j] = randint(1,100)
	# At level 3, matrices may be differing dimensions of multiplication and just larger for addition and subtraction
	if (int(level)==3):
		if (str(operation) == "mul"):
			num_row = randint(2,5)
			num_col = randint(2,5)
		elif (str(operation) == "add" or str(operation) == "sub"):
			num_row = randint(4,6)
			num_col = randint(4,6)
		rand_matrix = np.zeros((num_row, num_col))
		# Update the values of the matrix with random integers
		for i in range(num_row):
			for j in range(num_col):
				rand_matrix[i][j] = randint(1,100)
	print(rand_matrix)
	print(rand_matrix.shape)
	return rand_matrix, rand_matrix.shape[0], rand_matrix.shape[1]

# Pretty print a single matrix
def print_matrix(matrix1):
	# Convert matrix1 to a nice string
	for i in range(matrix1.shape[0]):
		s1 = "["
		for j in range(matrix1.shape[1]):
			s1 = str(s1) + str(matrix1[i][j]) + " "
		s1 = str(s1) + str(" ]")
		print(s1)
	return

# Pretty print a whole relation
def print_relation(operation, matrix1, matrix2):
	# Convert matrix1 to a nice string
	for i in range(matrix1.shape[0]):
		s1 = "["
		for j in range(matrix1.shape[1]):
			s1 = str(s1) + str(matrix1[i][j]) + " "
		s1 = str(s1) + str(" ]")
		print(s1)

	# Put "+", "-", or "*" depending on the operation
	if (str(operation) == "add"):
		print(" + ")
	if (str(operation) == "sub"):
		print(" - ")
	if (str(operation) == "mul"):
		print(" * ")
	# Convert matrix2 to a nice string
	for i in range(matrix2.shape[0]):
		s2 = "["
		for j in range(matrix2.shape[1]):
			s2 = str(s2) + str(matrix2[i][j]) + " "
		s2 = str(s2) + str(" ]")
		print(s2)	
	return

class AviMatrix:
    # integer for matrix index and bool for checking if index is empty
	matrix = np.zeros((0,0))

	def main():
		#random_matrix_generation_level(2) 
		print("Add Matrix Level 3")
		random_matrix_generation_level(3, "add")
		print("Sub Matrix Level 3")
		random_matrix_generation_level(3, "sub")
		print("Mul Matrix Level 3")
		random_matrix_generation_level(3, "mul")

	
	if __name__ == "__main__":
		main()

	# Display the matrix
	# def display(self, matrix):
	# 	if (len(matrix.shape)) == 2: 
	# 		for i in matrix.shape[0]: 
	# 			for j in matrix.shape[1]:
	# 				print(self.matrix(i,j) + " ")
