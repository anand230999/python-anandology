def flatten_dict(a, result=None,temp=''):
    if result is None:
        result = {}
    for x in a:
        if type(a[x]) == dict:
            print x
            flatten_dict(a[x], result,x)
        else:
            if temp == '':
                result[x] = a[x]
            else:
                result[temp+"."+x] = a[x]
    return result
print flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
