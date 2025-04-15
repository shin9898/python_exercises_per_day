# 模範回答
```python
from collections import Counter
from typing import List, Tuple

def analyze_log(log: List[str]) -> List[Tuple[str, int]]:
user_ids = [entry.split(":")[0].strip() for entry in log]
counter = Counter(user_ids) # 出現回数（降順）＋ユーザー名の昇順にソート
sorted_users = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
return sorted_users

# テスト

log = [
"user1: login",
"user2: login",
"user1: view",
"user2: view",
"user1: logout",
"user3: login",
"user2: logout",
"user3: logout",
"user1: login"
]

print(analyze_log(log)) # [('user1', 4), ('user2', 3), ('user3', 2)]
```

# Day3 解説 - ログデータ解析

## 主なポイント

- ログ文字列からユーザーIDを抽出する
```python
user_ids = [entry.split(":")[0].strip() for entry in log]
```
- collections.Counter を用いた出現回数のカウント

```python
count = Counter(user_ids)
```
- 頻度順ソートは .most_common() を使うと自動で降順に整列される

## 型ヒントについて
```python
from typing import List, Tuple
def analyze_log(log: List[str]) -> List[Tuple[str, int]]:
```
これは 関数の引数と戻り値の型を明示して、静的解析や補完精度を高めるためのものです。

## 応用ポイント
Counter は .most_common() で頻度順にソートされたリストを返す

リスト内包表記と split(":") の組み合わせで効率的にID抽出が可能