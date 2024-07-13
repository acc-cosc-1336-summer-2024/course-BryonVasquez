# 
def main(): 
    dna_sequences = [ 
        ['T', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'A'] 
        ['G', 'A', 'T', 'T', 'C', 'A', 'T', 'T', 'T', 'C'] 
        ['T', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'T'] 
        ['G', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'A'] 
    ] 
    Try: 
        distance_matrix = get_p_distance_matrix(dna_sequences) 
        for row in distance_matrix: 
            print(" ".join(f"{vaule:.5f}" for vaule in row))  
        
        except ValueError as e: 
print(f"Error: {e}") 
 

         