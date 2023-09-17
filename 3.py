# dt = {}

# lst = ["A", "B", "B", "C"]

# for w in lst:
#     dt[w] = dt.get(w, 0) + 1
    
# # for w in lst:
# #     if w not in dt:
# #         dt[w] = 0
# #     else:
# #         dt[w] += 1

# print(dt)

lst = [1, 2, 3, 4, 5]
k = 6
k = k % len(lst)
lst = lst[k:]+lst[:k]
print(lst)
