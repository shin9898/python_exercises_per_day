# Day6 解説

## ✅ 実装内容チェック

あなたの提出された解答を確認しました。以下の点が正しく実装されています：

- ✅ `Employee` クラスに `name`, `department`, `salary` の 3 属性を正しく実装
- ✅ `filter_employees` 関数で、部署・給与条件にマッチする社員名の抽出が行えている
- ✅ リスト内包表記を使った簡潔な記述
- ✅ テスト実行の結果 `["Alice", "Charlie"]` が出力されている

Good Job!! 🎉

---

## 🛠 改善ポイント・アドバイス

### 1. 戻り値の型ヒント

関数 `filter_employees` に対して `-> list[str]` という型ヒントが明示されている点は非常に良いです。
Python3.9 以降であれば `list[str]` の記法も使えますが、より汎用性を持たせるなら `List[str]`（`from typing import List`）も検討してみてください。

### 2. filter 関数との比較

今回はリスト内包表記で実装されていますが、同様の処理は `filter` や `lambda` を使っても書けるので、スタイルの違いも学んでおくと良いでしょう：

```python
names = list(map(lambda e: e.name, filter(lambda e: e.department == department and e.salary >= min_salary, employees)))
```

---

## 🧪 模範解答（サンプルコード）

```python
class Employee:
    def __init__(self, name: str, department: str, salary: int):
        self.name = name
        self.department = department
        self.salary = salary

def filter_employees(employees: list[Employee], department: str, min_salary: int) -> list[str]:
    return [e.name for e in employees if e.department == department and e.salary >= min_salary]

if __name__ == "__main__":
    employees = [
        Employee("Alice", "Engineering", 700),
        Employee("Bob", "HR", 500),
        Employee("Charlie", "Engineering", 600),
        Employee("Diana", "Engineering", 550),
        Employee("Eve", "Marketing", 650)
    ]

    result = filter_employees(employees, "Engineering", 600)
    print(result)  # => ["Alice", "Charlie"]
```

---

## 総評

Day6 では**クラスとリストの組み合わせによるデータ抽出処理**がテーマでした。クラスの定義やリスト内包表記の使い方も的確で、非常にスムーズなコードでした！

次のステップとしては、**ソート処理**や**複雑な条件分岐**のあるロジックにもチャレンジしてみましょう。Day7 で扱う予定ですのでお楽しみに！🔥

お疲れさまでした！
