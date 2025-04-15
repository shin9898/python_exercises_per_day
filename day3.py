from collections import Counter


def analyze_log(log: list[str]) -> list[tuple[str, int]]:
    slice_id_list = []
    for value in log:
        slice_id = value[0:5]
        slice_id_list.append(slice_id)
    count_id_list = Counter(slice_id_list)
    mx = count_id_list.most_common()
    print(mx)


log = [
    "user1: login",
    "user2: login",
    "user1: view",
    "user2: view",
    "user1: logout",
    "user3: login",
    "user2: logout",
    "user3: logout",
    "user1: login"
]
analyze_log(log)

# 模範回答
from collections import Counter
from typing import List, Tuple

def analyze_log(log: List[str]) -> List[Tuple[str, int]]:
    user_ids = [entry.split(":")[0].strip() for entry in log]
    counter = Counter(user_ids)
    # 出現回数（降順）＋ユーザー名の昇順にソート
    sorted_users = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
    return sorted_users

# テスト
log = [
    "user1: login",
    "user2: login",
    "user1: view",
    "user2: view",
    "user1: logout",
    "user3: login",
    "user2: logout",
    "user3: logout",
    "user1: login"
]

print(analyze_log(log))  # [('user1', 4), ('user2', 3), ('user3', 2)]
