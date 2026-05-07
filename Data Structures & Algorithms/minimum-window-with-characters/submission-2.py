class Solution:
    def minWindow(self, s: str, t: str) -> str:
       target ={}
       window= {}

       for c in t:
        target[c] = target.get(c,0) + 1

       have, need = 0, len(target)
       l=0
       res, resl= [-1,-1], float("inf")

       for r in range(len(s)):
        window[s[r]]= window.get(s[r], 0) + 1
        if s[r] in target and window[s[r]] == target[s[r]]:
            have +=1
        while have == need:
            if r-l+1 < resl:
                res= [l,r]
                resl = r-l+1
            window[s[l]] -= 1

            if s[l] in target and window[s[l]] < target[s[l]]:
                have-=1
            l+=1
       return  s[res[0]: res[1]+1] if resl != float('inf') else ""
