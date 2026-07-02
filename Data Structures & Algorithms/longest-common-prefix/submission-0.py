class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cmn= strs[0]
        res= ""
        for i in range(len(cmn)):
            for s in strs:
                if i== len(s) or s[i] != cmn[i]:
                    return res
            res= res+ cmn[i]

        return res