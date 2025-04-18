# Day7 解説

## ✅ 実装内容チェック

あなたの提出された解答を確認しました。以下の点が正しく実装されています：

- ✅ `Reservation` クラスに `user_name`, `event_name`, `date` の属性が正しく実装されている
- ✅ `ReservationManager` クラスに予約追加・検索・日付集計の 3 機能が正しく実装されている
- ✅ `__repr__` のオーバーライドで見やすい出力形式になっている
- ✅ `Counter` を用いた日付ごとの予約数のカウント処理が行われている
- ✅ テストデータと出力が要件通りに実行されている

Good Job!! 🎉

---

## 🛠 改善ポイント・アドバイス

### 1. クラス継承の見直し

`ReservationManager` が `Reservation` を継承していますが、これは意図しない設計です。
`ReservationManager` は予約情報の管理者であり、予約そのもの（`Reservation`）とは関係がないため、継承ではなく**コンポジション（has-a 関係）**が適切です。

```python
class ReservationManager:
    def __init__(self):
        self.reservation_list = []
```

---

### 2. 型ヒントの活用

戻り値の型ヒントやリストの型についても明示されており良い点です。さらに以下のように、PEP484 に従って `from typing import List` を使う記述も知っておくと柔軟性が広がります。

```python
from typing import List

def find_by_user(self, user_name: str) -> List[Reservation]:
```

Python3.9 以降は `list[Reservation]` でも OK ですが、チーム開発やライブラリ互換性を意識する場合は `List[...]` を使う場面も多くあります。

---

### 3. `find_by_user` の返り値について

現在は `repr()` 文字列のリストを返していますが、可能であれば Reservation オブジェクトのまま返す方が汎用性があります。表示用に文字列化するのは `print()` 側で行うのが理想的です。

```python
def find_by_user(self, user_name: str) -> list[Reservation]:
    return [r for r in self.reservation_list if r.user_name == user_name]

# 呼び出し側
print([repr(r) for r in manager.find_by_user("Alice")])
```

---

## 🧪 模範解答（サンプルコード）

```python
from collections import Counter

class Reservation:
    def __init__(self, user_name: str, event_name: str, date: str):
        self.user_name = user_name
        self.event_name = event_name
        self.date = date

    def __repr__(self):
        return f"Reservation(user_name='{self.user_name}', event_name='{self.event_name}', date='{self.date}')"

class ReservationManager:
    def __init__(self):
        self.reservation_list: list[Reservation] = []

    def add_reservation(self, reservation: Reservation):
        self.reservation_list.append(reservation)

    def find_by_user(self, user_name: str) -> list[Reservation]:
        return [r for r in self.reservation_list if r.user_name == user_name]

    def get_reservation_count_by_date(self) -> dict[str, int]:
        return dict(Counter(r.date for r in self.reservation_list))

if __name__ == "__main__":
    manager = ReservationManager()
    manager.add_reservation(Reservation("Alice", "Yoga", "2025-05-01"))
    manager.add_reservation(Reservation("Bob", "Yoga", "2025-05-01"))
    manager.add_reservation(Reservation("Charlie", "Dance", "2025-05-02"))

    print([repr(r) for r in manager.find_by_user("Alice")])
    print(manager.get_reservation_count_by_date())
```

---

## 総評

Day7 では**複数クラスの設計・連携によるデータ管理**という、より実践的なスキルが求められました。
あなたの実装は非常に堅実で、ロジックも明瞭、型ヒントやテストケースにも抜かりがありませんでした！

今後は、**入力値のバリデーション**や**例外処理**、**集計・ソート処理の応用**なども取り入れていくと、さらに実務力が高まっていきます。

お疲れさまでした！次回もがんばりましょう！🔥
