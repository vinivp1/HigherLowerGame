from style import logo
from game_data import data
import random

def choose_A(data):
    person_A = random.choice(data)
    name_A = person_A.get('name')
    followers_A = person_A.get('follower_count')
    description_A = person_A.get('description')
    country_A = person_A.get('country')
    return name_A, followers_A, description_A, country_A

def choose_B(data):
    person_B = random.choice(data)
    name_B = person_B.get('name')
    followers_B = person_B.get('follower_count')
    description_B = person_B.get('description')
    country_B = person_B.get('country')
    return name_B, followers_B, description_B, country_B


person_A = choose_A(data)
person_B = choose_B(data)

# print(person_A) #teste
# print(person_B, "\n") #teste

def game(person_A, person_B):
    print(f"Compare A: {person_A[0]}, a {person_A[2]}, from {person_A[3]}.")
    print("\n                    VS                   \n")
    print(f"Compare A: {person_B[0]}, a {person_B[2]}, from {person_B[3]}.")

game(person_A, person_B)

answer = input(print("Who has more followers? Type 'A' or 'B': "))

score = 0

if answer == 'A':
    if person_A[1] > person_B[1]:
        score += 1
        person_A = person_B
        choose_B()
    else:
        print(f"Sorry, that's wrong. Final score: {score}")

