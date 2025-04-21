# Day10 問題文

## 📓 内容

あなたはゲームマネージャーとして、プレイヤーのスコアを管理するシステムを開発します。以下の条件を満たす `Player` クラスと `ScoreManager` クラスを実装してください。

- `Player` は名前 (`name`: str) とスコア (`score`: int) を持つ
- `ScoreManager` は複数の Player を管理し、以下の操作を提供する:
  - プレイヤーの追加 (`add_player(player: Player)`)
  - 最高点のプレイヤーを検索 (`get_top_scorer()`)
  - 平均点を返す (`get_average_score()`)

## 🔧 条件

- Python のコードスタイルのベストプラクティスを意識しましょう
- 型ヒントはしっかりつけましょう
- 不正な引数やスコアがない場合は例外を投げましょう

## 🧪 目的

- クラスの組合せと専用粒度
- ステートを持つクラスの定義方式
- 数値操作の基礎と例外処理

---

## 🧰 テストコード例

```python
if __name__ == "__main__":
    manager = ScoreManager()
    manager.add_player(Player("Alice", 95))
    manager.add_player(Player("Bob", 87))
    manager.add_player(Player("Charlie", 92))

    print(manager.get_top_scorer())  # => "Alice"
    print(manager.get_average_score())  # => 91.33
```
