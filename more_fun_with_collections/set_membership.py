def in_set(check_set):

    return "Does the set contact 3? ", 3 in check_set


if __name__ == '__main__':
    my_set = {1,2,3,4,5}
    print("My set contains: ", my_set)
    print(in_set(my_set))
