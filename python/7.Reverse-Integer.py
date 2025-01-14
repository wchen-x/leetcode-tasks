class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        string = str(x)
        is_negative = string[0] == '-'
        if is_negative:
            start_idx = 1 
        else:
            start_idx = 0
        ans = ""
        
        for i in reversed(range(start_idx, len(string))):
            ans += string[i]

        if not is_negative:
            ans = int(ans)
        else: 
            ans = -int(ans)

        if ans < -2**31 or ans > 2**31 - 1:
            return 0
            
        return ans