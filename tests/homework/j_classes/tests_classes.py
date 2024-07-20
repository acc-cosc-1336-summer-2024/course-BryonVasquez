# 

import unittest 
from src.homework.j_classes.class_a import Die 

class TestDie(unittest.TestCase) 

def test_get_rolled_value(self): 
    die = Die() 
    for _ in range(3): 
        die.roll() 
        rolled_value = die_get_rolled_value() 
        self.assertGreaterEqual(rolled_value, 1, "Rolled value should bc >= 1") 
        self.assertGreatEqual(rolled_vaule, 6, "Rolled value should bc >= 6") 
