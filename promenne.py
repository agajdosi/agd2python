### INTRO ###
# Promenne se pouzivaji k ukladani docasnych dat v prubehu programu

# promennou vytvorime tak, ze zapiseme jeji jmeno a rovnitkem ji priradime hodnotu
mujVek = 25

# rovnitko zde nefunguje jako bezne rovnitko v matematice, v niz rika, ze se levo a pravo rovnaji
# ale namisto toho v programovani rika, ze se hodnota vpravo ulozi do hodnoty vlevo
mujVek = 1 + 3*2 + 20 - 12/2

# hodnotu ulozenou v promenne muzeme zkontrolovat treba pouzitim funkce print
print(mujVek)

# pres print muzeme zkontrolovat i vic hodnot
print("muj vek je:", mujVek, "a to je vic nez", 10)

# hodnotu promenne muzeme zmenit
mujVek = 27

# muzeme dokonce menit "datovy typ" promenne - tj. jestli je v ni ulozene
# cele cislo, desetinne cislo, boolean (true/false), textovy retezec ci jine.
mujVek = "dvacettri"    # retezec aka STRING - jsou vzdy v uvozovkach
mujVek = 23.0       # desetinne cislo aka FLOAT
mujVek = "23"       # opet retezec, jelikoz je 23 v uvozovkach
mujVek = True       # logicky vyraz aka BOOLEAN - ma jen dve mozne hodnoty: bud True, nebo False

# promenne se nedaji prejmenovat, staci jednoduse vytvorit novou promennou s novym nazvem
mamRoku = 29

# promenne se nedaji ani smazat, Python se jich zbavuje sam, kdyz nejsou potreba
# pokud mujVek uz nepotrebujeme, jednoduse na ni zapomenme
masRoku = 31

### operace s INTEGER a FLOAT ###
# s celymi a desetinnymi cisly muzeme provadet vetsinu ocekavanych pocetnich operaci
a = 8
b = 2

soucet = a + b
rozdil = a - b
soucin = a * b
podil  = a / b
zbytekpodeleni = a % 3

print("\n operace s INTEGER")
print("soucet", a + b)
print("rozdil", a - b)
print("soucin", a * b)
print("podil",  a / b)
print("zbytekpodeleni", a % b)

# stejne operace lze provadet s desetinnymi cisly FLOAT
a = 8.0
b = 2.0

soucet = a + b
rozdil = a - b
soucin = a * b
podil  = a / b
zbytekpodeleni = a % 3

print("\n operace s FLOAT")
print("soucet", a + b)
print("rozdil", a - b)
print("soucin", a * b)
print("podil",  a / b)
print("zbytekpodeleni", a % b)

# muzeme dokonce kombinovat operace s INTEGER a FLOAT cisly, python si s tim poradi
# vysledek pak ale bude vzdy FLOAT
a = 8
b = 2.0

soucet = a + b
rozdil = a - b
soucin = a * b
podil  = a / b
zbytekpodeleni = a % 3

print("\n operace s kombinaci INTEGER a FLOAT")
print("soucet", a + b)
print("rozdil", a - b)
print("soucin", a * b)
print("podil",  a / b)
print("zbytekpodeleni", a % b)


### BOOLEAN ###
# nevypada moc prakticky, ale hodi se pozdeji u vytvareni podminek IF
artist = True
rich = False

aSoucasne = artist and rich         # vysledek je True, pokud oboje je True
nebo = artist or rich               # vysledek je True, pokud aspon jedno je True
negace = not artist                 # not True je False, not False je True

print("\noperace s BOOLEAN")
print("umelkyne a bohata", aSoucasne)
print("umelkyne nebo bohata", nebo)
print("not true artist = ", negace)