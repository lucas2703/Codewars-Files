def solution(s):
    if len(s) == 0:
        return []
    n = 2
    s = [s[i:i+n] for i in range(0, len(s), n)]
    if len(s[len(s) - 1]) == 1:
        s[len(s) - 1] = s[len(s) - 1] + "_"
    return s
