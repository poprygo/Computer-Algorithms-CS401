def create_optimized_matrix(a):
    n = len(a)
    A = [[0] * n for _ in range(n)]  # Initialize an n x n matrix with all elements as 0
    
    for i in range(n):
        running_sum = 0  # Initialize running_sum to 0 for each i
        for j in range(i + 1, n):
            running_sum += a[j - 1]  # Update running_sum with the previous element in the list a
            A[i][j] = running_sum + a[j]  # Update A[i, j] with running_sum + current element in the list a
            
    return A  # Return the resultant matrix