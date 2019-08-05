from json import loads, dumps
with open("Info.txt", "r") as file:
    dct = loads(file.read())
nums = {}
day = 0
col = 0
for crime in dct["-"]:
    if crime["Day"] not in nums:
        nums[crime["Day"]] = 1
    else:
        nums[crime["Day"]] += 1
for el in nums:
    if nums[el] > col:
        day = el
        col = nums[el]
for crime in dct["-"]:
    if crime["Day"] == day:
        print(dumps(crime, indent=4))