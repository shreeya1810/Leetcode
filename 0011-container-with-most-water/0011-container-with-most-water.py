class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        i = 0
        j = len(height)-1
        max = (j-i)*min(height[i], height[j])

        while i < j:
            if height[i]<height[j]:
                i+=1
            else:
                j-=1

            if max<(j-i)*min(height[i], height[j]):
                max = (j-i)*min(height[i], height[j])
        return max
            
        