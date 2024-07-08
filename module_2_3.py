my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

nul = 0

while len(my_list) > nul:

    if my_list[0] == nul:
        my_list.remove(my_list[0])
        continue
    elif my_list[0] > nul:
        print(my_list[0])
        my_list.remove(my_list[0])
    else:
            break

