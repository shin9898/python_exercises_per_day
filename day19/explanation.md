## ✅ Day20 解答レビュー：有効ユーザー情報の抽出と整形

### 🔍 解答コード

```python
def validity_check(users: list[dict]) -> list[str]:
    return [f"{user['name']}さんのメールアドレスは{user['email']}です" for user in users if user['is_active']]


if __name__ == '__main__':
    users = [
        {"name": "Miyu", "email": "miyu@example.com", "is_active": True},
        {"name": "Ken", "email": "ken@example.com", "is_active": False},
        {"name": "Sara", "email": "sara@example.com", "is_active": True}
    ]

    print(validity_check(users))
```

---

### ✅ 総合評価：**98 点 / 100 点**

### ✨ 評価ポイント

| 観点                 | 評価        | コメント                                             |
| -------------------- | ----------- | ---------------------------------------------------- |
| Pythonic な書き方    | ✅ 優秀     | リスト内包表記が適切に使われており、非常に簡潔です。 |
| 可読性               | ✅ 良好     | フォーマット文字列もわかりやすく、読みやすいです。   |
| 型ヒントの使用       | ✅ 明記済   | 関数引数・戻り値に正しく型ヒントが書かれています。   |
| 入力条件への対応     | ✅ 完全対応 | `is_active`の真偽値を適切に判定しています。          |
| 再利用性（汎用性）   | ✅ 高い     | 関数がデータに依存せず汎用的に使えます。             |
| 出力結果と想定の一致 | ✅ 完全一致 | 出力が問題例と一致。                                 |
| 追加点：テストの有無 | ❌ やや不足 | `assert` などによるテストがあればなお良し。          |

---

### 🧠 解説（プロ目線）

このコードは、辞書のリストから`is_active`が`True`の要素のみを抽出し、特定の形式の文字列に変換してリストとして返すという非常に典型的な「情報の整形」処理です。

#### ✅ 技術的に良い点：

- **リスト内包表記**で簡潔に記述されており、パフォーマンス・可読性ともに優れています。
- **フォーマット済み文字列（f-string）** の使用により直感的なコードになっています。
- **関数化**されているため、再利用可能でテストもしやすくなっています。

#### 🛠 改善点を挙げるなら：

- 本格的なアプリケーション開発では**入力検証**や**例外処理**が必要になる場面もあります。
- **ユニットテスト関数（例：`test_validity_check()`）** を追加しておくと、拡張性・保守性がさらに向上します。

---

### ✅ 模範テストコードの提案

```python
def test_validity_check():
    users = [
        {"name": "Miyu", "email": "miyu@example.com", "is_active": True},
        {"name": "Ken", "email": "ken@example.com", "is_active": False},
        {"name": "Sara", "email": "sara@example.com", "is_active": True}
    ]
    expected = [
        "Miyuさんのメールアドレスはmiyu@example.comです",
        "Saraさんのメールアドレスはsara@example.comです"
    ]
    assert validity_check(users) == expected
    print("✅ test_validity_check PASSED")
```

---

### 💡 この問題の学習ポイント

- Django のテンプレート出力やフィルタ処理でよく使う「条件付きリスト抽出」と「文字列整形」の基礎を固める演習。
- 「データの整形・出力処理」は Web 開発の全ステップで登場する重要スキルです。

---

次回もこのような実務で役立つパターンを踏まえて出題していきます！
