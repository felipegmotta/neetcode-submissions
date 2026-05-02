class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1]*len(nums)
        print(res)
        for idx1, num1 in enumerate(nums):
            for idx2, num2 in enumerate(nums):
                if idx2 == idx1:
                    continue
                res[idx1] *= num2

        return res

        # [1,2,4,6]
        # [1,1,1,1]