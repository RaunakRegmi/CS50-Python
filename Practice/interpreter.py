def main():

    calculation = input('Enter the calculation you want to perform ').strip()

    x, y, z = calculation.split()

    x = int(x)

    z = int(z)

    if y == '+':
        result = x + z
        result = float(result)
        answer(result)

    elif y == '-':
        result = x - z
        result = float(result)
        answer(result)

    elif y == '*':
        result = x * z
        result = float(result)
        answer(result)

    elif y == '/':
        result = x / z
        result = float(result)
        answer(result)

    else:
        print('Enter a valid calculation')


def answer(result):
    print('The answer is: ',result)

main()




