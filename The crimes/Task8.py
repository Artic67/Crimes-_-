from json import loads, dumps
with open("Info.txt", "r") as file:
    dct = loads(file.read())
crime_count = 0
ar = ""
nd = 100
pr = 0
neu = {}
for name in dct:
    if name != "-":
        ar_co = 0
        for crime in dct[name]:
            crime_count += 1
            ar = crime["Arrest"]
            if ar == "True":
                ar_co += 1
        pr = nd * (ar_co/crime_count)
        crime_count = 0
        if name not in neu:
            neu[name] = 0
        neu[name] = pr
print(dumps(neu, indent=4))