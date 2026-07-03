class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        else:
            mid= len(nums)//2
            pivot= nums.pop(mid)
            less= [i for i in nums if i<= pivot]
            more= [j for j in nums if j>pivot]

            return self.sortArray(less) + [pivot] + self.sortArray(more)
