
def translation(seq:str):

    codon_table = {
    'UUU': 'F',    # Phenylalanine
    'UUC': 'F',    # Phenylalanine
    'UUA': 'L',    # Leucine
    'UUG': 'L',    # Leucine
    'CUU': 'L',    # Leucine
    'CUC': 'L',    # Leucine
    'CUA': 'L',    # Leucine
    'CUG': 'L',    # Leucine
    'AUU': 'I',    # Isoleucine
    'AUC': 'I',    # Isoleucine
    'AUA': 'I',    # Isoleucine
    'AUG': 'M',    # Methionine
    'GUU': 'V',    # Valine
    'GUC': 'V',    # Valine
    'GUA': 'V',    # Valine
    'GUG': 'V',    # Valine
    'UCU': 'S',    # Serine
    'UCC': 'S',    # Serine
    'UCA': 'S',    # Serine
    'UCG': 'S',    # Serine
    'CCU': 'P',    # Proline
    'CCC': 'P',    # Proline
    'CCA': 'P',    # Proline
    'CCG': 'P',    # Proline
    'ACU': 'T',    # Threonine
    'ACC': 'T',    # Threonine
    'ACA': 'T',    # Threonine
    'ACG': 'T',    # Threonine
    'GCU': 'A',    # Alanine
    'GCC': 'A',    # Alanine
    'GCA': 'A',    # Alanine
    'GCG': 'A',    # Alanine
    'UAU': 'Y',    # Tyrosine
    'UAC': 'Y',    # Tyrosine
    'UAA': '',     # Stop
    'UAG': '',     # Stop
    'CAU': 'H',    # Histidine
    'CAC': 'H',    # Histidine
    'CAA': 'Q',    # Glutamine
    'CAG': 'Q',    # Glutamine
    'AAU': 'N',    # Asparagine
    'AAC': 'N',    # Asparagine
    'AAA': 'K',    # Lysine
    'AAG': 'K',    # Lysine
    'GAU': 'D',    # Aspartic Acid
    'GAC': 'D',    # Aspartic Acid
    'GAA': 'E',    # Glutamic Acid
    'GAG': 'E',    # Glutamic Acid
    'UGU': 'C',    # Cysteine
    'UGC': 'C',    # Cysteine
    'UGA': '',     # Stop
    'UGG': 'W',    # Tryptophan
    'CGU': 'R',    # Arginine
    'CGC': 'R',    # Arginine
    'CGA': 'R',    # Arginine
    'CGG': 'R',    # Arginine
    'AGU': 'S',    # Serine
    'AGC': 'S',    # Serine
    'AGA': 'R',    # Arginine
    'AGG': 'R',    # Arginine
    'GGU': 'G',    # Glycine
    'GGC': 'G',    # Glycine
    'GGA': 'G',    # Glycine
    'GGG': 'G'     # Glycine
    }

    translated_seq = []
    seq = [nuc for nuc in seq]
    codons = [''.join(seq[i:i+3]) for i in range(0, len(seq), 3)]

    for n in codons:
        if codon_table[n] == '':
            break
        translated_seq.append(codon_table[n])

    translated_seq = "".join(translated_seq)
    return translated_seq

print(translation('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'))
# returns MAMAPRTEINSTRING
