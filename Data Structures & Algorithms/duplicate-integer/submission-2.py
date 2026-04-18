class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen= []
        for num in nums:
            for item in seen:
                if num== item:
                    return True
            seen.append(num)
        return False