#  for loops can iterate over lists , strings and tuples
#  Iterables are objects that can be iterated meaning they can be traversed  individually

# " for Iterables in Iterate_over
# Iteraration"

################### ITERATING OVER A STRING ######################

strings = "hey there we are learning loops now"

for string in strings:
    print(string)

#################### ITERATING OVER LISTS ########################

list_shows = ["breaking bad", "how i met your mother", "Friends", "twelve monkeys", "Big bang theory"]

for shows in list_shows:
    print(shows.capitalize())

#################### ITERATING OVER TUPLES ########################

The_best_Shows = (
"breaking bad", "twelve monkeys", "friends", "vampire diaries", "how i met your mother", "the good place")

for series in The_best_Shows:
    print(series.upper())

##################### RANGE IN LOOPS ##############################

number = input("Enter the number of multiplication ")
number = int(number)
for i in range(1, 11):
    print(f'{number} x {i} ={i * number}')

#################### COMBINE 2 LISTS #############################

action_series = ['breaking bad', "twelve monkeys", "dragon ball super"]
comedy_series = ["friends", "how i met your mother", "big bang theory"]
Full_list = []

for action in action_series:
    action = action.upper()
    Full_list.append(action)

for comedy in comedy_series:
    comedy = comedy.upper()
    Full_list.append(comedy)

print(Full_list)

###################### INDEX IN LISTS ##############################

list = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]

for show in list:
    print(f' at index {list.index(show)} is {show}')

######################### Guesing a number in list ####################

num_list = [1, 2, 3]
while True:

    guess = input("Guess any number or press q to quit")
    if guess == "q":
        break
    try:
        guess = int(guess)
    except ValueError:
        print("press a number or q")

    if guess in num_list:
        print("correct")
    elif guess not in num_list:
        print("incorrect")
