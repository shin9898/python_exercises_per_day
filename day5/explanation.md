# Day5 解説

## ✅ 実装内容チェック

あなたのコードは以下の要件を正しく満たしています：

- ✅ `sample.txt` を読み込んでいる
- ✅ 単語の区切りにスペースを使用している
- ✅ 小文字変換（`lower()`）を行っている
- ✅ `Counter` で出現回数を数えている
- ✅ 上位 5 件を出力している

とても丁寧に書けていて、**読みやすさ・正確さともに良好**です！🎉

---

## 🛠 改善ポイント・アドバイス

### 1. `while True` + `readline()` の代わりに `for line in f` を使う

Python ではファイルを 1 行ずつ読むには `for line in f:` を使うのが一般的です。よりシンプルで Pythonic になります。

```python
with open(filename, 'r', encoding="utf-8") as f:
    for line in f:
        word_list = line.lower().split()
        word_list_counter.extend(word_list)
```

### 2. `rstrip("\n")` は不要

`split()` を使うだけで改行も自然に無視されるため、`rstrip("\n")` は省略できます。

### 3. 出力順の保証

現状、Counter の `.items()` を使ってループしていますが、これは順序が保証されません。

```python
for word, count in result_dict.most_common(5):
    print(f"{word}: {count}")
```

とすることで、「出現数順に上位 5 件を正確に表示」できます。

---

## 🧪 模範解答（サンプルコード）

```python
from collections import Counter

def count_words(filename: str) -> None:
    word_list_counter = []
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            word_list = line.lower().split()
            word_list_counter.extend(word_list)

    result_dict = Counter(word_list_counter)
    for word, count in result_dict.most_common(5):
        print(f"{word}: {count}")

if __name__ == "__main__":
    count_words("sample.txt")
```

---

## 総評

非常に良いです！Day5 の締めとして、**ファイル操作・文字列操作・データ集計の基本をきっちり押さえたコード**でした。

次のステップとしては、**可読性・Python 的な書き方**にも意識を向けていくと、さらに一段レベルアップできます！🔥

お疲れさまでした！💪
