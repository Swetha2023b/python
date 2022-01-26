def Merge(dict1, dict2):
    return (dict2.update(dict1))
dict1 = {'ammu': 10, 'bins': 8}
dict2 = {'druv': 6, 'cyn': 4}
print(Merge(dict1, dict2))
print(dict2)
