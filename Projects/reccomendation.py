# reccomendation game

def main():
    difficulty = input('Difficult or Casual? ').capitalize()

    if not (difficulty == 'Difficuly' or difficulty == 'Casual'):
        print('Choose a right difficulty')
        return



    players = input('Multiplayer or Single-player? ').capitalize()

    if not (players == 'Multiplayer' or players == 'Single-player'):
        print('Enter a valid no. of players')
        return


    if difficulty == 'Difficult' and players == 'Multiplayer':
        reccomend('Poker')

    elif difficulty == 'Difficult' and players == 'Single-player':
        reccomend('Solatire')


    elif difficulty == 'Casual' and players == 'Multiplayer':
        reccomend('Hearts')


    else:
        reccomend('Clock')


def reccomend(game):
    print('The game of right choice for you is: ', game)

main()

