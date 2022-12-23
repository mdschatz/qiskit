import numpy as np


# Re-implement with https://en.wikipedia.org/wiki/Row_echelon_form
# From https://9to5science.com/how-to-reduce-matrix-into-row-echelon-form-in-numpy
def row_echelon(A):
    """ Return Row Echelon Form of matrix A """

    # if matrix A has no columns or rows,
    # it is already in REF, so we return itself
    r, c = A.shape
    if r == 0 or c == 0:
        return A

    # we search for non-zero element in the first column
    for i in range(len(A)):
        if A[i,0] != 0:
            break
    else:
        # if all elements in the first column is zero,
        # we perform REF on matrix from second column
        B = row_echelon(A[:,1:])
        # and then add the first zero-column back
        return np.hstack([A[:,:1], B])

    # if non-zero element happens not in the first row,
    # we switch rows
    if i > 0:
        ith_row = A[i].copy()
        A[i] = A[0]
        A[0] = ith_row

    # we divide first row by first element in it
    A[0] = A[0] / A[0,0]
    # we subtract all subsequent rows with first row (it has 1 now as first element)
    # multiplied by the corresponding element in the first column
    A[1:] -= A[0] * A[1:,0:1]

    # we perform REF on matrix from second row, from second column
    B = row_echelon(A[1:,1:])

    # we add first row and first (zero) column, and return
    return np.vstack([A[:1], np.hstack([A[1:,:1], B]) ])


# From https://en.wikipedia.org/wiki/Kernel_(linear_algebra)#Computation_by_Gaussian_elimination
def null_space(A):
	n_vec = A.shape[0]
	v_dim = A.shape[1]
	AI = np.vstack([A, np.eye(v_dim)])
	BC = np.transpose(row_echelon(np.transpose(AI)))
	# print(BC)

	bases = np.random.rand(v_dim, 0)
	for i in range(v_dim):
		if all(x == 0 for x in BC[:n_vec,i]):
			bases = np.hstack([bases, np.reshape(BC[n_vec:,i], [v_dim, 1])])
	return bases
