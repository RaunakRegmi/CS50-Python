months = [ "January", "February", "March", "April", "May", "June", "July",
           "August", "September", "October", "November", "December" ] ## month between 1-12, day between 1-31

# print in YYYY-MM-DD

def main():

    date = input('Enter a date: ').replace(',', " ")# MM/DD/YYYY

    if '/' in date:
        m, d, y = date.split('/')
        month = int(m)
        d = int(d)
        y = int(y)

    else:
        m, d, y = date.split()
        d = int(d)
        y = int(y)
        month = months.index(m) + 1

    if 1 <= month <= 12 and 1 <= d <= 31:

        print(f'{y}-{month:02d}-{d}')

main()