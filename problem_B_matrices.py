import numpy as np
import time as t

#Create matrices filled with random numbers
matrix_1 = np.random.rand(348,200)
matrix_2 = np.random.rand(200,140)
matrix_int_1 = np.random.randint (0,10, size = (348,200))
matrix_int_2 = np.random.randint (0,10, size = (200,140))


#Create empty matrices to fill with the product of the two matrices
matrix_int = [[0 for x in range(140)] for y in range(348)] 
matrix_double = [[0 for x in range(140)] for y in range(348)]  
matrix_alt_int = [[0 for x in range(140)] for y in range(348)] 
matrix_alt_double = [[0 for x in range(140)] for y in range(348)]  


#Multiply matrices with double data type
start_double = t.time()
print('Multiplying matrices using doubles')
for p in range(len(matrix_1)): #0-3  number of rows in matrix_1
	for q in range(len(matrix_2[0])): #0-3 number of columns in matrix_2
		for r in range(len(matrix_2)): #0-2 number of rows in matrix_2
			matrix_double[p][q] += matrix_1[p][r] * matrix_2[r][q]
#Print out the product of the multiplied matrices
for res in matrix_double:
	print(res)
end_double = t.time()
#Calculate and print how long multiplying the matrices took
print(end_double - start_double)


#Multiply matrices with int data type
start_int = t.time()
print('Multiplying matrices using ints')
for p in range(len(matrix_int_1)): #0-3  number of rows in matrix_1
	for q in range(len(matrix_int_2[0])): #0-3 number of columns in matrix_2
		for r in range(len(matrix_int_2)): #0-2 number of rows in matrix_2
			matrix_int[p][q] += matrix_int_1[p][r] * matrix_int_2[r][q]
			
#Print out the product of the multiplied matrices
for res in matrix_int:
	print(res)
end_int = t.time()
#Calculate and print how long multiplying the matrices took
print(end_int - start_int)

#---------------------------------------------------------------------------------------------------------------------------

#Multiply Matrices using the inner loop using double data type
start_alt_double = t.time()
print('Multiplying matrices using doubles with rows within the inner loop')
for p in range(len(matrix_1[0])): #0-2  number of columns in matrix_1
	for q in range(len(matrix_1)): #0-3 number of rows in matrix_2
		for r in range(len(matrix_2[0])): #0-3 number of columns in matrix_2
			matrix_alt_double[q][r] += matrix_1[q][p] * matrix_2[p][r]
			
#Print out the product of the multiplied matrices	
for res in matrix_alt_double:
	print(res)
end_alt_double = t.time()
#Calculate and print how long multiplying the matrices took
print(end_alt_double - start_alt_double)

#Multiply Matrices using the inner loop using int data type
start_alt_int = t.time()
print('Multiplying matrices using ints with rows within inner loop')
for p in range(len(matrix_int_1)): #0-3  number of rows in matrix_1
	for q in range(len(matrix_int_2[0])): #0-3 number of columns in matrix_2
		for r in range(len(matrix_int_2)): #0-2 number of rows in matrix_2
			matrix_alt_int[p][q] += matrix_int_1[p][r] * matrix_int_2[r][q]
			
#Print out the product of the multiplied matrices
for res in matrix_alt_int:
	print(res)

end_alt_int = t.time()
#Calculate and print how long multiplying the matrices took
print(end_alt_int - start_alt_int)
