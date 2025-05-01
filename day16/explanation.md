## ✅ Day16 解答コードレビュー & 標準解答

---

### 🔍 解いた問題の概要

**目的：**  
数列における「連続する部分配列の積」の最大値を求める。

---

### 📆 提出コード

```python
def maximum_of_the_product(arr: int, num_list: list[int]) -> int:
    result = 0
    for i in range(arr):
        if i == 0:
            result += num_list[i]
        else:
            result *= num_list[i]
    return abs(result)

if __name__ == '__main__':
    arr = int(input())
    num_list = list(map(int, input().split()))
    print(maximum_of_the_product(arr, num_list))
```

---

### 🔎 コードレビュー

#### ✅ 良かった点

- 入出力の受け方にミスがなく、Python の基本構文を正しく使えている
- `abs()` を用いて正負の考慮をしようとしている点は良い覚え

#### ⚠️ 問題点

- このコードは「**全体の積**の等等の第 1 要素を加算、その後に積を続けている」にすぎず、「**すべての部分配列の積**の中で最大値を探す」という要件を満たせていない
- たまた正しく出力されるケースもあるが、「問題の意図に合わない」ので要修正

---

### 🌟 標準解答 (DP による実装)

```python
def maximum_of_the_product(n: int, arr: list[int]) -> int:
    max_prod = arr[0]
    current_max = arr[0]
    current_min = arr[0]

    for i in range(1, n):
        num = arr[i]
        if num < 0:
            current_max, current_min = current_min, current_max
        current_max = max(num, current_max * num)
        current_min = min(num, current_min * num)
        max_prod = max(max_prod, current_max)

    return max_prod

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(maximum_of_the_product(n, arr))
```

#### 💡 ポイント

- **負数の反転対応：** 負の数をかけると max/min が交互する
- **0 の扱い：** `max(num, current_max * num)` として、分裂し直列を再スタート
- **max 値更新：** 各部分配列が終わるたびに最大値を続次更新

---

### ✨ 評価 (100 点満点中)

| 評価基準             | 評価    |
| -------------------- | ------- |
| Pythonic な書き方    | 15 / 20 |
| 可読性               | 12 / 20 |
| 型ヒントの記述       | 20 / 20 |
| 入力条件の綱管       | 10 / 20 |
| アルゴリズムの正確性 | 5 / 20  |

### 総合評価：【62 / 100 点】

---

### 🔄 次のステップ

- ① 「区間積」問題には DP の思考が有效
- ② 負数や 0 のオフセット変更を同時に考慮
- ③ 標準解答を手を動かしてトレースすること

---

以上で Day16 の解答レビューは終了です！ご期待の Day17 の問題も準備中です ♪
