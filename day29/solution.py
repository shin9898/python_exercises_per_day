def price_sort(status_checked_list: list[dict]) -> list[dict]:
    sorted_list = sorted(status_checked_list, key=lambda x: x['price'], reverse=True)
    result_list = [{order['order_id'], order['item'], order['price']} for order in sorted_list]
    return result_list




def status_check(orders: list[dict]) -> list[dict]:
    status_checked_list = [order for order in orders if order['status'] == 'shipped']
    return price_sort(status_checked_list)



if __name__ == '__main__':
    orders = [
    {"order_id": "A001", "item": "Laptop", "price": 120000, "quantity": 1, "status": "shipped"},
    {"order_id": "A002", "item": "Mouse", "price": 3000, "quantity": 2, "status": "pending"},
    {"order_id": "A003", "item": "Keyboard", "price": 8000, "quantity": 1, "status": "shipped"},
    {"order_id": "A004", "item": "Monitor", "price": 25000, "quantity": 1, "status": "pending"},
    {"order_id": "A005", "item": "Laptop", "price": 150000, "quantity": 1, "status": "shipped"},
    {"order_id": "A006", "item": "Webcam", "price": 5000, "quantity": 3, "status": "shipped"},
    {"order_id": "A007", "item": "SSD", "price": 10000, "quantity": 2, "status": "cancelled"},
    {"order_id": "A008", "item": "Mouse", "price": 3500, "quantity": 1, "status": "shipped"},
]

    print(status_check(orders))