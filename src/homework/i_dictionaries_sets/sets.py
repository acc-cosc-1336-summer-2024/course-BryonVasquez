# 
def get_p_distance(seq1, seq2): 
    if len(seq1) != len(seq2): 
        raise ValueError("Sequences must have the same length") 
    
    length = len(seq1) 
    mismatches = sum(1 for i in range(length) if seq[i] != seq2[i]) 
    return mismatches / length  

def get_p_distance_matrix(dna_list): 
    n = len(dna_list) 
    matrix = [[0.0] * n for _ in range(n)] 

    for i in range(n): 
        for j in range(i + 1, n): 
            dist = get_p_distance(dna_list[i], dna_list[j]) 
            matrix[i][j] = dist 
            matrix[j][i] = dist 