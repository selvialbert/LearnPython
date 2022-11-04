def string_slice_ops():
    print('Enter your string value :')
    string_value = str(input())
    print(f'You entered : '+string_value)
    print('-------------------------------------')
    print("Slice of '{1}' after removing first and last character'{0}'".format(string_value[1:-1], string_value))
    print('-------------------------------------')
    print("Slice of '{1}' after removing first 2 characters'{0}'".format(string_value[2:], string_value))
    print('-------------------------------------')
    print("Slice of '{1}' after removing last 2 characters '{0}'".format(string_value[:-2], string_value))
    print('-------------------------------------')
    print("Mid index is {0}".format(int(len(string_value) / 2)))
    print('-------------------------------------')
    mi = int(len(string_value) / 2)
    print("First half of '{1}' is '{0}'".format(string_value[:mi], string_value))
    print("Seond half of '{1}' is '{0}'".format(string_value[mi:], string_value))
    print('-------------------------------------')
string_slice_ops()



