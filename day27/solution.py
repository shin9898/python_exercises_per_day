from collections import OrderedDict

def category_calculation(products: list[dict]) -> list[str]:
    summary = OrderedDict()
    for item in products:
        category = item['category']
        price = item['price']

        if not isinstance(category, str):
            continue
        if not isinstance(price, int):
            raise ValueError("priceに不正な値が入っています。")

        if category not in summary:
            summary[category] = {'count': 0,'total': 0}
        summary[category]['total'] += price
        summary[category]['count'] += 1
    return [f"{category}:合計{data['total']}円、平均{round(data['total']/data['count'])}円" for category, data in summary.items()]

if __name__ == '__main__':
    products = [
    {"name": "りんご", "price": 120, "category": "食品"},
    {"name": "パン", "price": 200, "category": "食品"},
    {"name": "Tシャツ", "price": 1500, "category": "衣類"},
    {"name": "ズボン", "price": 3000, "category": "衣類"},
    {"name": "ボールペン", "price": 100, "category": "文房具"},
    {"name": "ノート", "price": 150, "category": "文房具"}
    ]

    print(category_calculation(products))