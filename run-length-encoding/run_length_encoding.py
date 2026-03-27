ab = '0123456789'
def decode(s):
    c = ''
    q = ''
    if len(s) > 0:
        for i in range(len(s)):
            if s[i] in ab:
                c += s[i]
            elif s[i] not in ab and c == '':
                q += s[i]
            else:
                q += int(c)*(s[i])
                c = ''
        return q
    else:
        return s


def encode(s):
    c = 1
    q = ''
    if len(s) > 1:
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                c += 1
                if i == len(s) - 2:
                    q += str(c) + s[i + 1]
            if s[i] != s[i + 1]:
                if c > 1:
                    q += str(c) + s[i]
                    c = 1
                else:
                    q += s[i]
        if s[-1] != q[-1]: q += s[-1]
        return q
    else:
        return s
