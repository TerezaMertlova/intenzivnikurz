vysvedceni = {"český jazyk": 1, "matematika": 2, "dejepis": 3}
print(vysvedceni)

# Zkopíruj si slovník do svého programu.
# Přidej do slovníku nově vydanou detektivku "Noc, která mě zabila", která zatím nebyla uvedena na trh, je tedy prodáno 0 kusů.
# U knihy "Vrah zavolá v deset" zvyš počet prodaných kusů o 100.

sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

sales["Noc, která mě zabila"] = 0
print(sales)

sales["Vrah zavolá v deset"] = sales["Vrah zavolá v deset"] + 100
print(sales)
