from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #双指针
        left = 0
        right = len(numbers) - 1

        while not left == right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1 , right + 1]
            
            elif total > target:
                right -= 1
                
            elif total < target:
                left += 1