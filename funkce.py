### FUNKCE ###
# funkce nam umoznuji definovat urcity kod = funkci, ktery pak muzeme pouzivat z ruznych mist v programu
# ulehci nam tak praci, jelikoz nebudeme muset stejnou funkcionalitu kodu kopirovat na ruzna mista v programu

### ZAKLADNI FUNKCE V PYTHONU ###
# python nabizi nektere zakladni funkce
# jsou jiz nadefinovane v samotnem pythonu a tak je muzeme hned pouzivat = volat je

print("Ahoj!")

#print je zde nazev funkce, je idealni aby nazev souvisel s tim, co funkce dela
#v zavorce uvadime jednotlive parametry funkce - data, s kterymi funkce pracuje
# parametr muze byt jeden, dva nebo i vic. nekdy jsou tez funkce, ktere nemaji parametr zadny
print()
print("Cau.")
print("Jak se mas?","Skvely ne?")

#jako parametr nemusime pouzivat primo data, tady napriklad primo konkretni retezce
#ale muzeme klidne jako parametr predavat promenne

pozdrav = "Cau"
print(pozdrav)

#a muzeme klidne predavat kombinaci, je to jedno
print(pozdrav,"Je, ahoj!")


### DEFINICE vlastni FUNKCE ###
# definici funkce zaciname klicovym slovem "def",
# pote uvedeme jmeno nasi funkce
# v zavorce pak pojmenujeme jednotlive parametry

def pozdravitDvakrat(pozdrav):
        print(pozdrav)
        print(pozdrav)

# s parametrem pak ve funkci zachazime jako s promennymi
# nevime sice, jakou hodnotu budou mit (ziskaji ji az podle toho, s jakymi hodnotami je pozdeji bude nekdo volat)
# jinak se ale parametry chovaji jako bezne promenne

#kdyz jsme funkci nadefinovali, muzeme ji pouzit = "zavolat"
pozdravitDvakrat("Cau!")

#muzeme definovat funkci, ktera nepouziva zadne parametry, zavorka ale zustane, jen bude prazdna
def upozorniUzivatele():
        print("Pozor, mozna se neco stane!")

#muzeme definovat i vice parametru
def pozdravJmenem(pozdrav, jmeno):
        print(pozdrav, jmeno, "!")

### VOLANI FUNKCE Z FUNKCE ###

def pozdravDvakrat(pozdrav):
        print(pozdrav)
        print(pozdrav)

def pozdravTrikrat(pozdrav):
        pozdravDvakrat("cau!")
        print(pozdrav)

# z funkce pozdrav dvakrat muzeme volat pythonovskou funkci print
# stejne tak muzeme zavolat i vlastni funkci pozdrav dvakrat

# namisto psani obrovskych funkci nebo obrovskych programu
# je tak idealni si kod rozdelit na mensi a univerzalnejsi funkce
# snizime tak mnozstvi opakovani stejneho kodu v celem programu 


def pozdravit(pocet, osloveni):
    for _ in range(pocet):
        print("Ahoj", osloveni, "!")

pozdravit(5, "Honzo")
pozdravit(12, "Martine")
pozdravit(0, "Lubosi")


### NAVRATOVA HODNOTY FUNKCE
# nektere funkce maji neco vykonat a neni treba, aby vracely urcitou hodnotu, napriklad print
print("Cau")

#obcas se ale hodi mit funkci, ktera vraci nejakou hodnotu, napriklad funkce soucet
def soucet(a, b):
        c = a + b
        return c

# pokud chceme, aby funkce vratila nejakou hodnotu, pouzijeme klicove slovo "return"
# vysledek = navratovou hodnotu funkce pak muzeme priradit do promenne
a = 10
b = 5

vysledek = soucet(a,b)
print(vysledek)

