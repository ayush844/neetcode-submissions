class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for text in strs:
            res += str(len(text))
            res += '#'
            res += text

        return res

    def decode(self, s: str) -> List[str]:

        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1

            next_text_size = int(s[i:j])
            res.append(s[j+1 : j+1+next_text_size])
            i = j+1+next_text_size

        return res