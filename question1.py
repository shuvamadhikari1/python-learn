

# ###WAP to create a random number guessing game where the user has to guess a randomly generated number between 1 and 100. The program should provide feedback on whether the guess is too high, too low, or correct. The game continues until the user guesses the correct number.
# import random

# def random_number_game():
#     random_number = random.randint(1, 100)

#     count = 0

#     while True:
#         guess = int(input("Enter your guess (between 1 and 100): "))
#         count += 1
#         if guess == random_number:
#             print(f"🎉 Congratulations! You've guessed the number {random_number} in {count} attempts.")
#             break
#         elif guess < random_number:
#             print("Too low! Try again.")    
#         else:
#             print("Too high! Try again.")

# random_number_game()



#Even or Odd Checker
#Ask the user for a number and print whether it’s even or odd.


# def even_odd_checker():
#     num=int(input("Enter a number: "))
#     if num%2==0:
#         print(f"{num} is an Even number")
#     else:
#         print(f"{num} is an Odd number")
# even_odd_checker()



# Sum of Digits
# Input a number and print the sum of all its digits (e.g., 123 → 6).

# def sum_of_digits():
#     num=int(input("Enter a number: "))
#     total=0
#     for i in str(num):
#         total= total + int(i)
#     print(f"The sum of digits in {num} is {total}")
# sum_of_digits()



##Multiplication Table Generator
# ##Ask the user for a number and print its multiplication table (1 to 10)
# def multiplication_table():
#     num = int(input("Enter a number: ")) 

#     for i in range(1, 11):              
#         print(f"{num} x {i} = {num * i}")


# multiplication_table()


#Rock, Paper, Scissors
#Play against the computer using random.choice().

import random
def rock_paper_scissors():
    choices=["rock","paper","scissors"]
    computer_choice=random.choice(choices)
    user_choice=input("Enter your choice (rock, paper, scissors): ").lower()
    print(f"Computer chose: {computer_choice}")
    if user_choice==computer_choice:
        print("It's a tie!")
    elif (user_choice=="rock" and computer_choice=="scissors") or (user_choice=="paper" and computer_choice=="rock") or (user_choice=="scissors" and computer_choice=="paper"):
        print("You win!")
    elif user_choice in choices:
        print("Computer wins!") 
    else:
        print("Invalid input! Please choose rock, paper, or scissors.") 
rock_paper_scissors()
