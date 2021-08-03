item = {"title": "konvička", "price": 899, "in Stock": True}

item["price"] = 929
print("Název položky je", item["title"])
print("Název položky je "+ str(item["title"]))
print(f"Cena položky je {item['price']}")
print(item)
item["weight"] = 0.5

if "weight" in item:
    print(item["weight"])
else:
    print("Hmotnost není zadaná.")


sausages = {"Jirka": 2, "Naty": 1, "Adam":4, "Lucka": 2}
print(len(sausages))
sausages.pop("Adam")
