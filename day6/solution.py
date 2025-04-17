# Day6 解答テンプレート

class Employee:
    def __init__(self, name: str, department: str, salary: int):
        self.name = name
        self.department = department
        self.salary = salary

def filter_employees(employees: list[Employee], department: str, min_salary: int) -> list[str]:
    applicable_employees_list = []
    for employee in employees:
        if employee.department not in department:
            continue
        if not employee.salary >= min_salary:
            continue
        applicable_employees_list.append(employee.name)
    return applicable_employees_list

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
