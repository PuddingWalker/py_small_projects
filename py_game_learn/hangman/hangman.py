#########################################################################
# File Name: hangman.py
# Author: Walker
# mail:qngskk@gmail.com
# Created Time: Tue 14 Dec 2021 01:54:50 PM CST
#########################################################################
#!/usr/bin/env python3

import random

HANGMAN_PICS = [
    '''
                +---+
                |
                |
                |
                ===''', '''
                +---+
                0    |
                |
                |
                ===''', '''
                +---+
                0   |
                |   |
                |
                ===''', '''
                +---+
                0   |
                /|  |
                |
                ===''', '''
                +---+
                0   |
                /|\ |
                |
                ===''', '''
                +---+
                0   |
                /|\ |
                /   |
                ===''', '''
                +---+
                0   |
                /|\ |
                /\  |
                ==='''
]

WORDS = '''ant baboon badger bat bear beaver camel cat clam cobra cougar coyote
crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard
llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python
rabbit ram rat raver rhino salmon seal shark sheep skunk sloth snake spider
stork swan tiger toad trout turkey turtle weasel whale wolf wombat
zebra'''.split()


class Hangman():
    def __init__(self):
        print('H A N G M A N')
        self.missedLetters = []
        self.correctLetters = []
        self.secretWord = self.getRandomWord(WORDS)
        self.gameIsDone = False

    def getRandomWord(self, wordList):
        # This function returns a random string from the passwd list of strings
        return random.choice(wordList)

    def displayBoard(self):
        print(HANGMAN_PICS[len(self.missedLetters)])
        print()

        print('Missed Letters:', ''.join(self.missedLetters), sep=' ')
        blanks = ['_' for l in self.secretWord]
        for i in range(len(self.secretWord)):
            if self.secretWord[i] in self.correctLetters:
                blanks[i] = self.secretWord[i]
        print(''.join(blanks))

    def getGuess(self, alreadyGuessed):
        # Returns the letter the player entered.
        # This function makes sure the player entered a single letter and not
        # somthing else.
        while True:
            print('Guess a letter:')
            guess = input().lower()
            if len(guess) != 1 and not guess.isalpha:
                print('Please enter a single letter.')
            elif guess in alreadyGuessed:
                print('You have already guessed that letter, Choose again:')
            else:
                return guess

    def playAgain(self):
        print('Do you wanna play again?(yes or no)')
        return input().lower().startswith('y')

    def do_play(self):
        while True:
            self.displayBoard()
            # guess
            guess = self.getGuess(self.missedLetters + self.correctLetters)
            if guess in self.secretWord:
                self.correctLetters.append(guess)
                # check if the player has won
                foundAllLetters = True
                for l in self.secretWord:
                    if l not in self.correctLetters:
                        foundAllLetters = False
                        break
                if foundAllLetters:
                    print(
                        f'Yes! The sceret word is "{self.secretWord}"! You have won!'
                    )
                    self.gameIsDone = True
            else:
                self.missedLetters.append(guess)

                # Check if player has guessed too many times and lost.
                if len(self.missedLetters) == len(HANGMAN_PICS) - 1:
                    self.displayBoard()
                    print(f'''You have run out of guessed!\nAfter
                          {len(self.missedLetters)} missed guessed and
                          {len(self.correctLetters)} correct guesses, the word was
                          {self.secretWord}''')
                    self.gameIsDone = True
            if self.gameIsDone:
                if self.playAgain():
                    self.__init__()
                else:
                    break


if __name__ == '__main__':
    xbz = Hangman()
    xbz.do_play()
