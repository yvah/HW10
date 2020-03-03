# -*- coding: utf-8 -*-

ph_numbers = open('phonenumbers.txt', 'r')
result = open('task2_result.txt', 'w')
for line in ph_numbers:
    line = line.strip()
    person = [str(i) for i in line.split()]
    if person[1][0] == 'C' or person[1][0] == 'K':
        result.write(line)
        print(line)
ph_numbers.close()
result.close()
