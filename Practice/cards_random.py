import random

cards = ['jack', 'joker', 'king', 'queen']

def main():
    # print(random.choice(cards))

    # print(random.sample(cards, k=3))

    # print(random.choices(cards, weights=[40, 40, 10, 10], k=4)) # priority to jack and joker more cause of 40 weight.

    random.seed(40) # always bring king and queen while re-run

    print(random.sample(cards, k = 4))
main()
