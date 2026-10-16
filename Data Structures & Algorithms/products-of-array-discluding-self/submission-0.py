class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_idx = set([])
        prod_with_no_zero = 1
        res = []

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_idx.add(i)
            else:
                prod_with_no_zero *= nums[i]

        if len(zero_idx) == 0:
            return [prod_with_no_zero // num for num in nums]

        if len(zero_idx) > 1:
            return [0 for _ in range(len(nums))]

        for i in range(len(nums)):
            if i in zero_idx:
                res.append(prod_with_no_zero)
            else:
                res.append(0)

        return res