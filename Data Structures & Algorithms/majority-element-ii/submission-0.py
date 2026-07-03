class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        hmap= {}
        for num in nums:
            hmap[num]= hmap.get(num, 0) + 1

        res= []
        for key, value in hmap.items():
            if value>n/3:
                res.append(key)
        return res

