import random

easy_words = ('cat', 'dog', 'burger', 'house', 'cloud', 'python')
hard_words = ('brobdingnagian', 'sesquipadelian', 'acquiesce', 'smidgen', 'obfuscate')


def Play(words):
    if words == 'e':
        word = ([*easy_words[random.randint(0, 5)]])
    elif words == 'h':
        word = ([*hard_words[random.randint(0, 4)]])
    guesses = 6
    blanks = []
    for _ in range(len(word)):
            blanks += '_'

    while guesses > 0:
        
        print(f"The word is {blanks}.")
        guessed_letter = input('Guess a letter a-z ').lower()
        

        if word.count(guessed_letter) == 0:
            print("WRONG")
            guesses -= 1
            print(f"Guesses Remaining: {guesses}.")
        else:
            print("Correct!")
            letter_position = word.index(guessed_letter)
            blanks[letter_position] = word[letter_position]
            print(blanks)

        if blanks.count('_') == 0:
            print('You Win!')
            break

    if guesses == 0:
        print(f"The Word Was {word}.")

    if input("Would you like to play again? \n'Y' for 'Yes'\n'N' for 'No':\n").lower() == "y":
        Play()
        


easy_or_hard = input("Would you like easy or hard difficulty?\n'E' for Easy\n'H' for Hard\n").lower()
if easy_or_hard == 'e':
    Play('e')
elif easy_or_hard == 'h':
    Play('h')










# while guesses < 6:

#     print(f'The word is ')
#     input("Guess a letter: ")



