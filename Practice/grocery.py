def main():
    my_list = []

    count = 0

    while True:

        try:
            items = input('Enter a grocery item: ').lower() #apple banana apple

            my_list.append(items)  # apple banana apple

        except EOFError:
            break

    my_list.sort()

    i = 0
    while i < len(my_list):

        item = my_list[i]
        count = my_list.count(item)
        print(count, item.upper())
        i += count


main()



