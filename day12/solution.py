from collections import defaultdict


def classify_by_distance(N: int, grid: list[list[int]]) -> dict[int, int]:
    center = N // 2
    total_num_dict = defaultdict(int)
    for i in range(N):
        for j in range(N):
            d = max(abs(i - center), abs(j - center))
            total_num_dict[d] += grid[i][j]
    element_to_remove_key_list = [key for key, value in total_num_dict.items() if value % 2 != 0]
    for key in element_to_remove_key_list:
        del total_num_dict[key]
    return dict(total_num_dict)


if __name__ == '__main__':
    # 入力例1
    N = 5
    grid = [
        [1, 1, 1, 1, 1],
        [1, 2, 2, 2, 1],
        [1, 2, 3, 2, 1],
        [1, 2, 2, 2, 1],
        [1, 1, 1, 1, 1],
    ]
    print(classify_by_distance(N, grid)) # 期待出力 {1: 16, 2: 16}
    # 入力例2
    N = 3
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    print(classify_by_distance(N, grid)) # 期待出力 {1: 40}