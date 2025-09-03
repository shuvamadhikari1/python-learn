

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

def sum_of_digits():
    num=int(input("Enter a number: "))
    sum=0