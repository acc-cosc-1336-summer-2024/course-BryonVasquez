# 
import unittest 
from src.homework.i_dictionaries_sets import get_p_distance, get_p_distance_matrix 

class TestDistanceFunctions(unittest.TestCase): 

    def test_get_p_distance(self): 
        seq1 = ['T', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'A'] 
        seq2 = ['G', 'A', 'T', 'T', 'C', 'A', 'T', 'T', 'T', 'C'] 
        self.assertAlmostEqual(get_p_distance(seq1, seq2), 0.4, places=5)  

    def test_get_p_distance_matrix(self): 
        dna_sequences = [ 
            ['T', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'A'] 
            ['G', 'A', 'T', 'T', 'C', 'A', 'T', 'T', 'T', 'C'] 
            ['T', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'T'] 
            ['G', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'A'] 
        ]  
        expected_matrix =[ 
            [0.0, 0.4, 0.1, 0.1] 
            [0.4, 0.0, 0.4, 0.3] 
            [0.1, 0.4, 0.0, 0.2] 
            [0.1, 0.3, 0.2, 0.0]
        ] 
        self.assertEqual(get_p_distance_matrix(dna_sequences), expected_matrix) 

