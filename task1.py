name = input('Имя: ')
surname = input('Фамилия: ')
s = 'Hello {0} {1}! You just delved into python.'
if len(name) < 10 and len(surname) < 10:
    print(s.format(name, surname))
