class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        element_index = {}
        n = len(nums)

        for i in range(n):
            req = target-nums[i]

            if req in element_index:
                return [element_index[req], i]

            element_index[nums[i]] = i

        return [-1, -1]