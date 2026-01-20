class Solution(object):
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = (m * n) - 1

        while left <= right:
            mid = (left + right) //2
            r = mid // n
            c = mid % n

            if target > matrix[r][c]:
                left = mid +1
            elif target < matrix[r][c]:
                right = mid -1 
            else:
                return True
        return False