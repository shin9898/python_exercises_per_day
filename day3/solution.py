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


