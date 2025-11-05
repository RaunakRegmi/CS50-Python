symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|', ';',
           ':', "'", '"', ',', '<', '.', '>', '/', '?', '`', '~', ' ']


# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if s[0] not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' or s[1] not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        return False

    for letters in s:

        if letters in symbols:
            return False

    number_found = False

    for digit in s:

        if digit.isnumeric():

            if not number_found:

                if digit == '0':
                    return False

            number_found = True
        else:

            if number_found:
                return False

    return True


main()




