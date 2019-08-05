from json import loads, dumps
with open("Info.txt", "r") as file:
    dct = loads(file.read())
data = input(": ")
for name in dct:
    for crime in dct[name]:
        if crime["Year"] == int(data):
            print(dumps(crime, indent=4))