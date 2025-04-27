## ✅ Day15 解答コードレビュー & 解説

---

### 🔍 コードの目的

昇順に並んだリストから、隣接して同じ値が連続する部分をまとめてカウントし、異なる値が現れたときだけカウントすることで「異なる要素の数」を求める処理。

---

### 📄 あなたの提出コード

```python
number_of_digit = int(input())
num_list = list(map(int, input().split()))

duplicate_num_list = []
for i in range(number_of_digit):
    if i == 0:
        duplicate_num_list.append(i)
    elif num_list[i] == num_list[i - 1]:
        continue
    else:
        duplicate_num_list.append(i)

print(len(duplicate_num_list))
```

---

### 📊 コードの分析

#### ✅ 良い点：

- **隣り合う要素だけを比較する**シンプルなロジックができている
- **初回のみ無条件でカウント**し、その後、**直前の要素と同じならスキップ**という発想は正しい
- **Python の基本文法**（リスト、ループ、条件分岐）が適切に使われている

#### 🔧 改善ポイント：

- `duplicate_num_list` に **インデックス（i）を append** しているが、必要なのは数のカウントなので、`count` を直接増やすだけでもよい
- 変数名が少し分かりづらい（`duplicate_num_list` だと重複リストっぽく感じる）
- 実際にはリストを作る必要はないので、**単純なカウント変数**だけで十分

---

### 📄 模範回答例

```python
def count_unique_numbers(num_list: list[int]) -> int:
    count = 1
    for i in range(1, len(num_list)):
        if num_list[i] != num_list[i - 1]:
            count += 1
    return count

if __name__ == '__main__':
    number_of_digit = int(input())
    num_list = list(map(int, input().split()))
    print(count_unique_numbers(num_list))
```

---

### 📊 入力例の検証

| 入力           | 期待出力 | 結果  |
| -------------- | -------- | ----- |
| 5\n1 1 2 2 3   | 3        | OK ✅ |
| 6\n1 1 1 1 1 1 | 1        | OK ✅ |
| 4\n1 2 3 4     | 4        | OK ✅ |

問題なく期待通りの動作が確認されました！

---

### ✨ 総評と評価

#### 総合得点：**92 / 100 点**

#### ✅ 評価基準別チェック：

- ✅ **Pythonic な書き方**：基本的には問題なし。ただし少し最適化できる
- ✅ **可読性**：やや改善余地あり（変数名、無駄なリスト作成）
- ✅ **型ヒント**：模範解答では付与（オリジナルコードでは無し）
- ✅ **入力条件対応力**：OK（例外ケースも想定できる）
- ⬜️ **最適化意識**：リスト作成不要な場面で作成しているのでやや減点

---

🎉 よくできています！

- ループ + 条件分岐の基本パターンが身についてきています。
- 次のステップとして「不要な変数を省く」「カウントだけする」といった **シンプルに書く意識** を持つと、さらにレベルアップできます！

---

🚀 次回予告：
「連続する要素のまとまりごとに、まとめたリストを作成する」など、さらに応用問題に挑戦していきましょう！
