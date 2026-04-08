class Solution:

    def encode(self, strs: List[str]) -> str:

        encod = []

        for i in range(len(strs)):
            count = 0
            for j in range(len(strs[i])):
                count = count + 1
            encod.append(str(count))
            encod.append('#')
            encod.append(strs[i])
        return "".join(encod)

    def decode(self, s: str) -> List[str]:

        decod = []
        nums = ""
        string = []
        i = 0

        while i < len(s):
            if s[i] != '#':
                nums = nums + s[i]
                i = i + 1
            elif s[i] == '#':
                for j in range(int(nums)):
                    i = i + 1
                    string.append(s[i])
                nums = ""
                decod.append("".join(string))
                string = []
                i = i + 1
        return decod

