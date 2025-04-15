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
        if not self.scores:
            raise ValueError("スコアが登録されていません")
        return round(sum(self.scores) / len(self.scores) , 2)  

class School:
    def __init__(self):
        self.students_list = []
    
    def add_student(self, student):
        if not student:
            raise ValueError("生徒が登録されていません")
        self.students_list.append(student)

    def school_average(self):
          scores = []
          if not self.students_list:
              raise ValueError("生徒が登録されていません")
          for student in self.students_list:
              for score in student.scores:
                  scores.append(score)
          return round(sum(scores) / len(scores), 2)
                  
    def top_student(self):
        if not self.students_list:
            raise ValueError("生徒が登録されていません")
        top = max(self.students_list, key=lambda student: sum(student.scores) / len(student.scores) if student.scores else 0)
        return top.name
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
print("Top student:", school.top_student())