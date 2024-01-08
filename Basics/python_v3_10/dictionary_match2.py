d = {'ali': 10, 'veli': 20, 'selami': 30, 'ayşe': 40, 'fatma': 50}

match d:
    case {'ali': 10, 'veli': 20, **others}:
        print(others)
