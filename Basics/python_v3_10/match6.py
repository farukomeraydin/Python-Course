while True:
    cmd = input('CSD>').split()
    if cmd == '':
        continue
    match cmd:
        case 'copy', source_path, dest_path:
            print(f'copy {source_path} {dest_path} executes')
        case 'rename', source_path, dest_path:
            print(f'rename {source_path} {dest_path} executes')
        case (['del', path] | ['erase', path] | ['remove', path]) as del_cmd:
            print(f'{del_cmd[0]} {path} executes')
        case ['quit'] | ['exit']:
            break
        case _:
            print(f'invalid command: {cmd[0]}')
