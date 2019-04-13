### PODMINKY ###
# Podminky nam umoznuji vetvit beh programu - reagovat na ruzne situace ruznymi vysledky.

### IF ###
#podminku IF zaciname klicovym slovem "if"
#po nem nasleduje samotna podminka: jakykoliv vyraz, ktery nabyva hodnot True nebo False
#napriklad vek>17
vek = 27
if vek > 17:       
    print("Muzem ti nalejt!") #tato cast kodu se vykonna jen kdyz je splnena podminka
    print("") #vykonna se vsechen kod odsazeny tabulatorem
print("") #neodsazeny kod se vykona tak ci tak - jiz neni soucasti podminky

#logicky vyraz v podmince muzeme nahradit primo logickou hodnotou
# napriklad misto podminky umistit rovnou promennou obsahujici True nebo False
# defacto si tak muzeme podminku pripravit predem a dal operovat jen s True/False

#do promenne dospely se ulozi hodnota vpravo, tou je False, jelikoz
#vyraz vek>17 se vyhodnoti jako nepravdivy: 16 neni vetsi nez 17
vek = 16
dospely = vek > 17
if dospely:         #IF pote zapiseme primo s promennou "dospely"
    print("Muzem ti nalejt!")

# obcas se hodi reagovat i na situaci, kdy podminka neni splnena
# k tomu muzeme pouzit dve podminky IF za sebou:

vek = 20
if vek > 17:       
    print("Muzem ti nalejt!")
if vek < 18:       
    print("Sorry jako!")


### IF-ELSE ###
#namisto k zachyceni obou vysledku podminek pomoci dvou IFu, ale muzeme pouzit i konstrukci IF-ELSE

if vek > 17:
    print("Muzem ti nalejt!")
else:
    print("Sorry jako.")

#vyhodou je, ze mame jistotu, ze se bude provede jedno nebo druhe, nemuzeme se splest a vynechat nejakou moznost

### IF-ELIF-ELSE
# pokud chceme reagovat na vice nez 2 situace, muzeme pouzit konstrukci IF-ELIF-ELSE
# pokud IF bude pravdive, vykonna se kod tohoto IFu a dalsi ELIF i ELSE se preskoci
# pokud IF nebude pravda, program bude pokracovat na dalsi ELIF
# pokud ELIF bude pravdivy, vykona se kod v tomto ELIFu a dalsi ELIF i ELSE se preskoci
# pokud nebude ELIF pravdivy, pak program pujde k dalsimu ELIFu
# pokud zadny z ELIFu nebude pravdivy, program dojde k ELSE a vykonna ELSE

# vzdy se vykonna kod pouze v jednom z IF-ELIF-ELSE 

vek = input()
vek = int(vek)

if vek > 17:
    print("Muzem ti nalejt!")
elif vek > 16:
    print("Vino by slo.")
elif vek > 14:
    print("Jen pivko...")
else:
    print("Sorry jako.")

# ELSE muzeme vynechat, coz se hodi pokud nebudeme chtit reagovat na situaci, kdy se zadny IF nebo ELIF nevykonna
