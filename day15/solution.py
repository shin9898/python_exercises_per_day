number_of_digit = int(input())
num_list = list(map(int, input().split()))


duplicate_num_list = []
for i in range(number_of_digit):
    if i == 0:
        duplicate_num_list.append(i)
    elif num_list[i] == num_list[i - 1]:
        continue
    else:
        duplicate_num_list.append(i)


print(len(duplicate_num_list))

# 8
# 1 1 2 2 2 3 1 1