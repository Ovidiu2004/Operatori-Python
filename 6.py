n=2345
a=n%10 #unitatile lui n
print(a,"ultima cifra a lui n")
b=(n%100)// #zecile lui n
print(b,"penultima cifra a lui n")
c=(n%1000)//100 #sutele lui n
d=n//1000 #miile lui n
print(n//9,"citul impartirii la 9")
print(n%9,"restul impartirii la 9")
print(a+b+c+d,"suma cifrelor lui n")
s=1000*a+100*b+10*c+d
print(s,"restul numarului")
