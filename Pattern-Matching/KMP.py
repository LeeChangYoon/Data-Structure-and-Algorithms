# KMP Algorithm

# pattern matching function
def pMatch(s, p):
    i, j = 0, 0
    lens = len(s)
    lenp = len(p)

    while i < lens and j < lenp:
        if string[i] == p[j]:
            i += 1
            j += 1

        elif j == 0: i += 1
        else: j = failure[j - 1] + 1

    return (i - lenp) if j == lenp else -1


# fail function
def fail(p):
    n = len(p)
    failure[0] = -1

    for j in range(1, n):
        i = failure[j - 1]
        while p[j] != p[i + 1] and i >= 0: i = failure[i]
        if p[j] == p[i]: failure[j] = i + 1
        else: failure[j] = -1


pattern = "die"
string = "I have no problem. I am prepared to die, I am prepared to."

failure = [0] * len(pattern)
fail(pattern)
print(pMatch(string, pattern))
