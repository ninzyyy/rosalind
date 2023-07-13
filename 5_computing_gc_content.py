

f = open('rosalind_gc.txt', 'r') #reads FASTA file

max_gc_name, max_gc_content = '', 0

buf = f.readline().rstrip()
while buf:
    seq_name, seq = buf[1:], ""
    buf = f.readline().rstrip()
    while not buf.startswith('>') and buf:
        seq = seq + buf
        buf = f.readline().rstrip()
    seq_gc_content =((seq.count("C") + seq.count("G")) / len(seq))
    if seq_gc_content > max_gc_content:
        max_gc_name, max_gc_content = seq_name, seq_gc_content

print(max_gc_name, max_gc_content*100)
f.close()

# Example of a FASTA format file
'''
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
'''
