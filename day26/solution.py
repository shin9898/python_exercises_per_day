from collections import OrderedDict

def category_count(products: list[dict]) -> list[str]:
    summary = OrderedDict()
    for item in products:
        category = item['category']

        if not isinstance(category, str):
            next

        if category not in summary:
            summary[category] = {"count": 0}
        summary[category]['count'] += 1
    return [f"{category}:{data["count"]}件" for category, data in summary.items()]

if __name__ == '__main__':
    products = [
        {"name": "りんご", "price": 120, "category": "食品"},
        {"name": "パン", "price": 200, "category": "食品"},
        {"name": "Tシャツ", "price": 1500, "category": "衣類"},
        {"name": "ズボン", "price": 3000, "category": "衣類"},
        {"name": "ボールペン", "price": 100, "category": "文房具"},
    ]

    print(category_count(products))
