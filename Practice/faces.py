text = input('enter a sad or happy sentence: ')

def main():
    convert(text)


def convert(phrase):
    global happy
    global sad

    happy = '🙂'
    sad = '🙁'

    print(phrase.replace(':)', happy).replace(':(', sad))

main()
