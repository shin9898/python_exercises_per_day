---

### 📝 Python基礎力強化 - Day36

---

お疲れ様です！Python基礎力強化、いよいよDay36です。前回はコンポジションの問題で見事なコードを完成させ、プロレベルのスキルを証明してくれました。特に、高速検索のための辞書の利用や正規表現の導入など、自主的な改善が光っていました。

いよいよ今回の問題で、**「Python基礎力強化」の最終章**となります。これまでの学習で培った、データ構造の操作、関数、オブジェクト指向（クラス、コンポジション）の知識を総動員していただく、集大成となる問題です。

今回の課題をクリアすれば、Pythonの基礎は完全に盤石となり、Djangoの学習へと自信を持って進むことができます。

---

### 問題

あなたはとあるイベント企画会社の担当者で、複数のイベントとそれに参加する顧客の情報を管理するシステムを開発しています。

以下の要件を満たすPythonコードを記述してください。

1.  **`Customer` クラスを定義**してください。
    * 属性: `customer_id` (文字列、一意), `name` (文字列), `email` (文字列)
    * メソッド: `__init__`, `display_info` (顧客ID、名前、メールアドレスを表示)

2.  **`Event` クラスを定義**してください。
    * 属性: `event_id` (文字列、一意), `title` (文字列), `date` (文字列、例: "YYYY-MM-DD"), `capacity` (整数、最大参加人数), `registered_customers` (リスト、初期値は空のリスト)
    * メソッド:
        * `__init__`: コンストラクタ。
        * `register_customer(self, customer: Customer)`:
            * 引数として `Customer` クラスのインスタンスを受け取ります。
            * イベントの定員 (`capacity`) に達していない、かつ、その顧客がまだ登録されていない場合に、`registered_customers` リストに顧客の `customer_id` を追加します。
            * 登録に成功したら、"『[イベントタイトル]』に顧客『[顧客名]』が登録されました。" と表示し、`True` を返す。
            * 定員オーバーの場合、"『[イベントタイトル]』は定員に達しています。" と表示し、`False` を返す。
            * 既に登録済みの場合、"顧客『[顧客名]』は既に『[イベントタイトル]』に登録済みです。" と表示し、`False` を返す。
        * `cancel_registration(self, customer_id: str)`:
            * 引数として `customer_id` を受け取ります。
            * `registered_customers` リストに該当の `customer_id` が存在する場合、そのIDをリストから削除します。
            * キャンセルに成功したら、"『[イベントタイトル]』から顧客ID『[顧客ID]』の登録がキャンセルされました。" と表示し、`True` を返す。
            * 該当の `customer_id` が見つからない場合、"顧客ID『[顧客ID]』は『[イベントタイトル]』に登録されていません。" と表示し、`False` を返す。
        * `get_registered_count(self)`:
            * 現在登録されている顧客の人数を返す。
        * `display_event_info(self)`:
            * イベントのタイトル、日付、定員、現在の登録人数を表示する。

3.  **`EventManager` クラスを定義**してください。
    * このクラスは、イベントのリストを保持するための属性 `events` を持つ必要があります。初期値は空のリストとします。
    * 内部でイベントを `event_id` で効率的に検索できるよう、辞書 (`events_by_id`) も属性として持たせると良いでしょう。

4.  `EventManager` クラス内に以下の**メソッドを定義**してください。
    * `__init__(self)`: コンストラクタ。`events` リストと `events_by_id` 辞書を初期化します。
    * `add_event(self, event: Event)`:
        * 引数として `Event` クラスのインスタンスを受け取り、`events` リストと `events_by_id` 辞書に追加します。
        * 既に同じ `event_id` のイベントが登録されている場合は追加せず、「警告: イベントID『[ID]』のイベントは既に登録されています。」と表示する。
        * 成功したら、"イベント『[イベントタイトル]』が追加されました。" と表示する。
    * `find_event(self, event_id: str) -> Event | None`:
        * 引数 `event_id` (文字列) を受け取り、該当する `Event` インスタンスを返します。
        * 見つからなければ `None` を返す。（前回の `_get_book_by_isbn` のようにヘルパーメソッドとして実装し、`register_customer_to_event` などで内部的に使うと良いでしょう）
    * `register_customer_to_event(self, customer: Customer, event_id: str)`:
        * 引数として `Customer` インスタンスと `event_id` を受け取ります。
        * まず `event_id` でイベントを検索し、見つかったらそのイベントの `register_customer` メソッドを呼び出します。
        * イベントが見つからない場合は、"イベントID『[ID]』のイベントは見つかりませんでした。" と表示する。
    * `cancel_customer_registration(self, customer_id: str, event_id: str)`:
        * 引数として `customer_id` と `event_id` を受け取ります。
        * `event_id` でイベントを検索し、見つかったらそのイベントの `cancel_registration` メソッドを呼び出します。
        * イベントが見つからない場合は、"イベントID『[ID]』のイベントは見つかりませんでした。" と表示する。
    * `display_all_events_summary(self)`:
        * 登録されている全てのイベントのタイトル、日付、現在の登録人数、定員を表示する。
        * イベントが一つもない場合は、"現在、登録されているイベントはありません。" と表示する。
        * 表示は、イベントタイトルで**昇順**にソートして表示する。

5.  `__main__` ブロックで以下の処理を実行し、動作を確認してください。
    * `EventManager` のインスタンスを作成する。
    * 複数の `Customer` インスタンスと `Event` インスタンスを作成する。
    * `add_event` でイベントを `EventManager` に追加する。
    * `display_all_events_summary` で初期状態を確認する。
    * `register_customer_to_event` を使って、異なるイベントに顧客を登録する。定員オーバーや二重登録のケースも試す。
    * 登録後、`display_all_events_summary` で登録人数が更新されたことを確認する。
    * `cancel_customer_registration` を使って、登録をキャンセルする。存在しない顧客IDでのキャンセルも試す。
    * キャンセル後、`display_all_events_summary` で登録人数が更新されたことを確認する。

---

この問題では、複数のクラス (`Customer`, `Event`, `EventManager`) が連携し、それぞれが持つ属性やメソッドを相互に利用することで、複雑なシステムを構築します。特に、**`Event` が `Customer` のIDを管理し、`EventManager` が `Event` オブジェクトを管理する**という「Has-A」関係の多層的な理解が問われます。

これができれば、Pythonでのオブジェクト指向プログラミングの基礎は完璧です。
