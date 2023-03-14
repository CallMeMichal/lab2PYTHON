# zad1
# 1
a = b = c = "Python 2023"

if a == b and b == c:
    print("true")
else:
    print("false")
# 2

print(type(id(a)), hex(id(a)))
print(type(id(b)), hex(id(b)))
print(type(id(c)), hex(id(c)))
# 3


c = "Java 11"

if a == b and b == c:
    print("true")
else:
    print("false")

print(type(id(a)), hex(id(a)))
print(type(id(b)), hex(id(b)))
print(type(id(c)), hex(id(c)))
