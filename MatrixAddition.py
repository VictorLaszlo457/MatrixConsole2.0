import AviMatrix
import numpy as np

class MatrixAddition:

    #Create an empty matrix 
    correct_matrix = AviMatrix.__init__(0,0)
    updated_matrix = AviMatrix.__init__(0,0)
    matrixA = AviMatrix.__init__(0,0)

    def main(): 
        matrix1 = AviMatrix.__init__('1 2; 3 4')
        matrix2 = AviMatrix.__init__('2 3; 4 5')
        matrix3 = np.zeros(2,2)

        rows = 0
        columns = 0
        print("What is the sum of the matrices A and B given below?:")
        print("Matrix A: ")
        matrix1.display(matrix1)
        print("Matrix B: ")
        matrix2.display(matrix2)
        rows = matrix1.chanceLoop("rows", rows, matrix1)
        columns = matrix2.chanceLoop("columns", columns, matrix2)
        #correct_matrix = matrix1 + matrix2

    def chanceLoop(thingBeingCounted, thing, matrix):
        span = 0
        if (thingBeingCounted == "rows"):
            span = matrix.shape[0]
        elif (thingBeingCounted == "columns"):
            span = matrix.shape[1]
        while (thing != span): 
            print("How many " +  thingBeingCounted + " should the matrix have?: ")
            try:
                thing = int(input(thingBeingCounted + ":"))
                if (thing != span): 
                    print("Incorrect - please try again: ")
            except ValueError:
                print("The input typed is not a number")
        return int(thing)

    

  
# Method ask the user to fill out a matrix of the given dimensions  
# and returns the completed matrix to the user. 
# @param rows the number of rows of the matrix.
# @param columns the number of columns of the matrix.
# @return m the completed matrix with entries typed in by the user.
    def enterMatrix (rows, columns):
        entered_matrix = AviMatrix.__init__(rows,columns)
        # Is matrix valid?
        is_valid = False
        print("The matrix has dimensions of " + rows + " rows - " + columns + " columns")
        # The two for loops are for traversing the matrix and the do-while loop
        # allows the user to type in an input as often as necessary until an acceptable
        # input in typed in.
        for i in rows: 
            for j in columns:
                while (is_valid == False): 
                    #print("Enter a single value of index matrix[" + (i + 1) + "][" + (j + 1) + "]: ")
                    try: 
                        entered_matrix[i][j] = int(input("Enter a single value of index matrix[" + (i + 1) + "][" + (j + 1) + "]: "))
                        is_valid = True
                    except ValueError:
                        print("Invalid input - please try again")
                        is_Valid = False 
                        pass
        return entered_matrix                       

    

        




        

