class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap= {}
        window= {}
        l=0
        for c in s1:
            hashmap[c] = hashmap.get(c,0) + 1
        
        for r in range(len(s2)):
            window[s2[r]] = window.get(s2[r], 0) + 1

            if r-l+1 > len(s1):
                window[s2[l]] -=1
                if window[s2[l]]== 0:
                    window.pop(s2[l])
                l=l+1
            if window == hashmap:
                return True
        return False


        
        