
def countPointMut(seq1:str, seq2:str):

    counter = 0

    for x, y in zip(seq1, seq2):
        if x != y:
            counter += 1
        else:
            continue

    return counter

print(countPointMut('GAGCCTACTAACGGGAT','CATCGTAATGACGGCCT'))
