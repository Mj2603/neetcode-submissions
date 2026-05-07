class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        res =[]

        while l<len(nums)-k+1:
            r= l+k
            window = nums[l:r]
            max_num = max(window)
            res.append(max_num)
            l= l+1
        return res
