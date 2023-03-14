#zad3


tab1 = ["1.Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie",
        "2.W jakich okolicznosciach czytasz ksiazki najczesciej?",
        "3.Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?",
        "4.Po książki w jakiej formie sięgasz najczęściej?",
        "5.Ile książek czytasz średnio w ciągu roku?",
        "6.Jak często średnio czytasz książki? ",
        "7.Po jakie gatunki książek sięgasz najczęściej?",
        ]
tab2 = [
    "a) oglądanie telewizji/filmów/seriali",
    "b) czytanie książek/czasopism",
    "c)  inne,jakie ?",

    "a) podczas podróży",
    "b) w czasie wolnym (po pracy, na urlopie)",
    "c) inne,jakie ? Twoja odpowiedz :",
    "a) chęć poszerzenia wiedzy",
    "b) czytanie mnie relaksuje/odpręża",
    "c) inne,jakie ? Twoja odpowiedz :",
    "a) papierowej (tradycyjnej)",
    "b) e-booki (książki elektroniczne) na komputerze",
    "c) inne,jakie ? Twoja odpowiedz :",
    "a) 0",
    "b) żadnej w całości - jedynie fragmenty",
    "c) inne,jakie ? Twoja odpowiedz :",
    "a) codziennie",
    "b) raz w tygodniu",
    "c) inne,jakie ? Twoja odpowiedz :",
    "a) kryminały/thrillery",
    "b) naukowe",
    "c) inne,jakie ? Twoja odpowiedz :"
]

result = []

print("Pytania kontrolne")
name = input("Jak masz na imie? :")

for i in range(len(tab1)):
    print(tab1[i])
    for j in range(3):
        print(tab2[i*3+j])
    answer = input("Udziel odpowiedzi calym zdaniem: ")
    result.append(answer)

print(name)

for i in range(0,len(tab1)):
    print(tab1[i])
    print(result[i])

