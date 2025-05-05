def validity_check(users: list[dict]) -> list[str]:
    return [f"{user['name']}さんのメールアドレスは{user['email']}です" for user in users if user['is_active']]



if __name__ == '__main__':
    users = [
        {"name": "Miyu", "email": "miyu@example.com", "is_active": True},
        {"name": "Ken", "email": "ken@example.com", "is_active": False},
        {"name": "Sara", "email": "sara@example.com", "is_active": True}
    ]

    print(validity_check(users))