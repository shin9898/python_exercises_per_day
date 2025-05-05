## 🐍 Python × Django 基礎トレ Day3：ユーザー一覧を整形表示しよう

### 🎯 目的

辞書のリストから特定の形式でユーザー情報を整形して出力できる力を養います。Django のテンプレート処理やデータ整形処理の基礎に繋がります。

---

### 📘 問題

複数のユーザー情報を持つ辞書のリストが与えられます。各ユーザーは `name`（名前）, `email`（メールアドレス）, `is_active`（有効ユーザーかどうか） という 3 つのキーを持っています。

このうち、有効ユーザー（`is_active`が`True`）のみを対象に、次のような文字列のリストを作成してください：

```
"{name}さんのメールアドレスは{email}です"
```

---

### 🔍 入力形式（例）

```python
users = [
    {"name": "Taro", "email": "taro@example.com", "is_active": True},
    {"name": "Hanako", "email": "hanako@example.com", "is_active": False},
    {"name": "Jiro", "email": "jiro@example.com", "is_active": True}
]
```

---

### ✅ 出力（例）

```python
[
    "Taroさんのメールアドレスはtaro@example.comです",
    "Jiroさんのメールアドレスはjiro@example.comです"
]
```

---

### 🧪 テスト用データ（自由に使ってください）

```python
users = [
    {"name": "Miyu", "email": "miyu@example.com", "is_active": True},
    {"name": "Ken", "email": "ken@example.com", "is_active": False},
    {"name": "Sara", "email": "sara@example.com", "is_active": True}
]
```

---

### 💡 ヒント

- リスト内包表記が使えるか挑戦してみましょう。
- `if` を条件に含めることで、有効ユーザーだけを対象にできます。
- Django ではこのような情報をテンプレート内に整形して出す処理が頻出します。
