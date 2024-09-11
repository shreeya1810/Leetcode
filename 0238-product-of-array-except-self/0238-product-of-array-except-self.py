class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        ans = [1] * len(nums)

        i = 1
        j = len(nums)-2
        k = 0
        prefix[0] = 1
        suffix [len(nums)-1] = 1

        while (i < len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
            i+=1

        while (j > -1):
            suffix[j] = suffix[j+1] * nums[j+1]
            j-=1

        while (k < len(nums)):
            ans[k] = prefix[k] * suffix[k]
            k+=1

        return ans

        