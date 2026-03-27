def sums(array: list) -> int:
    sums = {0}

    for num in array:
        new_sums = set()

        for s in sums:
            new_sums.add(s + num)

        sums.update(new_sums)

    return len(sums)
