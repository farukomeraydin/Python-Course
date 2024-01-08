while True:
    cmd = input('CSD>').strip()
    if cmd == '':
        continue
    match cmd:
        case 'copy':
            print('copy executes')
        case 'rename':
            print('rename executes')
        case 'del' | 'erase' | 'remove':
            print('delete executes')
        case 'quit' | 'exit':
            break
        case _:
            print(f'invalid command: {cmd}')
