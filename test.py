# To bedzie plik na którym będziemy pracowali na zajęciach z repo
def  hello(name):
	return "Hello" + str(name)

def odejmij(a,b):
	wynik = float(a)-float(b)
	return a-b

def dodaj(a,b):
	wynik = float(a) + float(b)
	return wynik

pierwsza = int(input())
druga = int(input())

print (dodaj(pierwsza, druga))


