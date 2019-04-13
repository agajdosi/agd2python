### Program: pocitani vyskytu slov v textu

# otevreme soubor text.txt, do ktereho jsme predem manualne ulozili anglicky text
# pouzijeme funkci open(), jako prvni parametr pouzijeme nazev souboru k otevreni (pripadne muzeme pouzit i cestu k nemu, treba: "texty/lekce4/text.txt")
# druhy parametr "r" rika, ze otevirame ke cteni (pozdeji v kodu tak nemuzeme do souboru zapisovat)
# funkce open() vraci otevreny soubor, ulozime jej do promenne file at s nim muzeme dale pracovat
file = open("text.txt", "r")

# otevreny soubor (typ FileIOWrapper) obsahuje funkci read, ktera precte z tohoto otevreneho souboru text
# vraceny text priradime do promenne "text"
text = file.read()

# text je textovy retezec, takze muzeme pouzit pripravene metody textovych retezcu, napriklad capitalize()
# prevede text na velka pismena
text = text.capitalize()

# pouzijeme metodu split() k rozdeleni textoveho retezce na seznam retezcu, budeme delit u znaku mezery: " "
# defacto rozdelime retezec podle prazdnych mezer na seznam obsahujici jednotliva slova
slova = text.split(" ")

### SLOVNIKY ###
#slovnik je podobny seznamu, jen se pise s {} a obsahuje pro kazdy prvek dva zaznamy: klic a hodnotu (key and value), oddelene :
slovnik = {"auto": "car", "pes": "dog"}
# slovnik take neni serazeny, takze k jednotlivym hodnotam nepristupujeme podle indexu - poradi prvku, ale podle jmena prave klice
print(slovnik["auto"])
print(slovnik["pes"])
#do slovniku muzeme pridat novy zaznam, pridame klic "les" s hodnotou "forest"
slovnik["les"] = "forest"
### konec o slovnicich ###

# vytvorime prazdny slovnik, do ktereho pozdeji budeme ukladat slova a kolikrat se vyskytly, klic bude slovo a hodnoty bude jeho vyskyt 
slovnik = {}

#udelame cyklus, ktery projde pres vsechna slova
for slovo in slova:
    # pokud slovo uz je jako klic ve slovniku, pak..
    if slovo in slovnik:
        slovnik[slovo] = slovnik[slovo] + 1 #vezmeme hodnotu ulozenou pod danym klicem slovo, zvetsime ji o 1 a ulozime tuto novou hodnotu zpet pod klic slovo
    else: # pokud slovo neni ve slovniku, pak..
        slovnik[slovo] = 1 # slovo pridame jako klic s hodnotou 1 do naseho slovniku

# prave jsme prosli pres vsechna slova, zkusime si teda vypsat nas slovnik
# ale abychom odfiltrovali nudne vysledky, vypiseme jen ta slova, ktera se opakovala 5x ci vice

limit = 4
print("Tato slova maji vyskyt vetsi nez:", limit)

# pro kazdy zaznam x ve slovniku
for x in slovnik:
    if slovnik[x] >= limit: # pokud je hodnota ulozena pod klicem x vetsi limitu 4
        print(x, slovnik[x]) # pak vypiseme klic x a vypiseme hodnotu ulozenou pod klicem x ve slovnivku

