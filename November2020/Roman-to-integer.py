class Solution:
    def romanToInt(self, s: str) -> int:
        dct={'I':1,'V':5,'X':10,'L':50, 'C':100, 'D':500, 'M':1000}
        ans = 0
        n=len(s)
        for i, r in enumerate(s):
            ans+= -dct[r] if i<n-1 and dct[r]<dct[s[i+1]]  else dct[r]
        return ans
        
'''
Input: s = "III"
Output: 3

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
'''
