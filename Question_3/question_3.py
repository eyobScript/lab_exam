import numpy as np

def reconstruct_matrix(U, S, V):
    S_matrix = np.diag(S)

    reconstructed_matrix = np.dot(U, np.dot(S_matrix, V.T))

    return reconstructed_matrix
#-----This is exammple-----
U = np.array([[1, 0], [0, 1]])
S = np.array([2, 1])
V = np.array([[1, 0], [0, 1]])

reconstructed_matrix = reconstruct_matrix(U, S, V)
print("Reconstructed matrix:\n", reconstructed_matrix)
