inp = [str(i) for i in input('Имя и фамилия: ').split()]
if 0 < len(inp) < 1000:
    for i in inp:
        def cap(name):
            if type(name[0]) == str:
                return name.capitalize()
        print(cap(i), end=' ')
