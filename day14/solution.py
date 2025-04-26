def the_sum_of_the_differences(num_list: list[int]) -> list[int]:
    result_list = []
    for i in range(len(num_list)):
        if i != len(num_list) - 1:
            result = (num_list[i - 1] - num_list[i]) + (num_list[i + 1] - num_list[i])
            result_list.append(result)
        else:
            result = (num_list[i - 1] - num_list[i]) + (num_list[0] - num_list[i])
            result_list.append(result)
    return result_list


if __name__ == '__main__':
    A1 = [3, 1, 4]
    # 期待出力: [-1, 5, -4]
    A2 = [2, 2, 2]
    # 期待出力: [0, 0, 0]
    A3 = [5, -5]
    # 期待出力: [-20, 20]
    print(the_sum_of_the_differences(A1))
    print(the_sum_of_the_differences(A2))
    print(the_sum_of_the_differences(A3))