#import necessary module

import random


#player data
player_1 = 'Ophélie'
player_2 = 'Bidule'



#pick a random word and store it in word
#add a dictionary
dico = ['mouton']
word = list(random.choice(dico))


#give the number of letter by printing _
lenght = len(word)
x_word = ("_"*int(lenght))

print("Le mot à deviner est :" + " ".join(x_word))
print()


#store it in hidden_word
hidden_word = list(x_word)


#error is an empty list, it store the wrong guess from players
error = list()



#fix the number of possible trial to find the letters
trial = 5




#program___________________________________________


#program loop until trial = 0

terminate = False

while terminate == False and trial > 0:
    #letter gived by player one
    print("\n ~~~~~~~~~~~~~~~~~~ \n ")
    letter_P1 = input('\n Proposer une lettre : ')

    if letter_P1 in word:
        copy_word = word
        copy_word = list(copy_word)

        while letter_P1 in copy_word:
            position = copy_word.index(letter_P1) #give the position of the letter
            hidden_word [position] = letter_P1 #replace the '_' by the letter at the wright place
            copy_word[position] = 0
        print("\n Le mot à deviner est : " + " ".join(hidden_word))

        if hidden_word == word:
            print('gagné')
            terminate = True

    elif letter_P1 not in word:
        error.append(letter_P1)
        error.sort()
        print("\n Le mot à deviner est : " + " ".join(hidden_word))
        print("\n Lettres déjà essayées par le J.1 : " + ", ".join(error))
        trial = int(trial) - 1

if terminate == False and trial == 0:
    print('\n Perdu !')
    terminate = True

#add a print when user loose
#add a proposition to continue playing
#add hanged man and number of trial remain
