# convert into m
distances = {
    'Voyager 1': 163,
    'Voyager 2': 136,
    'Pioneer 10': 80,
    'New Horizons': 58
}


def main():
    for name in distances.keys():
        convert(distances[name])

        print(f'The converted form of {name} is {convert(distances[name])} m.')


def convert(au):
    return au * 149597870700


main()




