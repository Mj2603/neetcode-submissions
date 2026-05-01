class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mxl=0
        l=0
        hash= {}

        for r in range(len(s)):
            hash[s[r]] = hash.get(s[r],0) +1
            if (r-l+1)- max(hash.values()) > k:
                hash[s[l]] -=1
                l +=1
            mxl = max(mxl, r-l+1)
        return mxl
            




        


        

            

        