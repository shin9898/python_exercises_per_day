### ✅ 解答レビュー：Day23 平均年齢の算出

def average_age(users: list[dict]) -> int:
age_list = [user['age'] for user in users]
try:
return round(sum(age_list) / len(age_list))
except TypeError:
print("'age'に整数でないものがあります")

if **name** == '**main**':
users = [
{"name": "Alice", "age": 30},
{"name": "Bob", "age": 24},
{"name": "Charlie", "age": 29}
]
print(average_age(users))

---

### 🧑‍💻 評価ポイント（100 点中）

- **Pythonic な書き方：** 20/20
- **可読性：** 20/20
- **型ヒントの使用：** 20/20
- **例外処理：** 15/20（例外のキャッチは良いが、やや用途がずれている）
- **汎用性・堅牢性：** 15/20（例外処理で`TypeError`を想定しているが、具体的なバリデーションの方が望ましい）

🟩 **総合評価：90 点**

---

### 💡 フィードバック（プロ目線）

- ✅ リスト内包表記を使った`age_list`の生成はとても読みやすく Pythonic です。
- ✅ `round()`で平均を四捨五入している点も、仕様に基づいた良い実装です。
- ⚠️ `try-except`ブロックで`TypeError`をキャッチするより、`age`が整数かどうかを事前に検証する方が堅牢です。
  例：
  ```python
  if not all(isinstance(user['age'], int) for user in users):
      raise ValueError("すべてのユーザーの年齢は整数である必要があります")
  ```
- ⚠️ `except`ブロック内で`print`するだけでは呼び出し元が結果を得られません。例外を上げる（`raise`）方がよい場合もあります。

---

### 🛠️ 改善提案

```python
def average_age(users: list[dict]) -> int:
    if not all(isinstance(user['age'], int) for user in users):
        raise ValueError("すべてのユーザーの年齢は整数である必要があります")
    age_list = [user['age'] for user in users]
    return round(sum(age_list) / len(age_list))
```

この改善により、エラーの原因を明確にしつつ、堅牢な関数になります。

---

素晴らしい取り組みでした！次の問題もお楽しみに 💪
