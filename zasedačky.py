# Firma eviduje volné meetingové místnosti v průběhu dne ve slovníku.
# Klíč slovníku je hodina a hodnotou slovníku seznam zasedaček, které jsou v té době volné.
# Napiš software, který se zeptá uživatele na číslo hodiny, kdy chce zamluvit meeting room.
# Poté vypíše počet volných místností, které jsou k dispozici.
# Pokud není k dispozici žádná místnost, program vypíše V tuto hodinu již není k dispozici žádná zasedací místnost.

volnePokoje = {
  9: ["Amadeus", "Goya", "Vlasy"],
  10: ["Forman", "Goya"],
  11: [],
  12: ["Amadeus", "Vlasy"]
}

cas = int(input("Na jakou hodinu chceš zasedačku?"))
if volnePokoje[cas] == []:

    print("Žádná zasedačka není volná.")
else:
    print("Jsou volné tyto zasedačky:", volnePokoje[cas])
    print("Počet volných zasedaček je",len(volnePokoje[cas]))


