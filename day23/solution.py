def product_sort(products: list[dict]) -> list[str]:
    """stockが1以上の商品情報を価格昇順のリストで返す"""
    for product in products:
        if not product['price'] != int:
            raise ValueError("priceに整数ではないものがあります")
    price_sort_list = sorted(products, key=lambda x: x["price"])
    return [f"{product['name']} : {product['price']}円 在庫{product['stock']}個" for product in price_sort_list if product['stock'] > 0]


products = [
    {"name": "鉛筆", "price": 100, "stock": 10},
    {"name": "消しゴム", "price": 80, "stock": 0},
    {"name": "ノート", "price": 120, "stock": 5},
    {"name": "定規", "price": 90, "stock": 3}
]

print(product_sort(products))