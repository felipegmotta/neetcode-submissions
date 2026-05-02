class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = []
        suffix = []
        
        prefix_product = 1
        i = 0
        while i < len(nums):
            prefix.append(prefix_product)
            prefix_product *= nums[i]
            i += 1

        suffix_product = 1
        i = len(nums) - 1
        while i >= 0:
            suffix.append(suffix_product)
            suffix_product *= nums[i]
            i -= 1

        res = []
        j = len(nums) - 1
        for i in range(len(nums)):
            res.append(prefix[i]*suffix[j])
            j -= 1

        return res