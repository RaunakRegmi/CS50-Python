def main():
    x = input('Greet your customer ').lower().strip()
    the_greetings(x)


def the_greetings(greetings):
    if greetings.startswith('hello'):
        print('You owe $0')
    elif greetings.startswith('h') and not(greetings.startswith('hello')) :
        print('You owe $20')

    else:
        print('You owe $100')

main()
