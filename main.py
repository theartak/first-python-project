name, age = "Artak", 25
# name = "Artak"
# age: int = 25
PI = 3.14
numbers = [1, 2, 3, 4]
isArtakAdult = True
message = 'This message is sponsored by Raid: Shadow Legends'

"""
Multiline comment
inside main.py
(c) Fjord[フィヨルド]
"""

print(name)
print(age)
print(PI)
print(numbers)
print(isArtakAdult)

print(type(name))
print(type(age))
print(type(PI))
print(type(numbers))
print(type(isArtakAdult))


def hello() -> str:
    return "hello"


def returnall():
    return name, age, isArtakAdult


print(hello())
print(returnall())
print(message.upper())