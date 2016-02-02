def unflatten_dict(a, result=None,temp=''):
    if result is None:
        result = {}
    for x in a:
       if str(x).find('.') == 1:
           result[x] = unflatten_dict(a[x], result,x)
       else:
           if temp == '':
                result[x] = a[x]
           else:
                result[temp+"."+x] = a[x]
    return result
print unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
