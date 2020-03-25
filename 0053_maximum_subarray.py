# Runtime: 124 ms, faster than 5.45% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 13.6 MB, less than 65.85% of Python3 online submissions for Maximum Subarray.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Method 1: O(n) time
        # max_sum = float('-inf')
        # min_cum_sum = cum_sum = 0
        # for i in range(len(nums)):
        #     min_cum_sum = min(min_cum_sum, cum_sum)
        #     cum_sum += nums[i]
        #     max_sum = max(max_sum, cum_sum - min_cum_sum)
        # return max_sum
        
        # divide-and-conquer O(nlogn) time
        def max_sub_array(left, right, s):
            if left == right:
                return s[left]
            mid = (left + right) // 2
            
            return max(max_sub_array(left, mid, s), max_sub_array(mid + 1, right, s), max_cross_array(left, right, mid, s))
        
        def max_cross_array(left, right, mid, s):
            cur_sum, left_max_sum = 0, float('-inf')
            for i in range(mid, left - 1, -1):
                cur_sum += s[i]
                if cur_sum > left_max_sum:
                    left_max_sum = cur_sum
            cur_sum, right_max_sum = 0, float('-inf')
            for i in range(mid + 1, right + 1):
                cur_sum += s[i]
                if cur_sum > right_max_sum:
                    right_max_sum = cur_sum
            return left_max_sum + right_max_sum
        
        return max_sub_array(0, len(nums) - 1, nums)
        