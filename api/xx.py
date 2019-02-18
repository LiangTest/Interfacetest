# def add(n,i):
#     print(
#         'n:',n,'\t',
#         'i:',i,'\t',
#         'n+i:',n+i,'\t',
#     )
#     return n+i
#
# g=[0,1]
# for n in [1,2]:
#     print(n)
#     g=(add(n,i) for i in g)
#
# print(list(g))


# def get_sum(num):
#     if num>=1:
#         res = num + get_sum(num-1)
#     else:
#         res = 0
#     return res

# res = get_sum(3)
# print(res)



str = 'abc 123 ABC'
str1 = str.replace(' ','')
str2 = ''.join(str.split(' '))
print(str1)
print(str2)


