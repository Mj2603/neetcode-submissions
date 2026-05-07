class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hashmap = {}
        window= {}

        for c in t:
            hashmap[c] = hashmap.get(c,0)+ 1

        have, need = 0, len(hashmap)
        res, resl= [-1,-1], float("inf")
        l=0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c,0) +1

            if c in hashmap and window[c]==hashmap[c]:
                have +=1

            while have==need:
                if r-l+1 < resl:
                    res = [l,r]
                    resl = r-l+1
                window[s[l]] -= 1
                if s[l] in hashmap and window[s[l]] < hashmap[s[l]]:
                    have -=1
                l+=1
        return s[res[0]:res[1]+1]



        




    
            
        
        

        

