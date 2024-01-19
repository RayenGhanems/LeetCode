class Solution(object):
    def minFallingPathSum(self, matrix):
        n = len(matrix)
        dict1 = {}  
        dict2 = {}  
        for col in range(n):
            dict1[col] = matrix[0][col]
        for row in range(1, n):
            dict2.clear()
            for col in range(n):
                prev_cols = [col - 1, col, col + 1]
                valid_prev_cols = [c for c in prev_cols if c >= 0 and c < n]
                dict2[col] = matrix[row][col] + min(dict1[c] for c in valid_prev_cols)
            dict1.clear()
            dict1.update(dict2)
        return min(dict1.values())

