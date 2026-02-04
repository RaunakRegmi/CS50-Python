def main():

    history = []

    while True:

        action  = input('Action:')

        if action == "undo":

            undone = history.pop()
            print(f'Undone: {undone}')

        elif action == "clear":
            history.clear()

        else:
            history.append(action)

        print(history)

main()
