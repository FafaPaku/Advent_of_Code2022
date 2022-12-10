data = []
my_sum = 0
# reading from file
with open("day1/input.txt") as file1:
    for line in file1:
        int_list = [int(i) for i in line.split()]
        if len(int_list) == 1:
            my_sum = my_sum + int_list[0]
        else:
            data.append((my_sum))
            my_sum = 0

    data.sort(reverse=True)
print(data[0])
print(sum(data[0:3]))
