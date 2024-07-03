my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

nul=0
positive=[]
while len(my_list)>nul:
    if my_list[0]>nul:
      b=my_list[0]
      my_list.remove(b)
      positive.append(b)

    else:
        b = my_list[0]
        my_list.remove(b)
print(positive)


my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
while len(my_list)>nul:
    if my_list[0]>nul:
      b=my_list[0]
      print(b)
      my_list.remove(b)

    elif my_list[0]== nul:
        b = my_list[0]
        my_list.remove(b)

    else : break
