from json import loads, dumps
with open("Info.txt", "r") as file:
    dct = loads(file.read())
lst = ["gun", "frisbee", "holder"]
print("May be this criminals is him: ")
for name in dct:
    for crime in dct[name]:
        for el in lst:
            if el in crime["Description"]:
                print(dumps(crime, indent=4))
