---

### 📝 Python基礎力強化 - Day40

---

お疲れ様です！Python基礎力強化、Day40です。いよいよ、これまでのオブジェクト指向の知識とデータベース連携を組み合わせる、新たなステップへと進みます。本日からは、SQLiteデータベースを使って、イベント管理システムのデータを永続化することを目指します。

---

### 問題

あなたはイベント企画会社の担当者で、イベント管理システムにデータベース機能を追加します。まずは、データベースの接続と、イベントおよび顧客情報を保存するためのテーブル作成、そして基本的なイベントの登録機能を実装します。

以下の要件を満たすPythonコードを記述してください。

1.  **前回までに作成した `Customer` クラスと `Event` クラスを再利用または定義**してください。
    * （Day39で完成させたコードをベースにしてください。エラーハンドリングもそのまま活用してください。）
    * 今回の課題では、`Event`クラスの`registered_customers`リストは一時的に使用しません。（データベースで管理するため）

2.  **`EventManager` クラスを修正し、以下のデータベース連携機能を追加**してください。

    * **属性の追加:**
        * `self.db_name: str`：データベースファイルの名前を保持する属性。`__init__`で引数として受け取るか、デフォルト値として`'events.db'`を設定する。
        * `self.conn: sqlite3.Connection | None`：データベース接続オブジェクトを保持する属性。初期値は`None`。
        * `self.cursor: sqlite3.Cursor | None`：カーソルオブジェクトを保持する属性。初期値は`None`。

    * **メソッドの追加:**
        * `__init__(self, db_name='events.db')`:
            * 既存の初期化処理 (`self.events = []`, `self.events_by_id = {}`) に加えて、`self.db_name`を設定する。
            * **データベースへの接続はここで行わないでください。** 接続と切断は専用のメソッドで行います。
        * `connect_db(self) -> None`:
            * `sqlite3.connect(self.db_name)` を使ってデータベースに接続し、`self.conn` に代入する。
            * `self.conn.cursor()` を使ってカーソルオブジェクトを作成し、`self.cursor` に代入する。
            * **`self.conn.execute('PRAGMA foreign_keys = ON')` を実行して、外部キー制約を有効にする。** (これは`Event`と`Customer`の関連を適切に管理するために重要です。)
            * データベース接続が成功したら、"データベースに接続しました: [db_name]" と表示する。
            * 接続中にエラーが発生した場合 (`sqlite3.Error` を捕捉)、"データベース接続エラー: [エラーメッセージ]" と表示する。
        * `close_db(self) -> None`:
            * `self.conn.close()` を使ってデータベース接続を閉じる。
            * 接続が成功したら、"データベース接続を閉じました。" と表示する。
            * 切断中にエラーが発生した場合 (`sqlite3.Error` を捕捉)、"データベース切断エラー: [エラーメッセージ]" と表示する。
        * `create_tables(self) -> None`:
            * **`events` テーブルを作成するSQL文を実行する。**
                * テーブル名: `events`
                * カラム:
                    * `event_id TEXT PRIMARY KEY`: イベントID (主キー)
                    * `title TEXT NOT NULL`: タイトル
                    * `date TEXT NOT NULL`: 日付
                    * `capacity INTEGER NOT NULL`: 定員
            * **`customers` テーブルを作成するSQL文を実行する。**
                * テーブル名: `customers`
                * カラム:
                    * `customer_id TEXT PRIMARY KEY`: 顧客ID (主キー)
                    * `name TEXT NOT NULL`: 名前
                    * `email TEXT NOT NULL`: メールアドレス
            * テーブル作成が成功したら、"テーブルを正常に作成しました。" と表示する。
            * エラーが発生した場合 (`sqlite3.Error` を捕捉)、"テーブル作成エラー: [エラーメッセージ]" と表示する。

3.  **`EventManager.add_event(self, event: Event)` メソッドを修正**してください。
    * **イベントをデータベースに登録する**ように変更する。
    * 既存の型チェックや重複チェック（`event.event_id in self.events_by_id`）はそのまま活用する。
    * データベースへの登録は `INSERT INTO events (...) VALUES (...)` SQL文を使用する。
    * 登録が成功したら、`self.conn.commit()` を実行して変更を確定する。
    * データベース登録中にエラーが発生した場合 (`sqlite3.Error` を捕捉)、"イベント『[タイトル]』のデータベース登録に失敗しました: [エラーメッセージ]" と表示する。

4.  `__main__` ブロックで以下の処理を実行し、動作を確認してください。

    * `EventManager` のインスタンスを作成する。
    * **`event_manager.connect_db()` を呼び出し、データベースに接続する。**
    * **`event_manager.create_tables()` を呼び出し、テーブルを作成する。** (初回実行時のみ作成されるように、既存チェックを考慮しても良い)
    * 複数の `Event` インスタンスを作成する。
    * `event_manager.add_event()` を使って、これらのイベントを**データベースに登録**する。（重複イベントも試す）
    * **`event_manager.close_db()` を呼び出し、データベース接続を閉じる。**
    * プログラム実行後、**DB Browser for SQLite などのツールを使って、作成された `.db` ファイルを開き、`events` テーブルにデータが正しく登録されていることを目視で確認**してください。

---

**ヒント:**
* `sqlite3` モジュールの基本的な使い方は、公式ドキュメントやオンラインのリソースを参照してください。
* SQL文の実行には `self.cursor.execute(sql_query, (parameters,))` の形式を使用します。パラメータはタプルで渡すことで、SQLインジェクションのリスクを減らせます。
* `self.conn.commit()` は、`INSERT`や`UPDATE`、`DELETE`などの変更をデータベースに永続的に保存するために必要です。
* `PRAGMA foreign_keys = ON` は、テーブル作成後、実際のデータ挿入前に一度だけ実行することで、外部キー制約が機能するようになります。

今回はデータベースとの「接続」「テーブル作成」「データ挿入」の基礎を固めるステップです。頑張ってください！