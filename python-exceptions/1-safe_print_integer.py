def list_division(my_l_1, my_l_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            res = 0
            try:
                res = my_l_1[i] / my_l_2[i]
            except ZeroDivisionError:
                print("division by 0")
            except IndexError:
                print("out of range")
            except (TypeError, ValueError):
                res = 0
        finally:
            new_list.append(res)
    return new_list
