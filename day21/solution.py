def discount_calculation(products: list[dict]) -> list[str]:
    return [f"{product['name']}の割引後の価格は{round(product['price'] * (1 - product['discount'] / 100))}円です" for product in products]


if __name__ == '__main__':
    products = [
        {"name": "Tシャツ", "price": 2000, "discount": 20.0},
        {"name": "ジーンズ", "price": 5000, "discount": 10.0},
        {"name": "帽子", "price": 1500, "discount": 0.0},
    ]
    print(discount_calculation(products))
