
def computeGC(seq:str):

    GC = seq.count("G") + seq.count("C")
    total = len(seq)

    return (GC/total)*100



print(computeGC('CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT'))
# returns 60.91954
