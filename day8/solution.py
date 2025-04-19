# Day8 解答テンプレート

# Studentクラスとfilter_passed_students関数を定義してください
# ヒント：
# - sum() と len() で平均を出せます
# - リスト内包表記が使えます
class Student:
    def __init__(self, name: str, scores: list[int]):
        self.name = name
        self.scores = scores

    def average_score(self):
        return sum(self.scores) / len(self.scores)

    def has_passed(self, threshold: int):
        if Student.average_score(self) >= threshold:
            return True
        else:
            return False  # return追記

def filter_passed_students(students: list, threshold: int) -> list[str]:
    return [student.name for student in students if student.has_passed(threshold)]

if __name__ == "__main__":
    # テストコード例
    students = [
        Student("Alice", [70, 80, 90]),
        Student("Bob", [50, 60, 55]),
        Student("Charlie", [90, 95, 100])
    ]

    print(filter_passed_students(students, 70))
