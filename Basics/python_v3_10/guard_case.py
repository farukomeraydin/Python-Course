a = int(input('Bir sayı giriniz:'))
x = -100
match a:
    case 10 if x > 0:
        print('Ok')
    case _:
        print('cannot match...')
