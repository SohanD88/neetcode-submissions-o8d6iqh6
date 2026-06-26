class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Brute force = loop through the entire matrix to find our number
            #O(N*M) time complexity with O(1) space

            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    if matrix[i][j] == target:
                        return True


            return False