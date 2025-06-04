---

### 📝 Python基礎力強化 - Day39

---

お疲れ様です！Python基礎力強化、Day39です。前回までのフィードバックを元に、ご自身のコードをさらに改善しようとする姿勢、素晴らしいです。ソート漏れのご指摘や、タプル戻り値の扱いの確認など、細部へのこだわりがプロの仕事に繋がります。

**今回の問題が、「Python基礎力強化」シリーズの本当に最後の問題となります。** これまで学習してきた全ての要素、特に**エラーハンドリング（例外処理）**に焦点を当てます。予期せぬ入力や、プログラムの想定外の動作に対して、いかに適切に対応し、ユーザーに分かりやすいメッセージを返すか、という部分は実務で非常に重要です。

---

### 問題

あなたは引き続きイベント企画会社の担当者で、これまでのシステムに**堅牢なエラーハンドリング**を追加します。これにより、不正なデータ入力や存在しないIDの指定があった場合でも、プログラムがクラッシュせず、ユーザーに適切なフィードバックを提供できるようにします。

以下の要件を満たすPythonコードを記述してください。

1.  **前回までに作成した `Customer` クラス、`Event` クラス、`EventManager` クラスを再利用または定義**してください。
    * （Day38で完成させたコードをベースにしてください。特に、`Event.register_customer`メソッドのタプル戻り値の扱いを修正してください。）

2.  以下の各メソッドに**エラーハンドリング（`try-except`ブロック）**を追加し、問題文の指示に従って適切な例外を発生させるか、メッセージを表示してください。

    * **`Event` クラス**
        * `__init__(self, event_id, title, date, capacity)`:
            * `capacity` が**0以下の整数**である場合、`ValueError` を発生させる。メッセージは `"定員は1以上の整数である必要があります。"`
        * `register_customer(self, customer: Customer)`:
            * 引数 `customer` が `Customer` クラスのインスタンスでない場合、`TypeError` を発生させる。メッセージは `"登録しようとしているオブジェクトはCustomerクラスのインスタンスではありません。" `
            * （これらは既存の型チェックを`try-except`で囲むか、より適切に修正してください。）
        * `cancel_registration(self, customer_id: str)`:
            * `customer_id` が空文字列の場合、`ValueError` を発生させる。メッセージは`"顧客IDは空にできません。"`

    * **`EventManager` クラス**
        * `add_event(self, event: Event)`:
            * 引数 `event` が `Event` クラスのインスタンスでない場合、`TypeError` を発生させる。メッセージは `"追加しようとしているオブジェクトはEventクラスのインスタンスではありません。" `
            * （これも既存の型チェックを修正してください。）
        * `register_customer_to_event(self, customer: Customer, event_id: str)`:
            * 引数 `customer` が `Customer` クラスのインスタンスでない場合、`TypeError` を発生させる。メッセージは `"登録しようとしているオブジェクトはCustomerクラスのインスタンスではありません。" `
            * `event_id` が空文字列の場合、`ValueError` を発生させる。メッセージは `"イベントIDは空にできません。"`
            * **`find_event` が `None` を返した場合（イベントが見つからない場合）は、`print`文で `"イベントID『[ID]』のイベントは見つかりませんでした。"` と表示するだけで、例外は発生させないでください。**
        * `cancel_customer_registration(self, customer_id: str, event_id: str)`:
            * `customer_id` が空文字列の場合、`ValueError` を発生させる。メッセージは`"顧客IDは空にできません。"`
            * `event_id` が空文字列の場合、`ValueError` を発生させる。メッセージは `"イベントIDは空にできません。"`
            * **`find_event` が `None` を返した場合（イベントが見つからない場合）は、`print`文で `"イベントID『[ID]』のイベントは見つかりませんでした。"` と表示するだけで、例外は発生させないでください。**

3.  `__main__` ブロックで以下の処理を実行し、**エラーハンドリングが正しく機能することを確認**してください。

    * `Event` インスタンスを作成する際に、`capacity` に**不正な値（0以下）**を渡してみて、`ValueError` が発生することを確認する。
        ```python
        print("\n--- Event容量不正テスト ---")
        try:
            invalid_event = Event("EVT999", "不正容量イベント", "2025-12-31", 0) # 定員0
        except ValueError as e:
            print(f"エラー捕捉: {e}")

        try:
            invalid_event2 = Event("EVT998", "不正容量イベント2", "2025-12-31", -5) # 定員負数
        except ValueError as e:
            print(f"エラー捕捉: {e}")
        ```
    * `EventManager.add_event` で、`Event` インスタンスではない**不正な型（例: 文字列や数値）**を渡してみて、`TypeError` が発生することを確認する。
        ```python
        print("\n--- add_event 型不正テスト ---")
        try:
            event_manager.add_event("これはイベントではありません")
        except TypeError as e:
            print(f"エラー捕捉: {e}")
        ```
    * `EventManager.register_customer_to_event` で、`customer` に**不正な型**を渡してみて、`TypeError` が発生することを確認する。
        ```python
        print("\n--- register_customer_to_event 型不正テスト ---")
        try:
            event_manager.register_customer_to_event("これは顧客ではありません", "EVT001")
        except TypeError as e:
            print(f"エラー捕捉: {e}")
        ```
    * `EventManager.register_customer_to_event` や `cancel_customer_registration` で、`event_id` や `customer_id` に**空文字列**を渡してみて、`ValueError` が発生することを確認する。
        ```python
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
        ```

    * （これまでの正常系のテストケースは引き続き実行し、全ての機能がエラーハンドリング追加後も問題なく動作することを確認してください。）

---

**ヒント:**
* `raise` キーワードを使って例外を発生させます。
* `try-except`ブロックは、予期しないエラーを捕捉するために使用します。今回は、メソッドの内部で不正な値が検出された場合に**「誰が」そのエラーを処理すべきか**を考え、適切な箇所で`raise`を使用してください。
* `TypeError`は、引数の型が間違っている場合に使うのが一般的です。
* `ValueError`は、引数の値が不正な場合に使うのが一般的です。
