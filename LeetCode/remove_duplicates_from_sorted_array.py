from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #读写指针
        write = 0
        read = 0

        while read < len(nums):
            if nums[read] == nums[write]:
                read += 1

            else:
                write += 1
                nums[write] = nums[read]

        nums = [x for x in nums[:write]]

        return write + 1