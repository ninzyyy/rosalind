
def rabbitPairs(months, pairs):

    if months == 1:
        return 1

    elif months == 2:
        return pairs

    children = rabbitPairs(months - 1, pairs)
    parents = rabbitPairs(months - 2, pairs)

    if months <= 4:
        return children + parents

    return children + (parents * pairs)

print(rabbitPairs(5,5))
# returns 41
