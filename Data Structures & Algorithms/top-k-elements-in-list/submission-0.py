class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ht = {}

        for num in nums:
            ht[num] = ht.get(num, 0) + 1

        sorted_num = sorted(list(ht.keys()), key = lambda x: ht[x], reverse=True)

        return sorted_num[:k]