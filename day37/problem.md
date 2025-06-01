---

### 📝 Python基礎力強化 - Day37

---

お疲れ様です！Python基礎力強化、Day37です。前回は、Day36のコードの評価と、現在の課題点を踏まえた次のステップについてお話ししました。

今回は、Day36で途中まで実装したクラスのうち、**`Customer`と`Event`クラスの完成、およびそれらの単体テスト**に焦点を当てます。`EventManager`クラスについては、今回は`add_event`メソッドのみを使用し、その他の複雑な連携はDay38以降に持ち越します。

---

### 問題

あなたはイベント企画会社の担当者で、顧客情報とイベント単体の管理機能を実装しています。

以下の要件を満たすPythonコードを記述してください。

1.  **`Customer` クラスを完成**させてください。
    * 属性: `customer_id` (文字列、一意), `name` (文字列), `email` (文字列)
    * メソッド:
        * `__init__(self, customer_id, name, email)`: 顧客の初期情報を設定します。
        * `display_info(self)`: **顧客ID、名前、メールアドレスを表示**する。
            * 例: `顧客ID: CUST001, 名前: 佐藤 太郎, メール: sato.taro@example.com`

2.  **`Event` クラスを完成**させてください。
    * 属性: `event_id` (文字列、一意), `title` (文字列), `date` (文字列、例: "YYYY-MM-DD"), `capacity` (整数、最大参加人数), `registered_customers` (リスト、初期値は空のリスト)
    * メソッド:
        * `__init__(self, event_id, title, date, capacity)`: イベントの初期情報を設定します。
        * `register_customer(self, customer: Customer)`:
            * 引数として `Customer` クラスのインスタンスを受け取ります。
            * イベントの定員 (`capacity`) に達していない、かつ、その顧客の `customer_id` がまだ `registered_customers` リストに存在しない場合に、顧客の `customer_id` をリストに追加します。
            * 登録に成功したら、`True` を返す。
            * 定員オーバーの場合、`False` を返す。
            * 既に登録済みの場合、`False` を返す。
            * **表示メッセージは、このメソッドでは不要です。** (メッセージの表示は`EventManager`の役割とします)
        * `cancel_registration(self, customer_id: str)`:
            * 引数として `customer_id` を受け取ります。
            * `registered_customers` リストに該当の `customer_id` が存在する場合、そのIDをリストから削除します。
            * キャンセルに成功したら、`True` を返す。
            * 該当の `customer_id` が見つからない場合、`False` を返す。
            * **表示メッセージは、このメソッドでは不要です。** (メッセージの表示は`EventManager`の役割とします)
        * `get_registered_count(self)`:
            * 現在 `registered_customers` リストに登録されている顧客の人数を返す。
        * `display_event_info(self)`:
            * イベントのタイトル、日付、定員、現在の登録人数 (`get_registered_count`を使用) を表示する。
            * 例: `イベント: Python Web開発入門 (2025-06-15), 定員: 5, 登録人数: 2`

3.  `__main__` ブロックで、以下の処理を実行し、**各クラスのメソッドの動作を確認**してください。（`EventManager`のメソッドは今回`add_event`以外は使いません）

    * `Customer` クラスのインスタンスを2つ作成し、それぞれの `display_info` を呼び出して表示を確認する。
        ```python
        # Customer インスタンスの作成例
        customer1 = Customer("CUST001", "佐藤 太郎", "sato.taro@example.com")
        customer2 = Customer("CUST002", "鈴木 花子", "suzuki.hanako@example.com")
        ```
    * `Event` クラスのインスタンスを1つ作成し、`display_event_info` で初期状態を確認する。
        ```python
        # Event インスタンスの作成例
        event1 = Event("EVT001", "Python Web開発入門", "2025-06-15", 2) # 定員2名でテスト
        ```
    * 作成した `Customer` インスタンスを使って、`Event` インスタンスの `register_customer` メソッドを複数回呼び出す。（**成功、定員オーバー、重複登録の各パターン**で返り値を確認）
        ```python
        # register_customer の呼び出し例
        print(f"登録試行1 (成功想定): {event1.register_customer(customer1)}") # True
        print(f"登録試行2 (成功想定): {event1.register_customer(customer2)}") # True
        print(f"登録試行3 (定員オーバー想定): {event1.register_customer(customer3)}") # False (customer3は別途作成)
        print(f"登録試行4 (重複登録想定): {event1.register_customer(customer1)}") # False
        ```
    * 各登録試行後、`Event` インスタンスの `display_event_info` を呼び出し、登録人数の変化を確認する。
    * `cancel_registration` メソッドを呼び出し、登録のキャンセルを試す。（**成功、未登録の顧客IDでのキャンセル**を試す）
        ```python
        # cancel_registration の呼び出し例
        print(f"キャンセル試行1 (成功想定): {event1.cancel_registration('CUST002')}") # True
        print(f"キャンセル試行2 (未登録ID想定): {event1.cancel_registration('CUST004')}") # False
        ```
    * キャンセル後、`Event` インスタンスの `display_event_info` を呼び出し、登録人数の変化を確認する。

---