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
            raise TypeError("登録しようとしているオブジェクトはCustomerクラスのインスタンスではありません。")
        elif customer.customer_id in self.registered_customers:
            return False, f"登録しようとしているIDは既に登録済みです。"
        elif len(self.registered_customers) >= self.capacity:
            return False, f"定員オーバーです。"
        else:
            self.registered_customers.append(customer.customer_id)
            return True

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


class EventManager:
    def __init__(self):
        self.events = []
        self.events_by_id = {}

    def add_event(self, event: Event):
        if not isinstance(event, Event):
            raise TypeError("追加しようとしているオブジェクトはEventクラスのオブジェクトではありません。")
        elif event.event_id in self.events_by_id or event in self.events:
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
            raise TypeError("登録しようとしているオブジェクトはCustomerクラスのオブジェクトではありません。")
        event = self.find_event(event_id)
        if not event is None:
            if event.register_customer(customer) is True:
                print(f"『{event.title}』に顧客『{customer.name}』が登録されました。")
            else:
                print(event.register_customer(customer)[1])
        else:
            print(f"イベントID『{event_id}』のイベントは見つかりませんでした。")

    def cancel_customer_registration(self, customer_id: str, event_id: str):
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
# EventManager のインスタンスを作成する。
    event_manager = EventManager()

    # 複数の Customer インスタンスと Event インスタンスを作成する。
    customer1 = Customer("CUST001", "佐藤 太郎", "sato.taro@example.com")
    customer2 = Customer("CUST002", "鈴木 花子", "suzuki.hanako@example.com")
    customer3 = Customer("CUST003", "田中 次郎", "tanaka.jiro@example.com")
    customer4 = Customer("CUST004", "高橋 結衣", "takahashi.yui@example.com")
    customer5 = Customer("CUST005", "渡辺 健", "watanabe.ken@example.com")

    event1 = Event("EVT001", "Python Web開発入門", "2025-06-15", 2) # 定員2名でテスト
    event2 = Event("EVT002", "データ分析とAI活用", "2025-07-20", 3) # 定員3名
    event3 = Event("EVT003", "クラウド基礎セミナー", "2025-08-10", 1) # 定員1名でテスト
    event_duplicate_id = Event("EVT001", "重複IDイベント", "2025-10-01", 5) # 重複IDテスト用

    # add_event でイベントを EventManager に追加する。（重複イベントも試す）
    print("\n--- イベント追加 ---")
    event_manager.add_event(event1)
    event_manager.add_event(event2)
    event_manager.add_event(event3)
    event_manager.add_event(event_duplicate_id) # 重複イベントの追加を試す

    # display_all_events_summary で初期状態を確認する。
    print("\n--- 初期イベントサマリー ---")
    event_manager.display_all_events_summary()

    # register_customer_to_event を使って、異なるイベントに顧客を登録する。
    print("\n--- 顧客登録 ---")
    # 成功するケース
    event_manager.register_customer_to_event(customer1, "EVT001") # EVT001に佐藤
    event_manager.register_customer_to_event(customer2, "EVT001") # EVT001に鈴木
    event_manager.register_customer_to_event(customer3, "EVT002") # EVT002に田中

    # 定員オーバーになるケース
    event_manager.register_customer_to_event(customer4, "EVT001") # EVT001は定員2なので定員オーバーになるはず
    event_manager.register_customer_to_event(customer5, "EVT003") # EVT003は定員1なので、次に登録すると定員オーバー

    # 二重登録になるケース
    event_manager.register_customer_to_event(customer1, "EVT001") # EVT001に佐藤は既に登録済みのはず

    # 存在しないイベントIDへの登録ケース
    event_manager.register_customer_to_event(customer1, "EVT00X")

    # 各登録試行後、display_all_events_summary で登録人数が更新されたことを確認する。
    print("\n--- 登録後イベントサマリー ---")
    event_manager.display_all_events_summary()

    # cancel_customer_registration を使って、登録をキャンセルする。
    print("\n--- 顧客登録キャンセル ---")
    # 成功するケース
    event_manager.cancel_customer_registration(customer2.customer_id, "EVT001") # EVT001から鈴木をキャンセル
    event_manager.cancel_customer_registration(customer3.customer_id, "EVT002") # EVT002から田中をキャンセル

    # 存在しない顧客IDでのキャンセルケース
    event_manager.cancel_customer_registration("CUST999", "EVT001") # EVT001に存在しない顧客ID
    event_manager.cancel_customer_registration(customer1.customer_id, "EVT002") # EVT002に佐藤は登録していない

    # 存在しないイベントIDでのキャンセルケース
    event_manager.cancel_customer_registration(customer1.customer_id, "EVT00Y")

    # 各キャンセル試行後、display_all_events_summary で登録人数が更新されたことを確認する。
    print("\n--- キャンセル後イベントサマリー ---")
    event_manager.display_all_events_summary()

    print("\n--- 最終イベントサマリー ---")
    event_manager.display_all_events_summary()