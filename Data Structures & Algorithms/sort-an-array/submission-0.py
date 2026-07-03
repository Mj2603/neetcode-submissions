class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n= len(nums)

        for i in range(n):
            j = i-1
            while j>=0 and nums[j] > nums[j+1]:
                tmp= nums[j+1]
                nums[j+1]= nums[j]
                nums[j]= tmp
                j-=1
        return nums
