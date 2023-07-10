# First solution
def count_nucleotides(seq:list):

    nuc_dict = {"A":0, "C":0, "G":0, "T":0}

    for nuc in seq:
        if nuc == "A" or nuc == "C" or nuc =='G' or nuc == "T":
            nuc_dict[nuc] += 1

    return nuc_dict["A"], nuc_dict["C"], nuc_dict["G"], nuc_dict["T"]

print(count_nucleotides('AGACGTCTCGTTCTAGAAGGTCGACGCCACAAGCTCTAATGCAGCGGTGAT\
                        CATTGCGCCTCTGTGTTAACCTCTGCGACCCCTCGGTTCGTGACGCGATCCT\
                        TAGTTCAATCTATACCCTCATGCCTCTGGACCTGATTCGTCAGATTTTCCTC\
                        TGACGAAGAAACAGCCACCCAGCCTTGCTCTTCCGACCACTAATCGCTATCG\
                        CTTTCTGGGCAGTGCCGCTAAACGCTTTGTGACGATACGTGGATCCAACCTG\
                        GACCCAGTCGCTACCGACAGCGTTCGCAAATGATGGGTCCAAGGAAGCATAG\
                        TTAGGAAGCCGGGACACGGATGGAGTAACTATGAACGCAGAACCATCGCGCA\
                        TTGGCGTGCGACTGTCTGGAGAGAACATAGGACATGGACCTGTACGTTAATC\
                        CGAATTGTGCGGGCACCCGGACCCTCAGGTACCTAGGCTTGGACTACCTAGA\
                        GTATGGGGAACTGTAGTGAAGGCTCAGGCTCATAATAATTTTACGCTGCTTT\
                        GTACTCCTGAAAAGCTGAAGCTAATATATTGACTTATAGTCTTTAAGAAGAC\
                        GTGTAGGAATCACGGCGGACCTCGTCCTGGGTAAGGTAAGAAAATTTGAGTA\
                        AAGAAGCGATTACACCCCGAGCGCTCCTATCCCCCGTCACGTGGCTAAACTG\
                        GTCCTGCACACTTTTCAGTACCAGCCACTTGGGTTCGCTAATCGGGAGATCT\
                        CGACCGAACTTTTTAACCTAGTACCACGCCAACGATAACCGGCAATGCAATT\
                        TGTCATATCACGGCAAGGAGCGATGTTCGGATACTACCGTAGTTAAGGTTAT\
                        TGAACCTCTGCTGCTATCAGGGAGAGGAGTGATCCCACTTTTTGTCGTAGCT\
                        CTATGATAGGATAGGTTGG'))

# returns (225, 229, 224, 224)
