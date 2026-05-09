class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
         n= len(heights)
         max_area= 0

         for i in range(n):
            height= heights[i]

            left= i
            right= i

            while left>0 and heights[left-1]>=height:
                left-=1
            while right< n-1 and heights[right+1]>= height:
                right+=1

            width = right-left+1
            area = height * width

            max_area= max(max_area, area)
         return max_area   