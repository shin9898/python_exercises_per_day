def sum_price(product_list: list[dict]) -> int:
    for product in product_list:
        if not isinstance(product["price"], int):
            raise ValueError("商品価格に不正な値があります")
    return sum(product["price"] for product in product_list)

def summarize_by_category(purchases: list[dict]) -> list:
    foodstuff_list = [product for product in purchases if product["category"] == "食品"]
    clothing_list = [product for product in purchases if product["category"] == "衣類"]
    stationery_list = [product for product in purchases if product["category"] == "文房具"]
    return [
        f"食品: 合計{sum_price(foodstuff_list)}円({len(foodstuff_list)}件)",
        f"衣類: 合計{sum_price(clothing_list)}円({len(clothing_list)}件)",
        f"文房具: 合計{sum_price(stationery_list)}円({len(stationery_list)}件)"
        ]


if __name__ == '__main__':
    purchases = [
        {"name": "りんご", "price": 120, "category": "食品"},
        {"name": "Tシャツ", "price": 1500, "category": "衣類"},
        {"name": "パン", "price": 200, "category": "食品"},
        {"name": "ズボン", "price": 3000, "category": "衣類"},
        {"name": "ボールペン", "price": 100, "category": "文房具"}
    ]

    print(summarize_by_category(purchases))

# 模範回答 - 動作チェック
from collections import OrderedDict

def summarize_by_category(purchases: list[dict]) -> list[str]:
    summary = OrderedDict()

    for item in purchases:
        category = item["category"]
        price = item["price"]

        if not isinstance(price, int):
            raise ValueError("価格が不正です")

        if category not in summary:
            summary[category] = {"total": 0, "count": 0}

        summary[category]["total"] += price
        summary[category]["count"] += 1

    return [
        f"{category}：合計{data['total']}円（{data['count']}件）"
        for category, data in summary.items()
    ]

if __name__ == '__main__':
    purchases = [
        {"name": "りんご", "price": 120, "category": "食品"},
        {"name": "Tシャツ", "price": 1500, "category": "衣類"},
        {"name": "パン", "price": 200, "category": "食品"},
        {"name": "ズボン", "price": 3000, "category": "衣類"},
        {"name": "ボールペン", "price": 100, "category": "文房具"}
    ]

    print(summarize_by_category(purchases))