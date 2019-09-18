import numpy as np
import time

#numpy solve
matrix_1 = np.random.rand(348,200)
matrix_2 = np.random.rand(200,140)
matrix_int_1 = np.random.randint (0,10, size = (348,200))
matrix_int_2 = np.random.randint (0,10, size = (200,140))



matrix_int = [[0 for x in range(140)] for y in range(348)] 
matrix_double = [[0 for x in range(140)] for y in range(348)]  
matrix_alt_int = [[0 for x in range(140)] for y in range(348)] 
matrix_alt_double = [[0 for x in range(140)] for y in range(348)]  



start_double = time.time()
print('Multiplying matrices using doubles')
for p in range(len(matrix_1)): #0-3  number of rows in matrix_1
	for q in range(len(matrix_2[0])): #0-3 number of columns in matrix_2
		for r in range(len(matrix_2)): #0-2 number of rows in matrix_2
			matrix_double[p][q] += matrix_1[p][r] * matrix_2[r][q]
for res in matrix_double:
	print(res)
end_double = time.time()
print(end_double - start_double)



start_int = time.time()
print('Multiplying matrices using ints')
for p in range(len(matrix_int_1)): #0-3  number of rows in matrix_1
	for q in range(len(matrix_int_2[0])): #0-3 number of columns in matrix_2
		for r in range(len(matrix_int_2)): #0-2 number of rows in matrix_2
			matrix_int[p][q] += matrix_int_1[p][r] * matrix_int_2[r][q]
for res in matrix_int:
	print(res)

end_int = time.time()
print(end_int - start_int)



start_alt_double = time.time()
print('Multiplying matrices using doubles with rows within the inner loop')
for p in range(len(matrix_1[0])): #0-2  number of columns in matrix_1
	for q in range(len(matrix_1)): #0-3 number of rows in matrix_2
		for r in range(len(matrix_2[0])): #0-3 number of columns in matrix_2
			matrix_alt_double[q][r] += matrix_1[q][p] * matrix_2[p][r]
for res in matrix_alt_double:
	print(res)
end_alt_double = time.time()
print(end_alt_double - start_alt_double)


start_alt_int = time.time()
print('Multiplying matrices using ints with rows within inner loop')
for p in range(len(matrix_int_1)): #0-3  number of rows in matrix_1
	for q in range(len(matrix_int_2[0])): #0-3 number of columns in matrix_2
		for r in range(len(matrix_int_2)): #0-2 number of rows in matrix_2
			matrix_alt_int[p][q] += matrix_int_1[p][r] * matrix_int_2[r][q]
for res in matrix_alt_int:
	print(res)

end_alt_int = time.time()
print(end_alt_int - start_alt_int)
