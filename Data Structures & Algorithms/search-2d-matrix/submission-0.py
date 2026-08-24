class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_cols = len(matrix[0])
        num_rows = len(matrix)
        
        for i in range(len(matrix)):
            if target > matrix[i][num_cols - 1]:
                if i == num_rows - 1:
                    return False
                continue
            
            # binary search within the row:
            left, right = 0, len(matrix[i]) - 1

            while left <= right:
                mid = (left + right) //2

                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return False