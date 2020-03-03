# 4. Из текстового файла удалить все слова, содержащие от трех до пяти символов, но при этом из каждой строки
# должно быть удалено только четное количество таких слов.
import io

result = open('t4result.txt', 'w')
with io.open('C:/Users/bonny/PycharmProjects/FirstPrj/advanced/HW10/t4file.txt', encoding='utf-8') as file:
    for line in file:
        counter = 0
        list_line = [str(i) for i in line.split()]
        for word in list_line:
            if 3 <= len(word) <= 5:
                counter += 1
            new_line = []
            del_counter = 0
        if counter % 2 == 1:
            counter -= 1
        for word in list_line:
            if 3 <= len(word) <= 5 and del_counter < counter:
                del_counter += 1
                continue
            new_line.append(f'{word} ')
        result.write(''.join(new_line) + '\n')
result.close()
