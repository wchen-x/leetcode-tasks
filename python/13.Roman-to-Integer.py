class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for i in range(len(s)):
            if s[i] == 'I':
                if i < len(s) - 1 and (s[i + 1] == 'V' or s[i + 1] == 'X'):
                    ans -= 1
                else:
                    ans += 1
            elif s[i] == 'V':
                ans += 5
            elif s[i] == 'X':
                if i < len(s) - 1 and (s[i + 1] == 'L' or s[i + 1] == 'C'):
                    ans -= 10
                else:
                    ans += 10
            elif s[i] == 'L':
                ans += 50
            elif s[i] == 'C':
                if i < len(s) - 1 and (s[i + 1] == 'D' or s[i + 1] == 'M'):
                    ans -= 100
                else:
                    ans += 100
            elif s[i] == 'D':
                ans += 500
            elif s[i] == 'M':
                ans += 1000

        return ans