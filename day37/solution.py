class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def display_info(self):
        print(f"顧客ID: {self.customer_id}, 名前: {self.name}, メール: {self.email}")


class Event:
    def __init__(self, event_id, title, date, capacity):
        self.event_id = event_id
        self.title = title
        self.date = date
        self.capacity = capacity
        self.registered_customers = []

    def register_customer(self, customer: Customer):
        if not isinstance(customer, Customer):
            raise ValueError("登録しようとしているオブジェクトはCustomerクラスのインスタンスではありません。")
        if not customer.customer_id in self.registered_customers and len(self.registered_customers) < self.capacity:
            self.registered_customers.append(customer.customer_id)
            return True
        else:
            return False

    def cancel_registration(self, customer_id: str):
        if customer_id in self.registered_customers:
            self.registered_customers.remove(customer_id)
            return True
        else:
            return False

    def get_registered_count(self):
        return len(self.registered_customers)

    def display_event_info(self):
        print(f"イベント: {self.title} ({self.date}), 定員: {self.capacity}, 登録人数: {self.get_registered_count()}")


if __name__ == '__main__':
    customer1 = Customer("CUST001", "佐藤 太郎", "sato.taro@example.com")
    customer2 = Customer("CUST002", "鈴木 花子", "suzuki.hanako@example.com")
    customer3 = Customer("CUST003", "田中 元", "tanaka.hajime@example.com")
    customer1.display_info()
    customer2.display_info()

    event1 = Event("EVT001", "Python Web開発入門", "2025-06-15", 2)
    # register_customer の呼び出し
    print(f"登録試行1 (成功想定): {event1.register_customer(customer1)}") # True
    event1.display_event_info()
    print(f"登録試行2 (成功想定): {event1.register_customer(customer2)}") # True
    event1.display_event_info()
    print(f"登録試行3 (定員オーバー想定): {event1.register_customer(customer3)}") # False (customer3は別途作成)
    event1.display_event_info()
    print(f"登録試行4 (重複登録想定): {event1.register_customer(customer1)}") # False
    event1.display_event_info()

    # cancel_registration の呼び出し
    print(f"キャンセル試行1 (成功想定): {event1.cancel_registration('CUST002')}") # True
    event1.display_event_info()
    print(f"キャンセル試行2 (未登録ID想定): {event1.cancel_registration('CUST004')}") # False
    event1.display_event_info()