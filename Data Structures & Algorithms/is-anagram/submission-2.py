class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap = {}
        for i in s:
            hashmap[i] = hashmap.get(i, 0) + 1
        for j in t:
            hashmap[j] = hashmap.get(j,0) - 1
        
        return all(x== 0 for x in hashmap.values())
        
        