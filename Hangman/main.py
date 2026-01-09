# Hangman Game in Python

import random
from collections import Counter

someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split(' ')
word = random.choice(someWords)

if __name__ == '__main__':
    print('Guess the word! HINT: word is a name of a fruit')

    for i in word:
        print('_', end=' ')
    print()

    letterGuessed = ''
    chances = len(word) + 2
    flag = 0

    try:
        while chances > 0 and flag == 0:
            print("\nChances left:", chances)
            chances -= 1

            guess = input('Enter a letter to guess: ').lower()

            if not guess.isalpha():
                print('Enter only a LETTER')
                continue
            elif len(guess) != 1:
                print('Enter only a SINGLE letter')
                continue
            elif guess in letterGuessed:
                print('You already guessed that letter')
                continue

            if guess in word:
                for _ in range(word.count(guess)):
                    letterGuessed += guess

            for char in word:
                if char in letterGuessed:
                    print(char, end=' ')
                else:
                    print('_', end=' ')

            if Counter(letterGuessed) == Counter(word):
                print("\n\nThe word is:", word)
                print("Congratulations! You won 🎉")
                flag = 1

        if chances == 0 and flag == 0:
            print("\nYou lost! The word was:", word)

    except KeyboardInterrupt:
        print("\nGame interrupted. Bye!")