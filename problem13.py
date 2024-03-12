import numpy as np
import scipy.linalg as linalg 
import sympy


# Creating the matrices
A = np.array([[3, 8, -5], [3, -6, -7], [3, 4, 2]]) 

# print('A =\n', A) 

b = np.array([[-1], [-1], [3]])

# print('b =\n', b) 


# part a: Compute the reduced echelon form of A and convert the result back to a numpy array. You will need sympy to compute the reduced echelon form.

A_sympy = sympy.Matrix(A)
A_rref = A_sympy.rref()
A_rref = np.array(A_rref[0].tolist())
print('A_rref =\n', A_rref)


# part b: Find the column space of A

x =  A_rref[0][0]
y =  A_rref[1][1]
z =  A_rref[2][2] 


print('Column space = ')
if x == 1:
    col_x = np.array([[A[0][0]], [A[1][0]], [A[2][0]]]) 
    print(col_x, ',') 
if y == 1:
    col_y = np.array([[A[0][1]], [A[1][1]], [A[2][1]]])
    print(col_y, ',')
if z == 1:
    col_z = np.array([[A[0][2]], [A[1][2]], [A[2][2]]]) 
    print(col_z)


# part c: Solve the matrix equation Ax = b

x = linalg.solve(A, b)
print('solved x vector\n', x)


# part d: Compute Nul A  

nullA = linalg.null_space(A)
print('Null space\n', nullA)  
