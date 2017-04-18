def data_type(x):
    if isinstance(x, str):
        return len(x)
    elif isinstance(x, bool):
        return x
    elif isinstance(x, int):
        if x > 100:
            return 'more than 100'
        elif x == 100:
            return 'equal to 100'
        else:
            return 'less than 100'
    elif isinstance(x, list):
        if len(x) >= 3:
            return x[2]
        else:
            return None
    elif x == None:
        return 'no value'
    else:
        return None

print(data_type(False))
