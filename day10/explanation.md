# Day10 解説

## ✅ 実装内容チェック

あなたの提出された解答を確認しました。以下の点が正しく実装されています：

- ✅ `Player` クラスの `name` と `score` 属性の定義が適切
- ✅ `ScoreManager` クラスにて、プレイヤーの追加・トップスコアの取得・平均スコアの計算が正しく実装されている
- ✅ リスト内包表記や `max()`、`round()` の使用が適切
- ✅ テスト実行の出力が期待通り：`"Alice"` および `91.33`

Excellent Work!! 🎯

---

## 🛠 改善ポイント・アドバイス

### 1. 平均スコアの型ヒント

```python
 def get_average_score(self) -> int:
```

となっていましたが、平均スコアは小数点以下も扱うため、正確には `-> float` が望ましいです：

```python
 def get_average_score(self) -> float:
```

---

## 🧪 模範解答（サンプルコード）

```python
class Player:
    def __init__(self, name: str, score: int):
        self.name = name
        self.score = score

class ScoreManager:
    def __init__(self):
        self.players_list: list[Player] = []

    def add_player(self, player: Player) -> None:
        self.players_list.append(player)

    def get_top_scorer(self) -> str:
        top_scorer = max(self.players_list, key=lambda player: player.score)
        return top_scorer.name

    def get_average_score(self) -> float:
        scores = [player.score for player in self.players_list]
        return round(sum(scores) / len(scores), 2)

if __name__ == "__main__":
    manager = ScoreManager()
    manager.add_player(Player("Alice", 95))
    manager.add_player(Player("Bob", 87))
    manager.add_player(Player("Charlie", 92))

    print(manager.get_top_scorer())  # => "Alice"
    print(manager.get_average_score())  # => 91.33
```

---

## 総評

Day10 では**スコアの最大値・平均値計算**という、実務にもよく出る集計系の処理がテーマでした。構文や関数の選定もよく、非常に良い解答でした！

次回 Day11 では、**ネストされたデータ構造や条件分岐の強化**など、さらに一歩進んだ実装問題を出題予定です。

引き続き、頑張っていきましょう！🔥
