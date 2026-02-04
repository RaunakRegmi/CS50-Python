WORDS = {'CHAIR': 5, 'HAIR': 4, 'PAIR': 4, 'GRAPHIC':7}


def main():

    print('Welcome to spelling bee!!')

    choice = input('Press y to continue, n to end the game: ').lower()

    continue_game(choice)


def continue_game(decision):

    if decision == 'y':

        print('WELCOME TO SPELLING BEE')

        print('YOUR LETTERS ARE: A I P C H R G')


        while len(WORDS) > 0:

            guess = input('Guess the word: ')

            if guess == "GRAPHIC":

                print('You guessed the main word')
                print(f'You scored {WORDS[guess]} points.')

                WORDS.clear()


            elif guess in WORDS.keys():


                print(f'You have scored {WORDS[guess]} points.')

                WORDS.pop(guess)

        print('You have guessed all the words!!')


    elif decision == 'n':
        print('The game ends here')


    else:
        print('Invalid choice!')

main()
