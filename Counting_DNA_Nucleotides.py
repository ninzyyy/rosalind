def count_nucleotides(seq:list):

    A, C, G, T = 0, 0, 0, 0
    new_list = list(seq)

    for x in new_list:
        if x == 'A':
            A += 1
        elif x == 'C':
            C += 1
        elif x == 'G':
            G += 1
        elif x == 'T':
            T += 1

    return A, C, G, T

print(count_nucleotides('ACGTCGTAGTATGGGTACCC'))
