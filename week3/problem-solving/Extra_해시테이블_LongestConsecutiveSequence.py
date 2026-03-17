# 해시 테이블 - Longest Consecutive Sequence
# 문제 링크: https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest = 0
        if set_nums :
            for n in set_nums:
                if n-1 not in set_nums:
                    length = 1
                    while n+length in set_nums:
                        length+=1
                    if length > longest :
                        longest = length
        return longest