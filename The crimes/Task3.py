from json import loads, dumps
with open("Info.txt", "r") as file:
    dct = loads(file.read())
with open("types.txt", "r") as file:
    types_list = file.read().split(",")
names = set()
for name in dct:
    for crime in dct[name]:
        for i in range(len(types_list)):
            if crime["Type"] == types_list[i]:
                if name != "-" and name not in names:
                    print(types_list[i], ":", name)
                    names.add(name)