class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n= len(nums)
        counter = {}
        bucket= [[] for _ in range(n+1)]

        for i in range(n):
            counter[nums[i]] = counter.get(nums[i], 0) + 1

        for num, freq in counter.items():
            bucket[freq].append(num)
        res= []
        for i in range(n, 0, -1):
            for t in bucket[i]:
                res.append(t)
            if len(res) == k:
                return res







