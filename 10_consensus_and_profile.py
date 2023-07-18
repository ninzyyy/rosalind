f = open('rosalind_cons.txt', 'r')  #reads FASTA file

sequences = []
buf = f.readline().rstrip()
while buf:
    seq_name, seq = buf[1:], ""
    buf = f.readline().rstrip()
    while not buf.startswith('>') and buf:
        seq = seq + buf
        buf = f.readline().rstrip()
    sequences.append(seq)

f.close()  #close the file after reading

# ['ATCCAGCT', 'GGGCAACT', 'ATGGATCT', 'AAGCAACC', 'TTGGAACT', 'ATGCCATT', 'ATGGCACT']

max_length = max(len(s) for s in sequences)
A, C, G, T = [], [], [], []
consensus = ''

for i in range(max_length):

    nuc_dict = {'A':0, 'C':0, 'G':0, 'T':0}
    for s in sequences:
        nuc_dict[s[i]] += 1

    A.append(nuc_dict['A'])
    C.append(nuc_dict['C'])
    G.append(nuc_dict['G'])
    T.append(nuc_dict['T'])

    counts = [nuc_dict['A'], nuc_dict['C'], nuc_dict['G'], nuc_dict['T']]
    max_count = max(counts) # gets the highest count of nuc

    if counts.count(max_count) > 1: #checks for a tie using count()

        if nuc_dict['A'] == max_count:
            consensus += 'A'
        elif nuc_dict['C'] == max_count:
            consensus += 'C'
        elif nuc_dict['G'] == max_count:
            consensus += 'G'
        elif nuc_dict['T'] == max_count:
            consensus += 'T'

    else:

        if nuc_dict['A'] == max_count:
            consensus += 'A'
        elif nuc_dict['C'] == max_count:
            consensus += 'C'
        elif nuc_dict['G'] == max_count:
            consensus += 'G'
        elif nuc_dict['T'] == max_count:
            consensus += 'T'

print(consensus)
print('A:', ' '.join(map(str, A)))
print('C:', ' '.join(map(str, C)))
print('G:', ' '.join(map(str, G)))
print('T:', ' '.join(map(str, T)))
