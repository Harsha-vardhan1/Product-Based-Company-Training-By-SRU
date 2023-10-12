class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)
        cnt = [0] * 7
        p = 0
        for i in range(n -1, -1, -1):
            cnt[i] = (ord(columnTitle[i]) - ord('A') + 1) * 26 ** p
            p += 1
        return sum(cnt)
