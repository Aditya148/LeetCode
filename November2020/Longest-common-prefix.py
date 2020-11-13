class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        try:
            if len(strs)==1:
                return strs[0]
            m = min(strs, key=len)
            ans = ''
            for i in range(len(m)):
                flag = True
                for j in range(len(strs)-1):
                    if not (strs[j][i] == strs[j+1][i]):
                        flag = False
                if flag:
                    ans += strs[j][i]
                else:
                    break
            return ans
        
        except:
            return ''
            
'''
Input: strs = ["flower","flow","flight"]
Output: "fl"

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''
