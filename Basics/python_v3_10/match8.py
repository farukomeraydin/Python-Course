a = [10, 20, 30, 40, 50]
match a:
    case 10, 20, *others:
        print(others)
