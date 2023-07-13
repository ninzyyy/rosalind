
def dna_complementation(seq:str):

    seq = seq.replace('A', 't').replace('T','a').replace('C', 'g').replace('G', 'c').upper()[::-1]

    return seq

print(dna_complementation('AAAACCCGGT'))
# returns ACCGGGTTTT
