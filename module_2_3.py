# применить навыки создания цикла while, а так же применения операторов break и continue

my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
while a < len(my_list):
    if my_list[a] > 0:
        print(my_list[a])
        a = a + 1
    else:
        if my_list[a] < 0:
            break
        a = a + 1


