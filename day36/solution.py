class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def desplay_info(self):
        pass


class Event:
    def __init__(self, event_id, title, date, capacity):
        self.event_id = event_id
        self.title = title
        self.date = date
        self.capacity = capacity
        self.registered_customers = []

    def register_customer(self, customer: Customer):
        pass

    def cancel_registration(self, customer_id: str):
        pass

    def get_registered_count(self):
        pass


class EventManager:
    def __init__(self):
        self.events = []
        self.events_by_id = {}

    def add_event(self, event: Event):
        if not isinstance(event, Event):
            raise ValueError("追加しようとしているオブジェクトはEventクラスのインスタンスではありません。")

        if event.event_id in self.events_by_id:
            print(f"警告: イベントID: '{event.event_id}' のイベント '{event.title}' は既に登録されています。")
            return

        self.events.append(event)
        self.events_by_id[event.event_id] = event
        print(f"{event.title}が追加されました。")

    def find_event(self, event_id: str) -> Event | None:
        pass

    def register_customer_to_event(self, customer: Customer, event_id: str):
        if not isinstance(customer,Customer):
            raise ValueError("登録しようとしているオブジェクトはCustomerクラスのインスタンスではありません。")
        event_to_register = self.events_by_id
        # for event in self.events:
        #     if event_id == event.event_id:
        #         event.register_customer(customer)
        #     else:
        #         print(f"イベントID:{event_id}のイベントは見つかりませんでした。")

    def cancel_customer_registration(self, customer_id: str, event_id: str):
        pass

    def display_all_events_summary(self):
        for event in self.events:
            print(f"イベントID:{event.event_id} タイトル:{event.title} 開催日:{event.date} 定員:{event.capacity}")


if __name__ == '__main__':
    event_manager = EventManager()
    # Customer インスタンスの作成
    customer1 = Customer("CUST001", "佐藤 太郎", "sato.taro@example.com")
    customer2 = Customer("CUST002", "鈴木 花子", "suzuki.hanako@example.com")
    customer3 = Customer("CUST003", "田中 次郎", "tanaka.jiro@example.com")
    customer4 = Customer("CUST004", "高橋 結衣", "takahashi.yui@example.com")

    # Event インスタンスの作成
    event1 = Event("EVT001", "Python Web開発入門", "2025-06-15", 5) # 定員5名
    event2 = Event("EVT002", "データ分析とAI活用", "2025-07-20", 3) # 定員3名
    event3 = Event("EVT003", "クラウド基礎セミナー", "2025-08-10", 10) # 定員10名
    event4 = Event("EVT004", "Python Web開発入門", "2025-09-01", 5) # 別日程の同じタイトルのイベント

    event_manager.add_event(event1)
    event_manager.add_event(event2)
    event_manager.add_event(event3)
    event_manager.add_event(event4)
    event_manager.display_all_events_summary()
    event_manager.register_customer_to_event(customer1, "EVT001")
    event_manager.register_customer_to_event(customer1, "EVT001") # 重複
    event_manager.register_customer_to_event(customer1, "EVT002")
    event_manager.register_customer_to_event(customer2, "EVT002")
    event_manager.register_customer_to_event(customer3, "EVT002")
    event_manager.register_customer_to_event(customer4, "EVT002") # 定員オーバー