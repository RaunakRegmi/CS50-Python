def main():
    name = {'name': "Raunak's satellite"}
    name.update({'distance': 143, 'date': 1974})
    print(report(name))


def report(spacecraft):
    return f'''

    ========REPORT========

    spacecraft = {spacecraft.get('name')}
    distance = {spacecraft.get('distance')} AU
    date = {spacecraft.get('date')} AD

    ======================


    '''


main()
