class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        ans = ''
        for s in str(x):
            if s == '-':
                negative = True
                continue
            ans += s
        ans = int(ans[-1::-1])
        if negative:
            ans = int('-'+str(ans))
        if ans>pow(-2,31) and ans<pow(2,31):
            return ans
        else:
            return 0
            
'''
Input: x = 120
Output: 21

Input: x = -123
Output: -321
'''
