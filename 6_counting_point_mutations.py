
def countPointMut(seq1:str, seq2:str):

    return sum([a!=b for a, b in zip(seq1, seq2)]) # Sums a list of True/False (1/0) matches


print(countPointMut('GAGCCTACTAACGGGAT','CATCGTAATGACGGCCT'))
