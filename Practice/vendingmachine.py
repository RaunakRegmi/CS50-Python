def main():

    money_owe = 50


    while money_owe > 0:

        print(f'Amount Due: {money_owe}')

        paid = int(input('Insert coin: '))

        if paid == 25:
            money_owe -= 25
            print(f'Amount Due: {money_owe}')

        elif paid == 10:
            money_owe -= 10

            print(f'Amount Due: {money_owe}')


        elif paid == 5:
            money_owe -= 5

            print(f'Amount Due: {money_owe}')

        else:

            continue


    print(f'Change Owed: {abs(money_owe)}')

    # if money_owe < 0:

    #     print(f'Change Owed: {abs(money_owe)}')

    # else:

    #     print('Paid successfully')

main()
