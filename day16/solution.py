def maximum_of_the_product(arr: int, num_list:list[int]) -> int:
    result = 0
    for i in range(arr):
        if i == 0:
            result += num_list[i]
        else:
            result *= num_list[i]
    return abs(result)

if __name__ == '__main__':
    arr = int(input())
    num_list = list(map(int, input().split()))
    print(maximum_of_the_product(arr, num_list))