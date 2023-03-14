#zad2
l1 = float(input("Podaj liczbe 1: "))
l2 = float(input("Podaj liczbe 2: "))

znak=input("Podaj znak + - * / // % **: ")

if   znak == "+":
   print(l1 + l2)
elif znak == "-":
   print(l1-l2)
elif znak == "*":
   print(l1 * l2)
elif znak == "/":
   print(l1 / l2)
elif znak == "//":
   print(l1 // l2)
elif znak == "%":
   print(l1 % l2)
elif znak == "**":
   print(l1 ** l2)
else:
   print("Wprowadz odpowiedni znak")