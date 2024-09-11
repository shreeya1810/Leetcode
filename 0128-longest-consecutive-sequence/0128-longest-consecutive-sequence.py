class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        start = set()
        for item in nums:
            start.add(item) 

        longest = 0

        for num in nums:
            if num-1 not in start:
                length=0
                while num+length in start:
                    length+=1
                if length>longest:
                    longest=length
        return longest



