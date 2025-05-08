def average_age(users: list[dict]) -> int:
    age_list = [user['age'] for user in users]
    try:
        return round(sum(age_list) / len(age_list))
    except TypeError:
        print("'age'に整数でないものがあります")


if __name__ == '__main__':
    users = [
            {"name": "Alice", "age": 30},
            {"name": "Bob", "age": 24},
            {"name": "Charlie", "age": 29}
        ]
    print(average_age(users))