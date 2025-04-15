class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, score):
        if 0<= score <=100:
            self.scores.append(score)
        else:
            print("不正な値です")

    def average_score(self):
        sum_scores = 0
        for score in self.scores:
            sum_scores += score
        average_s = sum_scores / len(self.scores)
        return round(average_s, 2)
            




student = Student("Koki")
student.add_score(80)
student.add_score(90)
student.add_score(75)

print(f"{student.name}'s average score is {student.average_score()}")
