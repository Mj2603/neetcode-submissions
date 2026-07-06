class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l,r= 0, min(len(word1), len(word2))

        res= ""

        while l<r:
            res+= word1[l] + word2[l]
            l+=1
        if len(word2)> len(word1):
            return res + word2[r:]
        else:
            return res + word1[r:]