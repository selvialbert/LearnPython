def list_index_ops():
    #print('Enter your list value :')
    my_list = []
    my_list = [int(item) for item in input("Enter the list numeric values : ").split()]
    my_list1 = []
    my_list1 = [item for item in input("Enter the list string values : ").split()]
    list = my_list + my_list1
    print(list)
    print('-------------------------------------')
    print("First character in '{1}' is '{0}'".format(list[0], list))
    print('-------------------------------------')
    print("Last character in '{1}' is '{0}'".format(list[-1], list))
    print('-------------------------------------')
    print("Length of string '{1}' is '{0}'".format(len(list), list))
    print('-------------------------------------')
    print("Mid index is {0}".format(int(len(list)/2)))
    print('-------------------------------------')
    mi = int(len(list)/2)
    if len(list)%2 == 0:
        print("Middle character of '{1}' are {0} and {2}".format(list[mi-1], list,list[mi]))
    else:
        print("Middle character of '{1}' is {0}".format(list[mi], list))

list_index_ops()