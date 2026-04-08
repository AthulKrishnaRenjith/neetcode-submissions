class Solution:

    def encode(self, strs: List[str]) -> str:

        encod = []

        for i in range(len(strs)):
            encod.append(str(len(strs[i])) + '#' + strs[i])
        return "".join(encod)

    def decode(self, s: str) -> List[str]:

        decod = []
        nums = ""
        i = 0

        while i < len(s):
            if s[i] != '#':
                nums = nums + s[i]
                i = i + 1
            elif s[i] == '#':
                decod.append(s[i + 1 : i + 1 + int(nums)])
                i = i + 1 + int(nums)
                nums = ""
        return decod

