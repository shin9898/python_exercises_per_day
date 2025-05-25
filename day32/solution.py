from collections import defaultdict

def analyze_students(courses: list[dict], enrollments: list[dict]) -> list[dict]:
    programming_courses = list(filter(lambda course: "Programming" in course['category'], courses))

    students_count = defaultdict(int)
    for enrollment in enrollments:
        course_id = enrollment['course_id']
        students_count[course_id] += 1

    processed_courses = []
    for course in programming_courses:
        course_id = course['course_id']
        course_name = course['name']
        num_students = students_count.get(course_id, 0)
        if num_students > 0:
            processed_courses.append({
                "name": course_name,
                "num_students": num_students
            })
    return sorted(processed_courses, key=lambda x : (-x['num_students'], x['name']))



if __name__ == '__main__':
    courses = [
    {"course_id": "C001", "name": "Python Basics", "category": "Programming", "level": "Beginner"},
    {"course_id": "C002", "name": "Web Development with Django", "category": "Programming", "level": "Intermediate"},
    {"course_id": "C003", "name": "Data Science Fundamentals", "category": "Data Science", "level": "Beginner"},
    {"course_id": "C004", "name": "Machine Learning Advanced", "category": "Data Science", "level": "Advanced"},
    {"course_id": "C005", "name": "Cloud Computing Essentials", "category": "Cloud", "level": "Intermediate"},
    ]

    enrollments = [
        {"student_id": "S001", "course_id": "C001", "progress": 80},
        {"student_id": "S002", "course_id": "C001", "progress": 100},
        {"student_id": "S003", "course_id": "C002", "progress": 50},
        {"student_id": "S004", "course_id": "C003", "progress": 90},
        {"student_id": "S005", "course_id": "C001", "progress": 70},
        {"student_id": "S006", "course_id": "C004", "progress": 20},
        {"student_id": "S007", "course_id": "C003", "progress": 100},
        {"student_id": "S008", "course_id": "C002", "progress": 100},
        ]

    print(analyze_students(courses, enrollments))
