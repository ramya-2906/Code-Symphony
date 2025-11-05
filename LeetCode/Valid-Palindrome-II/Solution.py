class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Helper function to check palindrome
        def palCheck(s):
            return s == s[::-1]

        l, r = 0, len(s) - 1

        while l < r:
            if s[l] == s[r]:
                # Move inward if chars match
                l += 1
                r -= 1
            else:
                # Skip either left or right char
                return palCheck(s[:l] + s[l+1:]) or palCheck(s[:r] + s[r+1:])
        
        return True