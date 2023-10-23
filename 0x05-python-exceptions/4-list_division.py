#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_l = []
    for i in range(list_length):
        try:
            resault = my_list_1[i] / my_list_2[i]
            new_l.append(resault)
        except ZeroDivisionError:
            print("division by 0")
            new_l.append(0)
        except TypeError:
            print("wrong type")
            new_l.append(0)
        except IndexError:
            print("out of range")
            new_l.append(0)
        finally:
            pass
    return new_l
