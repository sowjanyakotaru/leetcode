class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count=0
        maxcount=0
        for num in nums:
            if num==1:
                count+=1
            else:
                count=0
            maxcount=max(maxcount,count)
        return maxcount
        