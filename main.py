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
print(len(message))
print(name == "Artak")
print(isArtakAdult != False)
print(age > 18)
print("mess" in message)

comment = """
Hey you
Out there in the cold
Getting lonely, getting old
Can you feel me?
"""

print(comment)

email = """
Hello {}, how are you doing?
Here's the receipt for your order:
1234-5678-9010-0100
"""

print(email.format(name))

receipt = '1234-5678-9010-0100'

email_email = f"""
Hello {name}, how are you doing?
Here's the receipt for your order:
{receipt}
"""

print(email_email)
