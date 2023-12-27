def create_matrix(a):
    n = len(a)
    A = [[0] * n for _ in range(n)]  # Initialize an n x n matrix with all elements as 0
    
    for i in range(n):  # Fill the diagonal elements with the array elements
        for j in range(i + 1, n):  # Fill the upper triangular matrix
            for k in range(i, j + 1):  # Fill the lower triangular matrix
                A[i][j] += a[k]  # Sum the elements of the array

    return A  # Return the matrix


