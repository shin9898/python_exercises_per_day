# Day3 - ログデータの解析（ログインユーザーの頻度）

以下のログデータ（文字列リスト）から、ユーザー ID ごとの出現頻度を集計し、頻度が高い順に並べて出力してください。

## 制約

- ログの形式は `"{ユーザーID}: {アクション}"` です
- 頻度の高い順にタプル形式で表示してください（例: `("user1", 3)`）

## 実行例

```python
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
```

## 期待される出力：

```python
コピーする
編集する
[('user1', 4), ('user2', 3), ('user3', 2)]
perl
コピーする
編集する
```
