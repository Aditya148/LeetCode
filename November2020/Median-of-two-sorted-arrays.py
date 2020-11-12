class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = sorted(nums1 + nums2)
        l = len(num)
        ans = lambda l: (num[int(l/2)-1]+num[int(l/2)])/2 if l%2==0 else num[int(l/2)]
        return ans(l)
        
'''
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2
'''
