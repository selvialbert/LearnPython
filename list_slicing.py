def list_slice_ops():
    #print('Enter your list value :')
    my_list = []
    my_list = [int(item) for item in input("Enter the list numeric values : ").split()]
    my_list1 = []
    my_list1 = [item for item in input("Enter the list string values : ").split()]
    list = my_list + my_list1
    print(list)

    print(f'You entered : ', list)
    print('-------------------------------------')
    print("Slice of '{1}' after removing first and last character'{0}'".format(list[1:-1], list))
    print('-------------------------------------')
    print("Slice of '{1}' after removing first 2 characters'{0}'".format(list[2:], list))
    print('-------------------------------------')
    print("Slice of '{1}' after removing last 2 characters '{0}'".format(list[:-2],list))
    print('-------------------------------------')
    print("Mid index is {0}".format(int(len(list) / 2)))
    print('-------------------------------------')
    mi = int(len(list) / 2)
    print("First half of '{1}' is '{0}'".format(list[:mi], list))
    print("Second half of '{1}' is '{0}'".format(list[mi:], list))
    print('-------------------------------------')

list_slice_ops()
