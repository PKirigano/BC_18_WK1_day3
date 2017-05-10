def find_max_min(my_list):
    if max(my_list)==min(my_list):
        return [len(my_list)]
    else:
        return [min(my_list),max(my_list)]
