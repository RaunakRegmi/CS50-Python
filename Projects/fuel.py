def main():


    while True:
        fraction = input('Enter a fraction: ')

        try:
            floating = convert(fraction)

            if floating <= 1:
                print('E')

            elif floating >= 99:
                print('F')

            else:
                print(f'{floating}%')

        except ValueError:
            pass

        except ZeroDivisionError:
            pass

        else:
            break


def convert(value):

    x, y = value.split('/')

    x = int(x)

    y = int(y)

    if x > y:
        raise ValueError


    else:

        in_float = (x / y) * 100

        floating = round(in_float)

        return floating


main()


