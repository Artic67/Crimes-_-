from json import loads, dumps
with open("Info.txt", "r") as file:
    dct = loads(file.read())
with open("Ans.txt", "w") as file:
    pass
name1 = input("Name: ")
for name in dct:
    for crime in dct[name]:
        lst = []
        if name1 == name:
            for key in crime:
                lst.append(crime[key])
            with open("Ans.csv", "a") as file:
                for el in range(len(lst)):
                    lst[el] = str(lst[el])
                file.write(name1 + ";" + ";".join(lst) + "\n")