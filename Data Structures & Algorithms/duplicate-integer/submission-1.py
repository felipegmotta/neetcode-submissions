class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        validator = set()
        validator.update(nums)
        # for num in nums:
        #     validator.add(num)

        return len(nums) > len(validator)