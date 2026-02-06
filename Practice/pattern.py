def main():
    print_brick(4)


def print_brick(size):

    for i in range(size, 0, -1):

        for j in range(i):
            print('#', end = '')

        print()


main()
