def total_food_price(purchases: list[dict]) -> int:
    """category:食品の合計金額を返す"""
    for product in purchases:
        if not isinstance(product['price'], int):
            raise ValueError('価格に不正な値があります')
    food_price_list = [product['price'] for product in purchases if product['category'] == "食品"]
    return sum(food_price_list)

if __name__ == '__main__':
    purchases = [
        {"name": "りんご", "price": 120, "category": "食品"},
        {"name": "Tシャツ", "price": 1500, "category": "衣類"},
        {"name": "パン", "price": 200, "category": "食品"}
    ]
    print(total_food_price(purchases))