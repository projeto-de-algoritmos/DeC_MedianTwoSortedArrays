# Caso de Teste 2
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

import medianTwoSortedArrays as ma

nums1 = [1,2]
nums2 = [3,4]

solution = ma.Solution()
print(f"Sorted arrays: \nnums1: {nums1}\nnums2: {nums2}")
result = solution.findMedianSortedArrays(nums1, nums2)
print(f"Solution: {result}")