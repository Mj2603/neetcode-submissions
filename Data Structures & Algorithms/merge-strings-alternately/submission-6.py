class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l=0
        r= min(len(word1), len(word2))
        res=""

        while l<r:
            res += word1[l]
            res += word2[l]
            l+=1

        if len(word1)>len(word2):
            res += word1[r:]
        else:
            res += word2[r:]
        return res

