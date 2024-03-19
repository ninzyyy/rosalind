from Bio import SeqIO

def overlap_graphs(input):

    k = 3
    arr, solution = [], []

    fasta_sequences = SeqIO.parse(open(input),'fasta')
    for fasta in fasta_sequences:
        arr.append([fasta.id, str(fasta.seq)])

    for first in arr:
        for second in arr:

            first_suff = first[1][-k:]
            second_pref = second[1][:k]

            if first[1] == second[1]:
                continue
            if first_suff == second_pref:
                solution.append(f"{first[0]} {second[0]}")


    with open('solution2.txt', 'w') as f:
        for line in solution:
            f.write(f"{line}\n")

overlap_graphs('rosalind_grph-4.txt')