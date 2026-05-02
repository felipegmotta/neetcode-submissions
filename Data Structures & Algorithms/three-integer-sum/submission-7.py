class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        sorted_nums = sorted(nums)
        for idx, num in enumerate(sorted_nums[:-2]):
            start = idx + 1
            end = len(sorted_nums) - 1

            while start < end:
                triplet = [num, sorted_nums[start], sorted_nums[end]]
                triplet_sum = sum(triplet)

                if triplet_sum == 0:
                    if triplet not in result:
                        result.append(triplet)
                    start += 1
                elif triplet_sum > 0:
                    end -= 1
                else:
                    start += 1

        return result

        # [-4, -1, -1, 0, 1, 2, 2, 4]
        # [0,0,0,0]



