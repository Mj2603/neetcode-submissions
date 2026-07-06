class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l<r:
            if s[l] != s[r]:
                return self.ispalindrome(s, l+1, r) or self.ispalindrome(s, l, r-1)
            l+=1
            r-=1
        return True

    def ispalindrome(self, s,l,r):
        while l<r:
            if s[r] != s[l]:
                return False
            l+=1
            r-=1
        return True
