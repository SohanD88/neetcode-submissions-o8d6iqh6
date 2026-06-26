class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Brute force = loop through the entire matrix to find our number
            #O(N*M) time complexity with O(1) space

        """ for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    if matrix[i][j] == target:
                        return True


            return False"""


        #Optimal solution
        #We have to perform a binary search on this matrix
        rows, cols = len(matrix), len(matrix[0])

        l, r = 0, (rows*cols) - 1


        while l <= r:
            m = l + (r - l) // 2

            row = (m // cols)
            col = (m % cols)

            if matrix[row][col] > target:
                r = m - 1
            elif matrix[row][col] < target:
                l = m + 1

            else:
                return True

        return False
