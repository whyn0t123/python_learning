class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #滑动窗口
        left = 0
        window = set()
        max_len = 0

        for right in range(0, len(s)):
            while s[right] in window:
                window.remove(s[left])
                left += 1

            window.add(s[right])
            max_len = max(max_len, len(window))

        return max_len