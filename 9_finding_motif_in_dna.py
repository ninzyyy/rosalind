
def find_motif(seq:str, motif:str):

    positions = []

    for i in range(len(seq)):
        if seq[i:i+len(motif)] == motif:
            positions.append(i+1)

    return positions

print(find_motif('GATATATGCATATACTT', 'ATAT'))
# returns [2, 4, 10]
