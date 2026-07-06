class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l= min(len(word1), len(word2))
        res= []

        for r in range(l):
            res.append(word1[r])
            res.append(word2[r])
        
        if len(word1) > l:
            res.append(word1[l:])
        else:
            res.append(word2[l:])
        return "".join(res)