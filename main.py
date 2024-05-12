from style import logo
from game_data import data
import random

def choose(data):
    person = random.choice(data)
    name = person.get('name')
    followers = person.get('follower_count')
    description = person.get('description')
    country = person.get('country')
    return name, followers, description, country

def game(person_A, person_B):
    print(f"Compare A: {person_A[0]}, a {person_A[2]}, from {person_A[3]}.")
    print("\n                    VS                   \n")
    print(f"Compare B: {person_B[0]}, a {person_B[2]}, from {person_B[3]}.")

person_A = choose(data)
person_B = choose(data)
print(logo)
game(person_A, person_B)
answer = input("Who has more followers on ig? Type 'A' or 'B': ")

score = 0
should_continue = True

while should_continue:
    if answer == 'A' or answer == 'a':
        if person_A[1] > person_B[1]:
            score += 1
            person_A = person_B[:]
            person_B = choose(data)
            print(f"You're right! Current score: {score}.\n")
            game(person_A, person_B)
            answer = input("Who has more followers on ig? Type 'A' or 'B': ")
        elif person_A[1] == person_B[1]:
            print("It's a draw!")
            person_A = choose(data)
            person_B = choose(data)
            game(person_A, person_B)
            answer = input("Who has more followers on ig? Type 'A' or 'B': ")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            should_continue = False
    elif answer == 'B' or answer == 'b':
        if person_B[1] > person_A[1]:
            score += 1
            person_A = person_B[:]
            person_B = choose(data)
            print(f"You're right! Current score: {score}.\n")
            game(person_A, person_B)
            answer = input("Who has more followers on ig? Type 'A' or 'B': ")
        elif person_B[1] == person_A[1]:
            print("It's a draw!")
            person_A = choose(data)
            person_B = choose(data)
            game(person_A, person_B)
            answer = input("Who has more followers on ig? Type 'A' or 'B': ")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            should_continue = False
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        should_continue = False
