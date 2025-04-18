# Day7: ユーザー予約管理システム

## 問題文

ある Web アプリケーションで、ユーザーがイベントの予約を行えるシステムを構築したいと考えています。
以下の要件を満たすクラスと処理を実装してください。

### 要件

- `Reservation` クラスを定義してください：
  - 各予約は `user_name`（予約者名）、`event_name`（イベント名）、`date`（予約日：`YYYY-MM-DD`形式）を持ちます
- `ReservationManager` クラスを定義してください：
  - 予約を追加する `add_reservation(reservation: Reservation)` メソッドを持つ
  - ユーザー名で予約を検索する `find_by_user(user_name: str) -> list[Reservation]` を実装する
  - 日付ごとの予約数をカウントし、`get_reservation_count_by_date() -> dict[str, int]` を返す

## 制約・条件

- 日付の文字列を処理するために `datetime` ライブラリの使用を推奨します（ただしバリデーションは任意）
- 型ヒントは必ず記述してください
- 出力チェック用に、テストデータをいくつか登録して、検索・集計結果を `print()` してください

## 実行例

```python
# 期待される出力例（出力順は問わない）
# print(manager.find_by_user("Alice"))
# => [Reservation(user_name="Alice", event_name="Yoga", date="2025-05-01")]
# print(manager.get_reservation_count_by_date())
# => {"2025-05-01": 2, "2025-05-02": 1}
```

## ヒント

- `__repr__` をオーバーライドして、Reservation オブジェクトの中身を見やすくしておくと便利です
- 集計には `collections.defaultdict` や `Counter` が役立ちます

---

## 実装のスタートポイント

以下のコードをベースに、自分でクラス・関数・型ヒントをすべて記述してください：

```python
if __name__ == "__main__":
    # テストデータ登録
    manager = ReservationManager()
    manager.add_reservation(Reservation("Alice", "Yoga", "2025-05-01"))
    manager.add_reservation(Reservation("Bob", "Yoga", "2025-05-01"))
    manager.add_reservation(Reservation("Charlie", "Dance", "2025-05-02"))

    # 検索・集計処理
    print(manager.find_by_user("Alice"))
    print(manager.get_reservation_count_by_date())
```
