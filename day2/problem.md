# Day2 - School クラスで複数の Student を管理

Day1 の `Student` クラスをベースに、学校全体の成績を管理する `School` クラスを作成してください。

## 要件

- `School` クラスの属性
  - `students_list`: Student のリスト
- メソッド
  - `add_student(student: Student)`：生徒を追加
  - `school_average()`：全生徒のスコア平均を計算
  - `top_student()`：平均点が最も高い生徒の名前を返す

## 実行例

```python
student1 = Student("Koki")
student1.add_score(80)
student1.add_score(90)

student2 = Student("Rika")
student2.add_score(100)
student2.add_score(95)

school = School()
school.add_student(student1)
school.add_student(student2)

print("School average:", school.school_average())
# 出力例: School average: 91.25
print("Top student:", school.top_student())
# 出力例: Top student: Rika
```
