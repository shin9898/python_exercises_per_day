def stock_check(products: list[dict]) -> list[dict]:
    return [product for product in products if product["stock"] <= 10]


def tags_check(products: list[dict]) -> list[dict]:
    return [product for product in products if "business" in product["tags"]  or "gaming" in product["tags"]]


def price_sorted(products: list[dict]) -> list[dict]:
    sorted_list = sorted(products, key=lambda product: (product["price"], product['product_id']))
    return [{"name": product["name"], "price": product["price"]} for product in sorted_list]

if __name__ == '__main__':
    products = [
        {"product_id": "P001", "name": "Laptop Pro", "category": "Laptop", "price": 150000, "stock": 5, "tags": ["high-performance", "business"]},
        {"product_id": "P002", "name": "Basic Mouse", "category": "Peripheral", "price": 2500, "stock": 50, "tags": ["office", "wireless"]},
        {"product_id": "P003", "name": "Gaming Keyboard", "category": "Peripheral", "price": 12000, "stock": 10, "tags": ["gaming", "mechanical"]},
        {"product_id": "P004", "name": "Ultrabook Air", "category": "Laptop", "price": 180000, "stock": 3, "tags": ["thin", "portable", "business"]},
        {"product_id": "P005", "name": "External SSD 1TB", "category": "Storage", "price": 18000, "stock": 15, "tags": ["fast", "portable"]},
        {"product_id": "P006", "name": "Wireless Headset", "category": "Audio", "price": 7000, "stock": 20, "tags": ["wireless", "gaming"]},
        {"product_id": "P007", "name": "4K Monitor 27inch", "category": "Monitor", "price": 45000, "stock": 7, "tags": ["high-resolution", "display"]},
        {"product_id": "P008", "name": "Webcam HD", "category": "Peripheral", "price": 4000, "stock": 30, "tags": ["video", "office"]},
    ]
    products = stock_check(products)
    products = tags_check(products)
    print(price_sorted(products))
