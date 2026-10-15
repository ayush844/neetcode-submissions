class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sort_str = ["".join(sorted(text)) for text in strs]

        hash_table = {}

        for i, text in enumerate(sort_str):
            if text in hash_table:
                hash_table[text].append(strs[i])
            else:
                hash_table[text] = [strs[i]]

        return list(hash_table.values())