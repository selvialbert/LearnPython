def string_index_ops():
    print('Enter your string value :')
    string_value = str(input())
    print(f'You entered : '+string_value)
    print('-------------------------------------')



    print("First character in '{1}' is '{0}'".format(string_value[1], string_value))
    print("First character in '{1}' is '{0}'".format(string_value[0], string_value))
    print('-------------------------------------')
    print("Last character in '{1}' is '{0}'".format(string_value[-1], string_value))
    print('-------------------------------------')
    print("Length of string '{1}' is '{0}'".format(len(string_value), string_value))
    print('-------------------------------------')
    print("Mid index is {0}".format(int(len(string_value)/2)))
    print('-------------------------------------')
    mi = int(len(string_value)/2)
    if len(string_value)%2 == 0:
        print("Middle character of '{1}' are {0} and {2}".format(string_value[mi-1], string_value,string_value[mi]))
    else:
        print("Middle character of '{1}' is {0}".format(string_value[mi], string_value))

string_index_ops()



