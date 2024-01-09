def banner(s, ch='-'):
    if isinstance(s, (int, float)):
        s = str(s)
    print(ch * len(s))
    print(s)
    print(ch * len(s))

banner('ankara')
banner(10)
banner(12.4)
