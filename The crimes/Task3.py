from json import loads, dumps
with open("Info.txt", "r") as file:
    dct = loads(file.read())
with open("types.txt", "r") as file:
    types_list = file.read().split(",")
for name in dct:
    for crime in dct[name]:
        for i in range(len(types_list)):
            if crime["Type"] == types_list[i]:
                if name != "-":
                    print(types_list[i], ":", name)