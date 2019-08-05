from json import loads, dumps
with open("Info.txt", "r") as file:
    dct = loads(file.read())
min_year = 1000000000
co = 0
types = {}
col = 0
type1 = ""
for name in dct:
    for crime in dct[name]:
        if crime["Year"] < min_year:
            min_year = crime["Year"]
min_year = min_year//10
min_year *= 10
for i in range(3):
    for name in dct:
        for crime in dct[name]:
            if crime["Year"] > min_year and crime["Year"] < (min_year + 10):
                if crime["Type"] not in types:
                    types[crime["Type"]] = 1
                else:
                    types[crime["Type"]] += 1
                co += 1
    print("================\n   ",i+1,"decade")
    for el in types:
        if types[el] > col:
            col = types[el]
            type1 = el
    print(co, ",", type1)
    col = 0
    min_year += 10
    co = 0
    type1 = ""
    types = {}