def total_food_amount(purchases: list[dict]) -> int:
    foods_price_list = [product["price"] for product in purchases if product["category"] == "食品"]
    return sum(foods_price_list)

purchases = [
    {"name": "りんご", "price": 120, "category": "食品"},
    {"name": "Tシャツ", "price": 1500, "category": "衣類"},
    {"name": "パン", "price": 200, "category": "食品"}
]

print(total_food_amount(purchases))