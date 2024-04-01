class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)

        if (m + n) % 2 == 1:
            is_odd = True
            median_position = (m + n + 1) // 2
        else:
            is_odd = False
            median_position = (m + n) // 2

        def findMedianInOneArray(nums, start, prev_count, median_position, is_odd):
            pos = start + median_position - prev_count - 1
            if is_odd:
                return nums[pos]
            return (nums[pos] + nums[pos + 1]) / 2

        def findMedianInTwoArrays(
            nums1, start1, nums2, start2, prev_count, median_position, is_odd
        ):
            if nums1[start1] <= nums2[start2]:
                curr_array = nums1
                curr_array_pos = start1
                other_array = nums2
                other_array_pos = start2
            else:
                curr_array = nums2
                curr_array_pos = start2
                other_array = nums1
                other_array_pos = start1

            curr_ans = curr_array[curr_array_pos]
            if is_odd:
                return curr_ans

            if curr_array_pos + 1 >= len(curr_array):
                other_ans = other_array[other_array_pos]
            else:
                other_ans = min(
                    curr_array[curr_array_pos + 1], other_array[other_array_pos]
                )

            return (curr_ans + other_ans) / 2

        def helper(nums1, start1, nums2, start2, median_position, is_odd):
            prev_count = start1 + start2  # this is the number of numbers on the left

            # we are not at the right position, still need to search
            if start1 == len(nums1):
                return findMedianInOneArray(
                    nums2, start2, prev_count, median_position, is_odd
                )
            elif start2 == len(nums2):
                return findMedianInOneArray(
                    nums1, start1, prev_count, median_position, is_odd
                )
            elif prev_count + 1 == median_position:
                return findMedianInTwoArrays(
                    nums1, start1, nums2, start2, prev_count, median_position, is_odd
                )
            else:
                mid1 = (start1 + len(nums1) - 1) // 2
                mid2 = (start2 + len(nums2) - 1) // 2

                if nums1[mid1] <= nums2[mid2]:
                    return helper(
                        nums1, mid1 + 1, nums2, start2, median_position, is_odd
                    )
                else:
                    return helper(
                        nums1, start1, nums2, mid2 + 1, median_position, is_odd
                    )

        return helper(nums1, 0, nums2, 0, median_position, is_odd)


nums1 = [1, 2]
nums2 = [3, 4]

nums1 = [0, 0, 0, 0, 0]
nums2 = [-1, 0, 0, 0, 0, 0, 1]

sol = Solution()

print(sol.findMedianSortedArrays(nums1, nums2))
