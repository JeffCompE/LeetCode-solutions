from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """Running time: O( log( min(m, n) ) )
        """
        # check edge cases
        m = len(nums1)
        n = len(nums2)
        if m == 0 or n == 0:
            if m == 0:
                nums1, nums2, m, n = nums2, nums1, n, m
            if m % 2 == 1:
                return nums1[m // 2] / 1
            else:
                return (nums1[m // 2 - 1] + nums1[m // 2]) / 2

        # check cases where the maximum of one array <= the minimum of the other one
        # in this case, the median can be directly determined by the index
        total_len = m + n
        if nums1[m - 1] <= nums2[0] or nums2[n - 1] <= nums1[0]:
            if nums2[n - 1] <= nums1[0]:
                nums1, nums2, m, n = nums2, nums1, n, m

            if total_len % 2 == 1:
                k = total_len // 2
                return nums1[k] / 1 if k < m else nums2[k - m] / 1
            else:
                k = total_len // 2
                if k == m:
                    return (nums1[m - 1] + nums2[0]) / 2
                elif k < m:
                    return (nums1[k - 1] + nums1[k]) / 2
                else:
                    return (nums2[k - m - 1] + nums2[k - m]) / 2

        # for common cases, loop to search for the median
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m

        half_len = (total_len + 1) // 2
        i_max = m
        i_min = 0
        while True:
            i = (i_min + i_max) // 2
            j = half_len - i

            if i == 0:
                left_max = nums2[j - 1]
            elif j == 0:
                left_max = nums1[i - 1]
            else:
                left_max = max(nums1[i - 1], nums2[j - 1])

            if i == m:
                right_min = nums2[j]
            elif j == n:
                right_min = nums1[i]
            else:
                right_min = min(nums1[i], nums2[j])

            if left_max <= right_min:
                return left_max / 1 if (m + n) % 2 == 1 else (left_max + right_min) / 2

            if i != 0 and j != n and nums1[i - 1] > nums2[j]:
                # i is too large
                i_max = i - 1

            elif i != m and j != 0 and nums1[i] < nums2[j - 1]:
                # i is too small
                i_min = i + 1
