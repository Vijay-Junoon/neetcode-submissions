class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows,cols = len(matrix), len(matrix[0])
        left,right = 0, (rows*cols)-1

        while left <= right:

            mid = (left+right)//2
            row_ind = mid//cols
            col_ind = mid%cols

            if matrix[row_ind][col_ind] == target:
                return True
            elif matrix[row_ind][col_ind] < target:
                left = mid + 1
            else:
                right = mid - 1
            
        return False