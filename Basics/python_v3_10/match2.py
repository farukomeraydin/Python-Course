a = input('Bir değer giriniz:')

match a:
    case 'ankara':
        print('06')
    case 'eskişehir':
        print('26')
    case 'kocaeli':
        print('41')
    case 'adana':
        print('01')
    case 'izmir':
        print('35')
    case _:
        print('hiçbiri')
