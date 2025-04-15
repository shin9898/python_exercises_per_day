# Day1 - Studentクラスの平均点計算

以下の要件を満たす `Student` クラスを作成してください。

## 要件

- `Student` クラスは以下の属性を持つ
  - `name`: 学生の名前（文字列）
  - `scores`: テストの点数（整数のリスト）
- `add_score(score: int)` メソッド
  - 0〜100 の整数のみ追加可能
  - 範囲外の値は無視し、「不正な値です」と表示する
- `average_score()` メソッド
  - `scores` に追加された値の平均を計算し、小数点2桁で返す
  - スコアが登録されていない場合は例外を発生させる

## 実行例

```python
student = Student("Koki")
student.add_score(80)
student.add_score(90)
student.add_score(75)
print(f"{student.name}'s average score is {student.average_score()}")
# 出力: Koki's average score is 81.67
