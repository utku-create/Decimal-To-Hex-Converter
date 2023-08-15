sayi = int(input("Enter your num, pls:"))
bolum = sayi // 16
kalan = sayi % 16
onAltilik = str(kalan)
hex = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
while(bolum != 0):
    process = bolum
    bolum = process // 16
    kalan = process % 16
    if (kalan > 9):
        for i in hex:
            if(kalan in hex):
                kalan = hex[kalan]
    onAltilik = onAltilik + str(kalan)
print(onAltilik[::-1])

# -_-
