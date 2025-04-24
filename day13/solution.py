def rotate_grid_180(grid: list[list[int]]) -> list[list[int]]:
    rotated = [row[::-1] for row in grid[::-1]]
    return rotated


def is_grid_symmetric(grid: list[list[int]]) -> bool:
    rotated = rotate_grid_180(grid)
    return grid == rotated


if __name__ == '__main__':
    N = 3
    grid = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    print(is_grid_symmetric(grid))

    N = 3
    grid = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]
    print(is_grid_symmetric(grid))
    N = 3
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(is_grid_symmetric(grid))