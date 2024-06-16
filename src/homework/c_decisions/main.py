# 
import decisions 

def main(): 
    options = float(input("Enter the number of options: ")) 
    total = float(input("Enter the total: ")) 
    
    ratio = decisions.get_options_ratio(options, total) 

    rating = decisions.get_faculty_rating(ratio) 

    print(f"Ratio: {ratio}") 
    print(f"Faculty Rating: {rating}") 