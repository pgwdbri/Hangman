#Hangman Game 

def hangman(word):
    wrong = 0
    stages = ["","________        ","|               ","|        |      ","|        0      ","|       /|\     ","|       / \     ","|               "
             ]
    givenletter = list(word)
    board = ["__"] * len(word)
    win = False

    print("Welcome to Hangman")
    
    while wrong < len(stages) - 1:
        #wrong guesses are less than the stages of hangman
        print("\n")
        #prints a new line to look nice 
        msg = "Guess a letter"
        char = input(msg)
        
        if char in givenletter:
            replace = givenletter \
                   .index(char)
            board[replace] = char
            givenletter[replace] = '$'
            #for duplicate guess, if a letter occurs more than once in the given word
            
        else:
            wrong += 1
        print((" ".join(board)))
        end = wrong + 1
        print("\n"
              .join(stages[0: end]))
        
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
            
    if not win:
        print("\n"
              .join(stages[0: \
              wrong]))
        print("You lose! It was {}."
              .format(word))

hangman("cat")