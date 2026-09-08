class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n= len(heights)
        maxa= 0
        l,r= 0, n-1

        while l<r:
            width= r-l
            a= min(heights[l], heights[r]) * width
            maxa= max(a, maxa)
            if heights[l]> heights[r]:
                r-=1
            else:
                l+=1
        return maxa