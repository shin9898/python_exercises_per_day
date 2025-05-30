## 🧠 Day17：辞書とリストの基本操作（Django に必要なデータ構造）

### 📘 問題概要

Django でよく使われるデータ構造である「辞書（dict）」と「リスト（list）」の基本操作を学ぶための練習問題です。以下の仕様に沿って、辞書とリストを活用してデータを加工する関数を実装してください。

### 🔧 要件

次の仕様に従う関数 `format_user_data(users: list[dict]) -> list[str]` を作成してください：

- `users` はユーザー情報を格納した辞書のリストです。
- 各ユーザー情報の辞書には、`"name"`（名前）と `"age"`（年齢）のキーが含まれます。
- 各ユーザーに対し、次の形式の文字列を作成してください：
  - `"{名前}さんは{年齢}歳です"`
- 最終的に、すべてのユーザーについて上記形式の文字列のリストを返してください。

### 🔍 入力例

```python
users = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 24},
    {"name": "Charlie", "age": 29}
]
```

### ✅ 出力例

```python
["Aliceさんは30歳です", "Bobさんは24歳です", "Charlieさんは29歳です"]
```

---

### 💡 ヒント

- Django のビューやシリアライザーでは、辞書形式でやりとりすることが多くあります。
- f 文字列（f"{name}さんは{age}歳です"）を活用すると簡潔に書けます。

---

### 📥 入力制約

- `users` は最大 100 件までとします。
- 各ユーザーの `name` は 1〜20 文字の英字、`age` は整数（0〜120）とします。

---

### 🧪 テスト用コード（任意で活用してください）

```python
def test():
    users = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 24},
        {"name": "Charlie", "age": 29}
    ]
    expected = ["Aliceさんは30歳です", "Bobさんは24歳です", "Charlieさんは29歳です"]
    assert format_user_data(users) == expected
    print("✅ テスト通過！")
```
