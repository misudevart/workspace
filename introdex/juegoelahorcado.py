import random           
import os

def run():

    images = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

    DB = [
        'c',
        'python',
        'javascript',
        'php',
        'java',
    ]


    word = random.choice(DB)
    spaces = ["_"] * len(word)
    attemps = 0

    while True:
        os.system("clear")
        for character in spaces:
            print(character, end=" ")
        print(images[attemps])
        letter = input('elige una letra')


        found = False

        for idx, character in enumerate(word):
            if character == letter:
                spaces[idx] = letter
                found = True


        if not found:
            attemps +=  1

        if "_" not in spaces:
            os.system("clear")
            print("ganaste")
            break
            input()    

        if attemps == 6:
            os.system('clear')
            print("perdiste")
            break
            input()



if __name__ == '__main__':
    run()

