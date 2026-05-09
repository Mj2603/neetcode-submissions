class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack= []
        maxa = 0

        for i, h in enumerate(heights):
            start= i

            while stack and stack[-1][1]>h:
                index, height= stack.pop()
                width = (i-index)
                area= height* width
                maxa = max(maxa, area)
                start= index
            stack.append((start,h))

        for index, height in stack:
            maxa= max(maxa, height* (len(heights)- index)) 
        return maxa