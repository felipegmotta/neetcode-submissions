class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        validator = set(nums)
        # validator.update(nums)

        return len(nums) > len(validator)