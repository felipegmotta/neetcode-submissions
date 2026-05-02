class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}
        for i, num in enumerate(nums):
            if num in hashmap.keys():
                return [hashmap[num], i]

            difference = target - nums[i]
            hashmap[difference] = i

            

