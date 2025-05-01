def format_user_data(users: list[dict]) -> list[str]:
    row_list = [f"{user['name']}さんは{user['age']}歳です" for user in users]
    return row_list



def test():
    users = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 24},
        {"name": "Charlie", "age": 29}
    ]
    expected = ["Aliceさんは30歳です", "Bobさんは24歳です", "Charlieさんは29歳です"]
    assert format_user_data(users) == expected
    print("✅ テスト通過！")


if __name__ == '__main__':
    test()
    users = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 24},
        {"name": "Charlie", "age": 29}
    ]
    print(format_user_data(users))