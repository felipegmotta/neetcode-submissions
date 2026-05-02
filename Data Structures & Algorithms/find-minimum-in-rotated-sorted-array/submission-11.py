class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]

        left = 0
        right = len(nums)
        res = 0

        while True:
            middle = (left + right) // 2

            if nums[middle] == nums[-1]:
                return nums[-1]

            if nums[middle] > nums[middle + 1]:
                return nums[middle + 1]

            if nums[left] < nums[middle]:
                left = middle
            else:
                right = middle

        return res

        
