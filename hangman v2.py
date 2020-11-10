# create a hangman function
# create a board which len should be same as the desired word

def hangman(word):
    wrong = 0
    stages = ["",
              "________        ",
              "|               ",
              "|        |      ",
              "|        0      ",
              "|       /|\     ",
              "|       / \     ",
              "|               "
              ]
    desired_word = list(word)
    board = ["__"] * len(word)
    win = False
    print(" ###################  Welcome to Hangman  ##################")
    print("\n")
    while wrong < len(stages) - 1:
        charecter = input("Gues a cahrecter ")
        if charecter in desired_word:
            charecter_index = desired_word.index(charecter)
            board[charecter_index] = charecter
            desired_word[charecter_index] = "$"

        else:
            wrong += 1
        increament = wrong + 1
        print(" ".join(board))
        print("\n".join(stages[0:increament]))
        if "__" not in board:
            print("YOU WIN !!")
            win = True
            break
    if not win:
        print(f'you lose the answer is {word}')


hangman("cat")
