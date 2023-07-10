
def computeGC(seq:str):

    GC = 0
    for nuc in seq:
        if nuc == "G" or nuc == "C":
            GC += 1

    total = len(seq)

    return round(((GC/total)*100), 6)

print(computeGC('CGTTGCATGGACCTTCTCAAAAGTACTCTAGGTTGCATGACTGGACTGTGGATAGTTAGG\
GATTTAGTACACCGGAAGAGATTCTTACGAGTTAAAGGGAACCAACGCTTTCTACACCGC\
GTCGGCTTCGCTATAGAGCACAGCTCAAGCAGCGCCTTAAAACATAGTATTTGATGACAC\
AAGTGTACTAAAATAGCACGTTGATCAGAGACCCAGTTGTAATTTGGTACAATAACAGCC\
CTTGAATGCCTGCGGTTAGCGAGTCCTTTTTATGCTTGGCGACGGAGTGACCGAGGCTCT\
CGTCTTTTGTCTGAGGTTGGCGTCAACGTTCCATCGCAGCCCCATCTGGTCGCAACGAAA\
ACCACCAGGACTCCTAATCGACGTGTATGCTCAGTTTACGGAACTCGGAATACCTTTACG\
AGAATGATGACAGTCTCCAAGTCGACCGTGAGCTTTGTGGTGTTTCGTGTCACTTTTTTC\
GCGGGCCACTTACAACCCTCGCCACTCCTTTATCATTACACAATGATTCCACCCTGTGTA\
ACTCACATGTGCTTAAAGTCTGATATTCGATTTGCCGTGGTAAGCCGATTGACGTTTAGC\
CTCCCTTCACCTAGATACCGTCAAAACGATCCCGTGGGCTTCGGGGCTAACAGATACACC\
GGGATGTCCCGCGTCCGTACGATATCTACCTTCGTCTCGGGCTAGGAACACTTATGCCAT\
CAGCTCACGCCTGATGCTCCCCTTTGGCTCCTTCTGCCGCAGAATGTCCGGAGCCTTCGA\
TTTCACCTTATCGTTACTACGGAAACCGGCCGAGATTCCCGCGCAAGGCCTCGAGGAATT\
CCAATCACTTTTAAACCTATCCAAGTGGTTATGACGTATTACAATGTCCACAACTTCGTC\
CCCGGCTGTTTGCCAATCGAAAAATAAGGGGTTCCGTGCTGGCAGGCTCCACATATGCAG\
AAGGTGAATT'))
# returns 60.91954