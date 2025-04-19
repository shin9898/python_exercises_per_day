# Day8 問題

以下の要件に従ってクラスと関数を定義してください。

## 要件

1. `Student` クラスを作成し、名前 (`name`: str)、スコア (`scores`: list[int]、各教科の点数) を持つようにしてください。
2. 次のメソッドを実装してください：
   - `average_score()`：スコアの平均を計算して返す
   - `has_passed(threshold: int)`：平均点が `threshold` 以上であれば `True` を返す
3. `filter_passed_students(students: list[Student], threshold: int) -> list[str]` という関数を定義し、
   - 合格した生徒の名前だけをリストで返してください。

## 実行例

```python
students = [
    Student("Alice", [70, 80, 90]),
    Student("Bob", [50, 60, 55]),
    Student("Charlie", [90, 95, 100])
]

print(filter_passed_students(students, 70))  # => ["Alice", "Charlie"]
```
