while True:
    print('CSD>', end='')
    cmd = input().strip()
    if cmd == '':
        continue
    if cmd == 'quit':
        break
    if cmd == 'copy':
        print('copy command executes...')
    elif cmd == 'rename':
        print('rename command executes...')
    elif cmd == 'dir':
        print('dir command executes...')
    else:
        print('invalid command!')
