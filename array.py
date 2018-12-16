#Matrix multiplication using arrays

import numpy as np
row_column = int(input('Enter the size \n'))
matrix_list  = []
for i in range(0, row_column):
    matrix_list.append([int(i) for i in input().split()])
np_array = np.matrix(matrix_list)
np_identity = np.eye((row_column), dtype=int)
print(np_array)
print('Identity Matrix Multiplication \n', np_identity*np_array)