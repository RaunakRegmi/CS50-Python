def main():

    name = input('camelCase: ')
    list = []

    for letters in name:

        if letters.isupper():
            list.append('_')
            list.append(letters.lower())

        else:

            list.append(letters)

    print("".join(list))

main()
