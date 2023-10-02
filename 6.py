# lst_1 = '3 1 3 4 2 4 12'.split()
# lst_2 = '4 15 43 1 15 1'.split()
# for i in lst_1:
#     if i not in lst_2:
#         print(i,  end=' ')




# lst = list(map(int, '1 5 3 10 5 '.split()))
# counter = 0
# for i in range(1, len(lst)-1):
#     if lst[i-1] < lst[i] and lst[i+1] < lst[i]:
#         counter +=1
# print(counter)
# print(lst)







# lst = list(map(int, '4 2 3 2 3 7 2 2 6 7'.split()))
# n = 0
# for i in range(len(lst)):
#     for j in range(i+1, len(lst)):
#         if lst[i] == lst[j]:
#             n +=1
# print(n)


# def sum_of_divisors(n):
#     res = 0
#     for i in range(1, n):
#         if n % i == 0:
#             res += i

#     return res


# def is_friends(a, b):
#     return sum_of_divisors(a) == b and a == sum_of_divisors(b)


# k = 1000
# for a in range(1, k + 1):
#     for b in range(a + 1, k + 1):
#         if is_friends(a, b):
#             print(a, b)
            




