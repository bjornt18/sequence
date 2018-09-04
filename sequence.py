# tekur n inn sem lengd talnarunu. talnarunan er summa seinustu 3 talna í talnarununi
n = int(input("Enter the length of the sequence: "))
n1 = 0
n2 = 1
n3 = 2
nlok = n1 + n2 + n3
for i in range(0, n):
    print(n1, n2, n3, nlok)
    n1 = n2
    n2 = n3
    n3 = nlok
    nlok = n1 + n2 + n3

