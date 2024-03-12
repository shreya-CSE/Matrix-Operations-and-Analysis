# Matrix Operations and Analysis

This Python script performs various operations and analyses on a given matrix A and vector b using NumPy, SciPy, and SymPy libraries. The key functionalities include computing the reduced echelon form, finding the column space, solving a matrix equation, and computing the null space of matrix A.

## Code Overview

### Matrix Definition

```python
A = np.array([[3, 8, -5], [3, -6, -7], [3, 4, 2]])
b = np.array([[-1], [-1], [3]])
```

### Part a: Compute Reduced Echelon Form

```python
A_sympy = sympy.Matrix(A)
A_rref = A_sympy.rref()
A_rref = np.array(A_rref[0].tolist())
print('Reduced Echelon Form of A:\n', A_rref)
```

### Part b: Find Column Space

```python
x, y, z = A_rref[0][0], A_rref[1][1], A_rref[2][2]

print('Column space:')
if x == 1:
    col_x = np.array([[A[0][0]], [A[1][0]], [A[2][0]]]) 
    print(col_x, ',') 
if y == 1:
    col_y = np.array([[A[0][1]], [A[1][1]], [A[2][1]]])
    print(col_y, ',')
if z == 1:
    col_z = np.array([[A[0][2]], [A[1][2]], [A[2][2]]]) 
    print(col_z)
```

### Part c: Solve Matrix Equation

```python
x = linalg.solve(A, b)
print('Solved x vector:\n', x)
```

### Part d: Compute Null Space

```python
nullA = linalg.null_space(A)
print('Null space of A:\n', nullA)
```

## Dependencies

- NumPy: For numerical operations on matrices and vectors.
- SciPy: For linear algebra operations, including solving matrix equations and computing null spaces.
- SymPy: For symbolic mathematics, particularly useful for computing reduced echelon forms.

