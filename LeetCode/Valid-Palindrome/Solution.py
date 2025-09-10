class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        r=""
        for i in s:
            if(i.isalnum()):
                r=r+i.lower()
        return r[::-1]==r
        