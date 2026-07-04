class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n= len(nums)
        nat= [i for i in range(1,20)]

        for i in range(n):
            if nums[i] in nat:
                nat.remove(nums[i])
        return min(nat)
            