addresses = [
    {"zipcode": "160-0022", "pref": "東京都", "city": "新宿区新宿"},
    {"zipcode": "150-0001", "pref": "東京都", "city": "渋谷区神宮前"}
]

for address in addresses:
    print(f"{address["zipcode"]} {address["pref"]}{address["city"]}")