def main():

    user = input('Input: ')

    print(is_vowel(user))



def is_vowel(user_input):

    list = []


    for letters in user_input:

        list.append(letters)

        if letters in 'aeiou' or letters in 'AEIOU':

            list.pop()

        else:

            continue


    return "".join(list)



main()
