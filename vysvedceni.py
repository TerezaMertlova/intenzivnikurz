#
# Uvažujme vysvědčení, které máme zapsané jako slovník.
#
# Napiš program, který spočte průměrnou známku ze všech předmětů.
# Uprav program, aby vypsal všechny předměty, ve kterých získal student známku 1.

schoolReport = {
  "Český jazyk": 1,
  "Anglický jazyk": 1,
  "Matematika": 1,
  "Přírodopis": 2,
  "Dějepis": 1,
  "Fyzika": 2,
  "Hudební výchova": 4,
  "Výtvarná výchova": 2,
  "Tělesná výchova": 3,
  "Chemie": 4,
}

soucet = 0
pocet = len(schoolReport)
for predmet, znamka in schoolReport.items():
  soucet = soucet + znamka
  if znamka == 1:
    print(predmet)
prumer = soucet / pocet
print(prumer)

