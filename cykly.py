### CYKLY ###
# Cykly se pouzivaji k opakovani urciteho ukonu, abychom jej nemuseli kopirovat na nekolik radku.
# Soucasne se take hodi, pokud chceme zopakovat ukon na vsech prvcich seznamu (list), pripadne slovniku (dictionary)

### FOR ###
# cyklus for zacina klicovym slovem "for"
# po nem nasleduje jmeno promenne, pod niz se budou objevovat jednotlive objekty ze seznamu
# pote nasleduje klicove slovo "in" a nakonec seznam, pres ktery ma cyklus for prochazet
m = [0, 1, 2, 3, 4]
# muzeme cist jako: pro kazdy prvek "x" v mnozine "m" udelej: ....
# program tedy zacne u prvniho prvku 0, x se tedy bude rovnat nule a provede prikazy,
# pak bude pokracovat prvkem 1, udela prikazy a pujde dal, dokud se nedostane k poslednimu prvku 4
for x in m:
    print(x)

#muzeme  prochazet pres libovolny seznam, treba ten obsahujici retezce
#seznam obsahujici retezce se jmeny ucastniky kurzu
seznam = ["Alina", "Andreas", "Anicka", "Zdenka", "Svata", "Martin"]
# muzeme cist jako: pro kazdy prvek "clovek" v mnozine "seznam" udelej: ....
for clovek in seznam:
    print("Hi," + clovek + "!")

# pokud budeme chtit nejakou operaci vykonat v urcitem poctu opakovani, hodi se funkce range()
# range(x) generuje seznam, ktery obsahuje x cisel zvysujicich se o 1
cisla = range(10)
#cisla = [0,1,2,3,4,5,6,7,8,9]
print(cisla)
for x in cisla:
    print(x)

# funkci range() muzeme pouzit i primo v cyklu for:
for x in range(100):
    print(x)

### CONTINUE ###
# v cyklu muzeme pouzit prikaz continue, ktery preskoci k dalsimu prubehu/iteraci cykly
# vynecha tedy vsechen kod, ktery po nem nasleduje

for x in range(100):
    print("vypisuji cislo", x)
    if x < 10:
        continue #pokud je cislo mensi jak 10, pak preskoci k dalsimu cislu a druhy print se uz nevykona
    print("vypisuji podruhe, protoze je vetsi jak 10", x)

print("A jsme z cyklu venku")

### BREAK ###
# cyklus muzeme i predcasne ukoncit, k tomu slouzi prikaz break

for x in range(100):
    print(x)
    if x == 44: 
        break #pokud je x rovno 44, pak se cyklus ukonci a program pokracuje v kodu za cyklem
    print(x)

print("A jsme z cyklu venku...")
