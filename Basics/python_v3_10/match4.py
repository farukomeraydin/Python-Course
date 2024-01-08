while True:
    cmd = input('CSD>').strip()
    if cmd == '':
        continue
    match cmd:
        case 'copy':
            print('copy executes')
        case 'rename':
            print('rename executes')
        case ('del' | 'erase' | 'remove') as del_cmd:
            print(f'{del_cmd} executes')
        case 'quit' | 'exit':
            break
        case _:
            print(f'invalid command: {cmd}')
