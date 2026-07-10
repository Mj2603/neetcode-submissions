class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res= []
        def kSum(start, target,k, path):
            if k==2:
                l,r= start, len(nums)-1
                while l <r:
                    curr_sum= nums[l] + nums[r]
                    if curr_sum< target:
                        l+=1
                    elif curr_sum> target:
                        r-=1
                    else:
                        res.append(path + [nums[l], nums[r]])
                        l+=1
                        r-=1
                        while l<r and nums[l] ==nums[l-1]:
                            l+=1
                        while l<r and nums[r] == nums[r+1]:
                            r-=1
                return


            for i in range(start, len(nums)):
                if i>start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                kSum(i+1, target- nums[i], k-1, path)
                path.pop()

        kSum(0, target, 4, [])
        return res
