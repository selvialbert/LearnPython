def tuple_index_ops():
    #print('Enter your tuple value :')
    my_tuple = []
    my_tuple = [int(item) for item in input("Enter the tuple numeric values : ").split()]
    my_tuple1 = []
    my_tuple1 = [item for item in input("Enter the tuple string values : ").split()]
    tuple = my_tuple + my_tuple1
    print(tuple)
    print('-------------------------------------')
    print("First item in the tuple '{1}' is '{0}'".format(tuple[0], tuple))
    print('-------------------------------------')
    print("Last item in the tuple '{1}' is '{0}'".format(tuple[-1], tuple))
    print('-------------------------------------')
    print("Length of the tuple is '{1}' is '{0}'".format(len(tuple), tuple))
    print('-------------------------------------')
    print("Mid item's index in the tuple is {0}".format(int(len(tuple)/2)))
    print('-------------------------------------')
    mi = int(len(tuple)/2)
    if len(tuple)%2 == 0:
        print("Middle item of the tuple is '{1}' are {0} and {2}".format(tuple[mi-1], tuple,tuple[mi]))
    else:
        print("Middle item(s) of the tuple are '{1}' is {0}".format(tuple[mi], tuple))

tuple_index_ops()