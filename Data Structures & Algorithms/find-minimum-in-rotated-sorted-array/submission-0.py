class Solution:
    def findMin(self, nums: List[int]) -> int:

        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            # If the current subarray is already sorted
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            mid = (l + r) // 2
            res = min(res, nums[mid])

            # If mid is part of the left sorted portion, explore the right
            if nums[mid] >= nums[l]:
                l = mid + 1
            # If mid is part of the right sorted portion, explore the left
            else:
                r = mid - 1
                
        return res