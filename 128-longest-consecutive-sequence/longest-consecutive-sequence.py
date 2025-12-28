class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        out = 0

        for n in nums:
            if n - 1 not in nums:   # start of a sequence
                length = 1
                while n + length in nums:
                    length += 1
                out = max(out, length)

        return out
