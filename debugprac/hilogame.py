import random
from art import logo #, vs
from art import vs
from data import data_all
import os
#確認一下是否可成功印出

# print(data_all)
def account(x):
    name  = x['name']
    descr = x['description']
    count = x['country']
    return f"{name} is {descr} live in {count}"

def check(user_AB, a_number, b_number):
    if a_number > b_number:   #short writing
        #return user_AB == "a"  #此時 return user_AB == "a" 就等於是True了
        if user_AB == "a":
            return True
        else:
            return False
    else:
        #return user_AB == "b"  #此時return後就等於是True了
        if user_AB == "b":
            return True
        else:
            return False

print(logo)
score  = 0
continue_game = True
person_b = random.choice(data_all)
while continue_game:
    person_a = person_b
    person_b = random.choice(data_all)
    #如果重複就要讓他再選一次
    if person_a == person_b:
        person_b = random.choice(data_all)
    print(f"Compare A:{account(person_a)}")
    print(vs)
    print(f"Against B:{account(person_b)}")

    #ask for guess
    user_AB  = input("Which one is higher? type 'A' or 'B': ").lower()
    a_number = person_a['number']
    b_number = person_b['number']
    correct  = check(user_AB, a_number, b_number)
    os.system('clear')
    # feedback
    if correct:
        score += 1
        print(f"YOU GET IT, now you have score:{score}")
    else:
        continue_game = False
        print(f"SORRY YOU LOSE, final score:{score}")







# print(Compare_A)
# print(Agister_B)


# def Compare_box(A, B):
#     
#     game = False
#     while not game:
#         if A > B and User_AB == "a":
#             return "Correct"
#         elif A < B and User_AB == "b":
#             B = A
#             return "Correct"
#         elif A > B and User_AB == "b":
#             game = True
#         else:
#             game = True


# Compare_box(Compare_A, Agister_B)

# n = Compare_box(Compare_A, Agister_B)
# print(n)
