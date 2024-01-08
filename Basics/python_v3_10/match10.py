a = [10, 20, 30, 40, 50]
match a:
    case 10, *others, 40:
        print(others)
