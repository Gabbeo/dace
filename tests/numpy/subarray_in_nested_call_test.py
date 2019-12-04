import numpy as np
import dace

# dace semantics

M = dace.symbol('M')
K = dace.symbol('K')


@dace.program
def sdfg_transpose(A: dace.float32[M, K], B: dace.float32[K, M]):
    for i, j in dace.map[0:M, 0:K]:
        B[j, i] = A[i, j]


@dace.program
def transpose_test(C: dace.float32[20, 20], D: dace.float32[20, 20]):
    sdfg_transpose(C[:], D[:])

if __name__ == '__main__':
    c = np.random.rand(20, 20).astype(np.float32)
    d = np.zeros((20, 20), dtype=np.float32)

    transpose_test(c, d, K=20, M=20)

    if not np.allclose(c.transpose(), d):
        exit(1)

