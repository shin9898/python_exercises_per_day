from collections import defaultdict



def classify_by_distance(N: int, grid: list[list[int]]) -> dict[int, int]:
    center = N // 2
    total_num_dict = defaultdict(int)
    for i in range(N):
        for j in range(N):
            d = max(abs(i - center) , abs(j - center))
            total_num_dict.setdefault(d, 0)
            total_num_dict[d] += grid[i][j]
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
    print(classify_by_distance(N, grid)) # 期待出力 {0: 3, 1: 16, 2: 16}
    # 入力例2
    N = 3
    grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9,]
    ]
    print(classify_by_distance(N, grid)) # 期待出力 {0: 5, 1: 40}
    # 入力例3
    N = 5
    grid = [
        [1, 1, 1, 1, 1],
        [1, 2, 2, 2, 1],
        [1, 2, 3, 2, 1],
        [1, 2, 2, 2, 1],
        [1, 1, 1, 1, 1]
    ]
    print(classify_by_distance(N, grid)) # 期待出力 {0: 3, 1: 16, 2: 16}
    # 入力例4
    N = 7
    grid = [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 2, 2, 2, 2, 2, 1],
        [1, 2, 3, 3, 3, 2, 1],
        [1, 2, 3, 4, 3, 2, 1],
        [1, 2, 3, 3, 3, 2, 1],
        [1, 2, 2, 2, 2, 2, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ]
    print(classify_by_distance(N, grid)) # 期待出力 {0: 4, 1: 20, 2: 40, 3: 24}