# zad2
# l1 = float(input("Podaj liczbe 1: "))
# l2 = float(input("Podaj liczbe 2: "))

# znak=input("Podaj znak + - * / // % **: ")

# if   znak == "+":
#    print(l1 + l2)
# elif znak == "-":
#    print(l1-l2)
# elif znak == "*":
#    print(l1 * l2)
# elif znak == "/":
#    print(l1 / l2)
# elif znak == "//":
#    print(l1 // l2)
# elif znak == "%":
#    print(l1 % l2)
# elif znak == "**":
#    print(l1 ** l2)
# else:
#    print("Wprowadz odpowiedni znak")
# zad3


tab1 = ["1.Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie",
        "2.W jakich okolicznosciach czytasz ksiazki najczesciej?",
        "3.Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?",
        "4.Po książki w jakiej formie sięgasz najczęściej?",
        "5.Ile książek czytasz średnio w ciągu roku?",
        "6.Jak często średnio czytasz książki? ",
        "7.Po jakie gatunki książek sięgasz najczęściej?",
        ]
tab2=[

    ]

result = []
ans=0
print("Pytania kontrolne")
p1 = input("Jak masz na imie? :")

for i in range(7):
    print(tab1[i])


print(tab1[0])
print("a) oglądanie telewizji/filmów/seriali")
print("b) czytanie książek/czasopism")
input("c)  inne,jakie ?")
#if c1 == "c" or b1 == "b" or a1 == "a":
    #input()
    #result.append()

print(tab1[1])
a2 = print("a) podczas podróży")
b2 = print("b) w czasie wolnym (po pracy, na urlopie)")
c2 = input("c) inne,jakie ? Twoja odpowiedz :")
print(tab1[2])
a3 = print("a) chęć poszerzenia wiedzy")
b3 = print("b) czytanie mnie relaksuje/odpręża")
c3 = input("c) inne,jakie ? Twoja odpowiedz :")

print(tab1[3])
a4 = print("a) papierowej (tradycyjnej)")
b4 = print("b) e-booki (książki elektroniczne) na komputerze")
c4 = input("c) inne,jakie ? Twoja odpowiedz :")
print(tab1[4])
a5 = print("a) 0")
b5 = print("b) żadnej w całości - jedynie fragmenty")
c5 = input("c) inne,jakie ? Twoja odpowiedz :")
print(tab1[5])
a6 = print("a) codziennie")
b6 = print("b) raz w tygodniu")
c6 = input("c) inne,jakie ? Twoja odpowiedz :")
print(tab1[6])
a7 = print("a) kryminały/thrillery")
b7 = print("b) naukowe")
c7 = input("c) inne,jakie ? Twoja odpowiedz :")

for i in tab1:
    for x in result:
        print(tab1[i][x])
