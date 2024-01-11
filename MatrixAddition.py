#from AviMatrix import AviMatrix
import numpy as np

# Global variables
# @correct_matrix should contain the final answer
correct_matrix = np.zeros((0,0))

# @dimension: the dimension (row or column) whose size the user has to input correctly
# @matrix: the output matrix whose dimensions are to be correctly provided by the user
def chance_loop(dimension, matrix):
    # dim_size is the size of the dimension being iterated over
    dim_size = 0
    if (dimension == "rows"):
        dim_size = matrix.shape[0]
    elif (dimension == "columns"):
        dim_size = matrix.shape[1]
    input_dim_size = 0
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


class MatrixAddition:

    def main(): 
        matrix1 = np.matrix('1 2; 3 4')
        matrix2 = np.matrix('2 3; 4 5')
        matrix3 = np.zeros((2,2))
        rows = 0
        columns = 0
        print("What is the sum of the matrices A and B given below?:")
        print("Matrix A: ")
        print(matrix1)
        #matrix1.display(matrix1)
        print("Matrix B: ")
        #matrix2.display(matrix2)
        print(matrix2)
        rows = chance_loop("rows", matrix1)
        columns = chance_loop("columns", matrix1)
        correct_matrix = matrix1 + matrix2
        print("The Correct Matrix is: ")
        print(correct_matrix)


      
    # Method ask the user to fill out a matrix of the given dimensions  
    # and returns the completed matrix to the user. 
    # @param rows the number of rows of the matrix.
    # @param columns the number of columns of the matrix.
    # @return m the completed matrix with entries typed in by the user.
    # def enterMatrix (rows, columns):
    #     entered_matrix = np.zeros((rows,columns))
    #     # Is matrix valid?
    #     is_valid = False
    #     print("The matrix has dimensions of " + rows + " rows - " + columns + " columns")
    #     # The two for loops are for traversing the matrix and the do-while loop
    #     # allows the user to type in an input as often as necessary until an acceptable
    #     # input in typed in.
    #     for i in rows: 
    #         for j in columns:
    #             while (is_valid == False): 
    #                 #print("Enter a single value of index matrix[" + (i + 1) + "][" + (j + 1) + "]: ")
    #                 try: 
    #                     entered_matrix[i][j] = int(input("Enter a single value of index matrix[" + (i + 1) + "][" + (j + 1) + "]: "))
    #                     is_valid = True
    #                 except ValueError:
    #                     print("Invalid input - please try again")
    #                     is_Valid = False 
    #                     pass
    #     return entered_matrix                       

    if __name__ == "__main__":
        main()
        




        

