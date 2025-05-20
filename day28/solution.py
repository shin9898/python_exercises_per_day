from collections import defaultdict

def max_sales_category(sales: list[dict]) -> str:
    summary = defaultdict(lambda: {"count": 0, "total": 0})
    for item in sales:
        category = item['category']
        price = item['price']

        if not isinstance(category, str):
            continue
        if not isinstance(price, int):
            raise ValueError("priceが不正な値です")

        summary[category]['total'] += price
        summary[category]['count'] += 1
    price_list = [data['total'] for _, data in summary.items()]
    high_price = max(price_list)
    for category, date in summary.items():
        if date['total'] == high_price:
            return category




if __name__ == '__main__':

    sales = [
        {"name": "りんご", "price": 120, "category": "食品"},
        {"name": "Tシャツ", "price": 1500, "category": "衣類"},
        {"name": "パン", "price": 200, "category": "食品"},
        {"name": "ズボン", "price": 3000, "category": "衣類"},
        {"name": "ボールペン", "price": 100, "category": "文房具"},
        {"name": "ノート", "price": 150, "category": "文房具"},
        {"name": "シャーペン", "price": 120, "category": "文房具"}
    ]

    print(max_sales_category(sales))