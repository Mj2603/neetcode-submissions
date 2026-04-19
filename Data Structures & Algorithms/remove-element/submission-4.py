class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums_size = len(nums)
        found = 0
        arr = []
        for x in range(nums_size):
            if nums[x] != val:
                arr.append(nums[x])
                found += 1
        for x in range(nums_size):
            if x >= found:
                break
            nums[x] = arr[x]
        return found


        