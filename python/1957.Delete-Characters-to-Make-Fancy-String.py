class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """

        ans = ""

        for i in range(len(s)):
            if i + 2 < len(s) and s[i] == s[i + 1] and s[i] == s[i + 2]:
                continue
            else:
                ans += s[i]
        return ans