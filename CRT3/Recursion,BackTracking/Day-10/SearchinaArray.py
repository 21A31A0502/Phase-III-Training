def matSearch(self, mat, N, M, X):
        # Complete this function
        for i in range (N):
            for j in range (M):
                if mat[i][j] == X:
                    return 1
        return 0