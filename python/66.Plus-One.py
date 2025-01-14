class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = int("".join(str(d) for d in digits))
        num += 1
        ans = []
        for i in str(num):
            ans.append(int(i))
        return ans