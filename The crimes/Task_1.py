"""
1. Необходимо сделать отчет по каждому из известнх преступников: Загрузите информацию из файла в следующую структуру:
Словарь, ключами в котором являются имена преступников, каждому из
которых соответствует список со всеми их дениями, каждое из которых является словарем

Далее с помощью модуля json выведите на экран даный словарь

(Деяния неизвестных преступников обьедените в список и поместите в свой словарь с ключом "-")

10 баллов
10 минут
"""
from json import loads,dumps
dct = {}
with open("Crimes.csv", "r") as file:
    keys = file.readline().strip("\n").split(",")
    print(keys)
    for line in file:
        lst = line.strip("\n").split(",")
        print(lst)
        if lst[5] not in dct:
            dct[lst[5]] = []
        dct[lst[5]].append({
            keys[0]: lst[0],
            keys[1]: lst[1],
            keys[2]: lst[2],
            keys[3]: lst[3],
            keys[4]: lst[4],
            keys[6]: lst[6],
            keys[7]: lst[7],
            keys[8]: lst[8]
        })
with open("Info.txt", "w") as file:
    file.write(dumps(dct))
print(dumps(dct, indent=4))