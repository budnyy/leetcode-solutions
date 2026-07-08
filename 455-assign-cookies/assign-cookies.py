class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        output, i, j = 0, 0, 0
        s.sort()
        g.sort()
        while i < len(s) and j < len(g):
            if s[i] >= g[j]:
                output += 1
                j += 1
            i += 1
        return output

            