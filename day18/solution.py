def main(items: list[dict]) -> list[str]:
    row_list = [f"{item['name']}は{item['price']}円で在庫あり" for item in items if item['stock'] > 0]
    print(row_list)


if __name__ == '__main__':
    items = [
        {"name": "定規", "price": 80, "stock": 0},
        {"name": "ホッチキス", "price": 300, "stock": 2},
        {"name": "鉛筆", "price": 60, "stock": 5}
    ]
    # 出力例
    # ["ホッチキスは300円で在庫あり", "鉛筆は60円で在庫あり"]
    main(items)