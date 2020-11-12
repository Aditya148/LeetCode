class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max = 0
        for i in range(len(s)):
            sub = []
            for ch in s[i:]:
                if ch not in sub:
                    sub.append(ch)
                elif ch in sub:
                    break
            if len(sub)>max:
                max=len(sub)
        return max
        
'''
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3
'''
