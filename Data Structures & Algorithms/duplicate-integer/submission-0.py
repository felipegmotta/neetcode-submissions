class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        validator = set()

        for num in nums:
            validator.add(num)

        return len(nums) > len(validator)