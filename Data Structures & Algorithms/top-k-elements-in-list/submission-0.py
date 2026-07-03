class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n= len(nums)
        hmap= {}
        bucket= [[] for _ in range(n+1)]

        for i in range(n):
            hmap[nums[i]]= hmap.get(nums[i], 0) + 1

        for num, freq in hmap.items():
            bucket[freq].append(num)

        res= []
        for i in range(n,-1,-1):
            if bucket[i]:
                res.extend(bucket[i])
                if len(res)== k:
                    return res

