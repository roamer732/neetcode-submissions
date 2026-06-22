class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = len(matrix[0])
        row = len(matrix)
        l, r = 0, (col*row)-1
        while l <= r:
            m = l + (r-l)//2
            i, j = m//col, m%col
            if target < matrix[i][j]:
                r = m - 1
            elif target > matrix[i][j]:
                l = m + 1
            else:
                return True
        return False