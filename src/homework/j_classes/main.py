# 
from class_a import die

def main():
    game_die = die()
    
    while True:
        input("Press Enter to roll the die...")
        game_die.roll()
        print(game_die)
        
        choice = input("Roll again? (y/n): ").strip().lower()
        if choice != 'y':
            break

if __name__ == "__main__":
    main()
