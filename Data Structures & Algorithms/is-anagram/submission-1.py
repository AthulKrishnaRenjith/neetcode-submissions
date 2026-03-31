class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        strlist1 = list(s)
        strlist2 = list(t)
        sortstrlist1 = sorted(strlist1)
        sortstrlist2 = sorted(strlist2)
        if sortstrlist1 == sortstrlist2:
            return True
        else:
            return False
        