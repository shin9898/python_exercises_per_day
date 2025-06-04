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
        if capacity <= 0:
            raise ValueError("定員は1以上の整数である必要があります。")
        else:
            self.capacity = capacity
        self.registered_customers = []

    def register_customer(self, customer: Customer):
        if not isinstance(customer, Customer):
            raise TypeError("登録しようとしているオブジェクトはCustomerクラスのインスタンスではありません。")
        elif customer.customer_id in self.registered_customers:
            return False, f"登録しようとしているIDは既に登録済みです。"
        elif len(self.registered_customers) >= self.capacity:
            return False, f"定員オーバーです。"
        else:
            self.registered_customers.append(customer.customer_id)
            return True, None

    def cancel_registration(self, customer_id: str):
        if customer_id == "":
            raise ValueError("顧客IDは空にできません。")
        if customer_id in self.registered_customers:
            self.registered_customers.remove(customer_id)
            return True
        else:
            return False

    def get_registered_count(self):
        return len(self.registered_customers)

    def display_event_info(self):
        print(f"イベント: {self.title} ({self.date}), 定員: {self.capacity}, 登録人数: {self.get_registered_count()}")


class EventManager:
    def __init__(self):
        self.events = []
        self.events_by_id = {}

    def add_event(self, event: Event):
        if not isinstance(event, Event):
            raise TypeError("追加しようとしているオブジェクトはEventクラスのインスタンスではありません。")
        if event.event_id in self.events_by_id:
            print(f"警告: イベントID『{event.event_id}』のイベントは既に登録されています。")
        else:
            self.events.append(event)
            self.events_by_id[event.event_id] = event
            print(f"イベント『{event.title}』が追加されました。")

    def find_event(self, event_id: str) -> Event | None:
        if not event_id in self.events_by_id:
            return None
        else:
            return self.events_by_id[event_id]

    def register_customer_to_event(self, customer: Customer, event_id: str):
        if not isinstance(customer, Customer):
            raise TypeError("登録しようとしているオブジェクトはCustomerクラスのインスタンスではありません。")
        if event_id == "":
            raise ValueError("イベントIDは空にできません。")
        event = self.find_event(event_id)
        if not event is None:
            success, message = event.register_customer(customer)
            if success:
                print(f"『{event.title}』に顧客『{customer.name}』が登録されました。")
            else:
                if message:
                    print(message)
        else:
            print(f"イベントID『{event_id}』のイベントは見つかりませんでした。")

    def cancel_customer_registration(self, customer_id: str, event_id: str):
        if customer_id == "":
            raise ValueError("顧客IDは空にできません。")
        if event_id == "":
            raise ValueError("イベントIDは空にできません。")
        event = self.find_event(event_id)
        if not event is None:
            if event.cancel_registration(customer_id):
                print(f"『{event.title}』から顧客ID『{customer_id}』の登録がキャンセルされました。")
            else:
                print(f"顧客ID『{customer_id}』は『{event.event_id}』に登録されていません。")
        else:
            print(f"イベントID『{event_id}』のイベントは見つかりませんでした。")

    def display_all_events_summary(self):
        if len(self.events) > 0:
            for event in self.events:
                print(f"タイトル:{event.title}、日付:{event.date}、現在の登録人数:{len(event.registered_customers)}人、定員:{event.capacity}人")
        else:
            print("現在、登録されているイベントはありません。")

if __name__ == '__main__':
    customer1 = Customer("CUST001", "佐藤 太郎", "sato.taro@example.com")
    customer2 = Customer("CUST002", "鈴木 花子", "suzuki.hanako@example.com")
    customer3 = Customer("CUST003", "田中 次郎", "tanaka.jiro@example.com")
    customer4 = Customer("CUST004", "高橋 結衣", "takahashi.yui@example.com")
    customer5 = Customer("CUST005", "渡辺 健", "watanabe.ken@example.com")
    event_manager = EventManager()
    print("\n--- Event容量不正テスト ---")
    try:
        invalid_event = Event("EVT999", "不正容量イベント", "2025-12-31", 0) # 定員0
    except ValueError as e:
        print(f"エラー捕捉: {e}")

    try:
        invalid_event2 = Event("EVT998", "不正容量イベント2", "2025-12-31", -5) # 定員負数
    except ValueError as e:
        print(f"エラー捕捉: {e}")

    print("\n--- add_event 型不正テスト ---")
    try:
        event_manager.add_event("これはイベントではありません")
    except TypeError as e:
        print(f"エラー捕捉: {e}")

    print("\n--- register_customer_to_event 型不正テスト ---")
    try:
        event_manager.register_customer_to_event("これは顧客ではありません", "EVT001")
    except TypeError as e:
        print(f"エラー捕捉: {e}")

    print("\n--- ID空文字列テスト ---")
    try:
        event_manager.register_customer_to_event(customer1, "") # 空のevent_id
    except ValueError as e:
        print(f"エラー捕捉: {e}")

    try:
        event_manager.cancel_customer_registration("", "EVT001") # 空のcustomer_id
    except ValueError as e:
        print(f"エラー捕捉: {e}")

    try:
        event_manager.cancel_customer_registration(customer1.customer_id, "") # 空のevent_id
    except ValueError as e:
        print(f"エラー捕捉: {e}")