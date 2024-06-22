# 

from src.homework.d_repetition.repetition import get_factorial, sum_odd_numbers 

def main(): 
    while True: 
        print("Homework 3 Menu")
        print("1-Factorial") 
        print("2-Sum odd numbers") 
        print("3-Exit")  

    choice = input("Enter your choice (1/2/3): ")  

    if choice == '1': 
        num = int(input("Enter a number to calculate factorial (1-9): ")) 
        if 1 <= num <= 9: 
            print(f"Factorial of {num} is: {get_factorial(num)}") 
        else: 
            print("Invalid input. Please enter number between  1 and 9.") 
   
    elif choice == '2':
    num = int(input("Enter a number to calculate sum of odd numbers (1-99): ")) 
    if 1 <= num <= 99: 
        print(f"Sum of odd numbers up to {num} is: {sum_odd_numbers(num)}") 
    else: 
        print("Invalid input. Please enter number between 1 and 99.") 
    elif choice == '3': 
    exit_program = input("Do you want to exit? (yes/no): ").lower() 
    if exit_program == 'yes':
        break 
    else: 
        print("Invalid choice. Please enter 1, 2, or 3. ") 
    