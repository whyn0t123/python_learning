from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #方法一：暴力破解
        for i, num_0 in enumerate(nums):
            for j in range(i+1,len(nums)):
                num_1 = nums[j]
                if num_0 + num_1 == target:
                    return [i, j]
        #方法二：哈希表
        indexs = {}

        for i, num_0 in enumerate(nums):
            indexs[num_0] = i

        for i, num_0 in enumerate(nums):
            num_1 = target - num_0
            if num_1 in indexs and indexs[num_1] != i:
                return[i, indexs[num_1]]
        #方法三：哈希表进阶
        indexs = {}

        for i, num_0 in enumerate(nums):
            num_1 = target - num_0
            if num_1 in indexs:
                return [i,indexs[num_1]]

            indexs[num_0] = i