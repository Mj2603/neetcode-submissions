class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res=[]

        for k,a in enumerate(nums):
            if k>0 and a == nums[k-1]:
                continue
            i= k+1
            j= len(nums)-1
            while i<j:
                sum1= nums[i] + nums[j] + a
                if sum1> 0:
                    j-=1
                elif sum1< 0:
                    i+=1
                else:
                    res.append([nums[i],nums[j],a])
                    i+=1
                    while i<j and nums[i] == nums[i-1]:
                        i+=1
        return res