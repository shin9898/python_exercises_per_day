# Day6 問題：社員データのフィルタリング

以下の指示に従って、社員データを処理する関数を作成してください。

---

## 🔧 要件

以下のような `Employee` クラスを定義してください：

```python
class Employee:
    def __init__(self, name: str, department: str, salary: int):
        self.name = name
        self.department = department
        self.salary = salary
```

次に、社員リストから以下の条件に合う社員の名前を抽出する関数を作成してください：

```python
def filter_employees(employees: list[Employee], department: str, min_salary: int) -> list[str]:
    pass
```

この関数は、

- 指定された部署（`department`）に所属していて
- 給与が `min_salary` 以上
  の社員の名前リストを返すものとします。

---

## ✅ テストケース

以下のコードを使って、関数が正しく動作するかを確認してください：

```python
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
