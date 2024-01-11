#from AviMatrix import AviMatrix
import numpy as np

# Global variables
# @correct_matrix should contain the final answer
correct_matrix = np.zeros((0,0))
entered_matrix =  np.zeros((0,0))

# @dimension: the dimension (row or column) whose size the user has to input correctly
# @matrix: the output matrix whose dimensions are to be correctly provided by the user
def enter_dimensions(dimension, matrix):
    # @dim_size: size of the dimension specified in the argument
    # @input_dim_size: size of dimension as input by the user
    dim_size = 0
    input_dim_size = 0
    if (dimension == "rows"):
        dim_size = matrix.shape[0]
    elif (dimension == "columns"):
        dim_size = matrix.shape[1]

    #print("dim_size: " + str(dim_size))
    #print("dimensions: " + str(dimension))
    while (int(input_dim_size) != int(dim_size)): 
        try:
            input_dim_size = input("How many " +  str(dimension) + " should the matrix have?: ")
            if (int(input_dim_size) != int(dim_size)): 
                # print("input_dim_size: " + str(input_dim_size))
                # print(int(input_dim_size) == int(dim_size))
                print("Incorrect - please try again: ")
        except ValueError:
            print("The input typed is not a number")
    
    print("Correct! The matrix should have " + str(dim_size) + " " + str(dimension))
    return dim_size


# Method ask the user to fill out a matrix of the given dimensions  
# and returns the completed matrix to the user. 
# @rows:  number of rows of the matrix.
# @columns: number of columns of the matrix.
# @return m the completed matrix with entries typed in by the user.
def enter_matrix (rows, columns):
    entered_matrix = np.zeros((rows,columns))
    print("The matrix has a dimension of " + str(rows) + " x " + str(columns))
    print("Please enter the values for the entries of the matrix")
    # The two for loops are for traversing the matrix and the while loop
    # allows the user to type in an input as often as necessary until an acceptable
    # input in typed in.
    for i in range(int(rows)): 
        for j in range(int(columns)):
            # As long as an invalid value is input for the entry, request that the user enter it again
            is_valid = False 
            while (is_valid == False):
                try: 
                    entered_matrix[i][j] = int(input("Enter a single value of index [" + str(i) + "][" + str(j) + "]: "))
                    is_valid = True
                except ValueError:
                    print("Invalid input - please try again")
    return entered_matrix  

def matrix_check(entered_matrix, correct_matrix):
    if ((entered_matrix == correct_matrix).all()):
        print("You are correct! The matrix difference is ")
        print(correct_matrix)
    else: 
        retry = str(input("Your answer is incorrect. Would you like to try again? Please type Y/N: ")).lower()
        if (retry == "y" or retry == "yes"): 
            reentered_matrix = enter_matrix(entered_matrix.shape[0], entered_matrix.shape[1])
            matrix_check(reentered_matrix, correct_matrix)
        elif (retry == "n" or retry == "no"): 
            print("That's too bad. Just for reference, the correct answer would have been")
            print(correct_matrix)


class MatrixAddition:

    def main(): 
        matrix1 = np.matrix('1 2; 3 4')
        matrix2 = np.matrix('2 3; 4 5')
        matrix3 = np.zeros((2,2))
        rows = 0
        columns = 0
        print("What is the difference of the matrices A and B given below?:")
        print("Matrix 1: ")
        print(matrix1)
        #matrix1.display(matrix1)
        print("Matrix 2: ")
        #matrix2.display(matrix2)
        print(matrix2)
        rows = enter_dimensions("rows", matrix1)
        columns = enter_dimensions("columns", matrix1)
        entered_matrix = enter_matrix(rows, columns)
        print("The Entered Matrix is: ")
        print(entered_matrix)
        correct_matrix = matrix1 - matrix2

        # If matrix_check returns "True", the user has input the correct matrix or would like to discontinue
        # If matrix_check returns "False", the user has not input the correct matrix, but would like to try again 
        exit_process = matrix_check(entered_matrix, correct_matrix)
      
                    

    if __name__ == "__main__":
        main()
        




        
