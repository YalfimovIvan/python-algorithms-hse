def message(q: str) -> int:
    if not q:
        return 0
    n = len(q)
    drt = [1] + [0] * n

    for i in range(1, n + 1):
        if '1' <= q[i - 1] <= '9':
            drt[i] = drt[i - 1]
        if i > 1 and '10' <= q[i - 2:i] <= '33':
            drt[i] += drt[i - 2]
        if q[i - 1] == '0':
            drt[i] += drt[i - 1]
    return drt[n]
