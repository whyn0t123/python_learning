from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #滑动窗口（快慢指针）
        slow = 0
        fast = 0
        total = 0
        length = float('inf')

        for fast in range(0, len(nums)):
            total += nums[fast]

            while total >= target:
                length = min(length, fast - slow + 1)
                total -= nums[slow]
                slow += 1

        return length if length != float('inf') else 0