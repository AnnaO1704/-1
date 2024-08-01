immutable_var = (1,2,'a','b')
print(immutable_var)
#immutable_var .append(3)
# print(immutable_var) #кортеж является неизменяемым
mutable_list = [1,2,3,4]
mutable_list[0] = 32
mutable_list .append('number')
print(mutable_list)
