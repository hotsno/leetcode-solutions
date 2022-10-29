class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def helper(r, c):
            prev = matrix[r][c]
            for i in range(4):
                temp = r
                r = c
                c = len(matrix) - 1 - temp
                temp = matrix[r][c]
                matrix[r][c] = prev
                prev = temp

        for r in range((len(matrix) + 1) // 2):
            for c in range(r, len(matrix) - r - 1):
                helper(r, c)

        return matrix
