---

### 📝 Python基礎力強化 - Day41

---

お疲れ様です！Python基礎力強化、Day41です。昨日はデータベースへの接続、テーブル作成、そしてイベントの追加という、基礎の基礎を固めました。SQLインジェクション対策もバッチリで、素晴らしいスタートです！

今日は、データベースからデータを取り出すことに焦点を当てます。特に、個別のイベントを検索する機能と、顧客をイベントに登録する際にその情報をデータベースに記録する方法を学びます。これにより、システムがより動的にデータベースを活用できるようになります。

---

### 問題

あなたはイベント企画会社の担当者で、イベント管理システムに顧客の登録・キャンセル機能をデータベースと連携させます。

以下の要件を満たすPythonコードを記述してください。

1.  **前回までに作成した `Customer` クラス、`Event` クラス、`EventManager` クラスを再利用または定義**してください。
    * （Day40で修正したコードをベースにしてください。特に`EventManager`クラスの`events`リストと`events_by_id`辞書は削除し、データベースが唯一の情報源となるようにします。）

2.  **`EventManager` クラスに以下のメソッドを追加・修正**してください。

    * **`find_event_from_db(self, event_id: str) -> Event | None`** (メソッド名変更)
        * 引数 `event_id` (文字列) を受け取り、**データベース**から該当するイベント情報を検索します。
        * `SELECT` SQL文を使用して、`events` テーブルから `event_id` に一致するレコードを取得します。
        * レコードが見つかった場合、そのデータ（`event_id`, `title`, `date`, `capacity`）を使って新しい **`Event` クラスのインスタンスを作成し、それを返します**。
        * レコードが見つからなければ `None` を返す。
        * データベース操作中にエラーが発生した場合 (`sqlite3.Error` を捕捉)、"イベント検索エラー: [エラーメッセージ]" と表示し、`None` を返す。
        * **（ヒント: カーソルの `fetchone()` メソッドは、結果セットの次の行をタプルとして返します。全ての行を処理した場合は `None` を返します。）**

    * **`register_customer_to_event(self, customer: Customer, event_id: str)` を修正:**
        * このメソッド内で、まず`self.find_event_from_db(event_id)`を呼び出して**データベースからイベントを取得**するように変更します。
        * イベントが見つかった場合、次に**`event_registrations` という新しいテーブルに顧客の登録情報を記録**するようにします。
        * **新しいテーブル `event_registrations` を作成するSQL文を`create_tables`メソッドに追加**してください。
            * テーブル名: `event_registrations`
            * カラム:
                * `registration_id INTEGER PRIMARY KEY AUTOINCREMENT`: 自動的に増えるユニークなID
                * `event_id TEXT NOT NULL`: 登録するイベントのID
                * `customer_id TEXT NOT NULL`: 登録する顧客のID
                * `FOREIGN KEY (event_id) REFERENCES events(event_id)`: `events`テーブルへの外部キー
                * `FOREIGN KEY (customer_id) REFERENCES customers(customer_id)`: `customers`テーブルへの外部キー
                * `UNIQUE (event_id, customer_id)`: 同じイベントに同じ顧客が複数回登録されるのを防ぐ複合ユニーク制約

        * `register_customer_to_event`での登録ロジック:
            * まず、**顧客が既にイベントに登録されているか**を`event_registrations`テーブルから確認します (`SELECT`文)。
            * 次に、**イベントの現在の登録人数が定員に達しているか**を`event_registrations`テーブルから確認します (`SELECT COUNT(*)`文)。
            * これらのチェックをパスした場合のみ、`event_registrations`テーブルに新しい登録 (`INSERT`文) を追加します。
            * 各チェックの結果と登録の成否に応じて、適切なメッセージを`print`する。
            * データベース操作は`self.conn.commit()`で確定する。
            * データベース操作中にエラーが発生した場合 (`sqlite3.Error` を捕捉)、適切なエラーメッセージを表示する。

    * **`cancel_customer_registration(self, customer_id: str, event_id: str)` を修正:**
        * このメソッド内で、まず`self.find_event_from_db(event_id)`を呼び出して**データベースからイベントを取得**するように変更します。
        * イベントが見つかった場合、**`event_registrations` テーブルから顧客の登録情報を削除**するようにします。
        * **顧客がイベントに登録されているか**を`event_registrations`テーブルから確認します (`SELECT`文)。
        * 登録が見つかった場合のみ、`DELETE` SQL文を使ってレコードを削除します。
        * 削除の成否に応じて、適切なメッセージを`print`する。
        * データベース操作は`self.conn.commit()`で確定する。
        * データベース操作中にエラーが発生した場合 (`sqlite3.Error` を捕捉)、適切なエラーメッセージを表示する。

3.  `__main__` ブロックで以下の処理を実行し、動作を確認してください。

    * `EventManager` のインスタンスを作成し、データベースに接続し、**`create_tables()` を呼び出す**。（`event_registrations`テーブルが追加されていることを確認）
    * **顧客インスタンスをデータベースの`customers`テーブルに事前に登録**してください。（`EventManager`にはまだ`add_customer`メソッドがないので、`self.cursor.execute`を直接使って手動で`INSERT`してください。これは一時的な措置です。）
        * 例: `self.cursor.execute("INSERT INTO customers (customer_id, name, email) VALUES (?, ?, ?)", ("CUST001", "佐藤 太郎", "sato.taro@example.com"))`
    * 複数のイベントをデータベースに登録する。（Day40のコードを再利用）
    * `register_customer_to_event` を使って、異なるイベントに顧客を登録する。
        * 成功するケース
        * 定員オーバーになるケース
        * 二重登録になるケース (UNIQUE制約が働くことを確認)
        * 存在しないイベントIDへの登録ケース
    * `cancel_customer_registration` を使って、登録をキャンセルする。
        * 成功するケース
        * 存在しない顧客IDでのキャンセルケース
        * 存在しないイベントIDでのキャンセルケース
    * **プログラム実行後、DB Browser for SQLite などのツールを使って、`customers` テーブルと `event_registrations` テーブルにデータが正しく登録・更新・削除されていることを目視で確認**してください。

---

**ヒント:**
* `find_event_from_db`で`Event`インスタンスを生成する際、`Event`クラスのコンストラクタは`capacity`が0以下の場合は`ValueError`を発生させます。データベースから取得した`capacity`が常に正の数であることを想定してください。
* `register_customer_to_event`や`cancel_customer_registration`で、データベースから情報を取得する際には、`cursor.execute()`の後に`cursor.fetchone()`や`cursor.fetchall()`を使用します。
* **複合ユニーク制約** (`UNIQUE (event_id, customer_id)`) を設定することで、同じイベントに同じ顧客を重複して登録しようとした場合に、SQLiteが`IntegrityError`を発生させてくれます。これを`try-except`で捕捉し、「既に登録済み」というメッセージを表示するのに利用できます。

今回は、データベースからの検索と、リレーション（関連性）を持つテーブルへのデータの挿入・削除がメインテーマです。頑張ってください！