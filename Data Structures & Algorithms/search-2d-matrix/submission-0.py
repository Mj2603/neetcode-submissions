class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols= len(matrix), len(matrix[0])
        low, high= 0, (rows*cols)- 1

        while low<= high:
            mid= (low+ high)//2

            r= mid//cols
            c= mid%cols

            val= matrix[r][c]

            if val < target:
                low= mid+1
            elif val>target:
                high= mid-1
            else:
                return True
        return False
            



