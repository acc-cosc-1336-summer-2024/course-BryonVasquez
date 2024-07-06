# 
def get_hamming_distance(dna1, dna2): 
    if len(dna1) != len(dna2): 
        raise ValueError("DNA sequences must be of equal length ") 
    return sum(1 for x, y in zip(dna1, dna2) if x != y) 

def get_dna_complement(dna): 
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'} 
    return ''.join(complement[base] for base in dna)  