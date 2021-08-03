
# Pořadatel našeho večírku se stává stále více paranoidním a nyní rozhodl, že každý z hostů bude mít speciální heslo, které je platné jen pro něj. Seznam hostů a jejich hesel je níže. Napiš program, který nejprve zkontroluje, zda je host na seznamu, a pokud tam je, zeptá se ho na heslo a zkontroluje jeho správnost. Hostu na seznamu, který zadá správné heslo, vypíše program text: “Smíš vstoupit.”

passwords = {"Jiří": "tajne-heslo", "Natálie": "jeste-tajnejsi-heslo", "Klára": "nejtajnejsi-heslo"}

jméno = input("Zadej svoje jméno:")
if jméno in passwords:
    heslo = input("Zadej heslo:")
    if heslo == passwords[jméno]:
        print("Můžeš vejít")
    else:
        print("Přístup zamínut, špatné heslo")
else:
    print("Nebyl jsi pozván")
