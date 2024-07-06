# 
from strings import get_hamming_distance, get_dna_complement 

def print_menu(): 
    while True: 
        try: 
            choice = int(input("Enter your choice (1/2/3): ")) 
            if choice in [1, 2, 3]: 
                return choice 
            else: 
                print("Invalid choice. Please enter 1, 2, or 3.") 
        except ValueError: 
            print("Invalid input. Please enter a number.") 
             


def main(): 
    while True: 
        print_menu() 
        choice == get_user_choice() 

        if choice == 1: 
            dna1 = input("Enter the first DNA sequence: ") 
            dna2 = input("Enter the second DNA sequence: ") 
            try: 
                distance = get_hamming_distance(dna1, dna2) 
                print (f"Hamming Distance between {dna1} and {dna2} is: {distance}")  
            except ValueError as e: 
                print(f"Error: {e}") 

        
        elif choice == 2: 
            dna = input("Enter a DNA sequence: ") 
            complement = get_dna_complement(dna) 
            print(f"DNA complemnt of {dna} is: {complement}") 

        elif choice == 3: 
            print("Exiting program...") 
            break 

            