import sqlite3

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
    def __init__(self, db_name='events.db'):
        self.db_name = db_name
        self.events = []
        self.events_by_id = {}

    def connect_db(self) -> None:
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.conn.execute('PRAGMA foreign_keys = ON')

    def close_db(self) -> None:
        try:
            self.cursor.close()
            self.conn.close()
            print("データベース接続を閉じました。")
        except sqlite3.Error as e:
            print(f"データベース切断エラー: [{e.args[0]}]")

    def create_tables(self) -> None:
        self.cursor.execute(
            "CREATE TABLE events(" \
            "event_id TEXT PRIMARY KEY," \
            "title TEXT NOT NULL," \
            "date TEXT NOT NULL," \
            "capacity INTEGER NOT NULL)"
        )
        self.cursor.execute(
            "CREATE TABLE customers(" \
            "customer_id TEXT PRIMARY KEY," \
            "name TEXT NOT NULL," \
            "email TEXT NOT NULL)"
        )
        try:
            self.conn.commit()
            print("テーブルを正常に作成しました。")
        except sqlite3.Error as e:
            print(f"テーブル作成エラー: {e.args[0]}")

    def add_event(self, event: Event):
        if not isinstance(event, Event):
            raise TypeError("追加しようとしているオブジェクトはEventクラスのインスタンスではありません。")
        if event.event_id in self.events_by_id:
            print(f"警告: イベントID『{event.event_id}』のイベントは既に登録されています。")
        else:
            try:
                sql = "INSERT INTO events (event_id, title, date, capacity) VALUES (?, ?, ?, ?)"
                # パラメータはタプルとして渡す
                self.cursor.execute(sql, (event.event_id, event.title, event.date, event.capacity))
                self.conn.commit() # 変更をデータベースにコミット
                print(f"イベント『{event.title}』がデータベースに登録されました。")
            except sqlite3.Error as e:
                print(f"イベント『{event.title}』のデータベース登録に失敗しました: {e}")
                # エラーが発生した場合はロールバックすることも検討
                if self.conn:
                    self.conn.rollback()


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
    event_manager = EventManager()
    event_manager.connect_db()
    try:
        event_manager.create_tables()
    except sqlite3.OperationalError as e:
        print(f"テーブル作成エラー: [{e.args[0]}]")

    # Eventインスタンス作成
    event1 = Event("EVT001", "Pythonイベント", "2025-12-31", 5)
    event2 = Event("EVT002", "Djangoイベント", "2025-6-9", 10)
    event3 = Event("EVT003", "sqlite3イベント", "2025-10-14", 3)
    event_manager.add_event(event1)
    event_manager.add_event(event2)
    event_manager.add_event(event3)

    event_manager.close_db()
