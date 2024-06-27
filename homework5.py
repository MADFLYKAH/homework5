immutable_var = 1,True,'banana'
print('Immutable tuple:',immutable_var)
# immutable_var[0] = 2    TypeError: 'tuple' object does not support item assignment
mutable_list = [1,False,'dog']
mutable_list[0] = 2
mutable_list[2] = 'cat'
print('Mutable list:',mutable_list)
