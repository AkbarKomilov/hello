# tuple = ((1,2), (2,3),(3,4))

# natija = []

# for juftlik in tuple :
#     natija.append(list(juftlik))
#     print(natija)

#-------------------------------------------

# malumotlar = ("ada", 212, False, 4567, "aziza")

# for qiymat in malumotlar:
#     if isinstance(qiymat, (str, int)):
#         if str(qiymat) == str(qiymat)[::-1]:
#             print(qiymat, "palindrom")
#         else:
#             print(qiymat, "palindrom emas")
#     else:
#         print(qiymat, " palindrom emas")

# --------------------------------------------------

# malumotlar = [(1, 2, 3), (2, 2), (3, 0, 0)]

# natija = []

# for tuple in malumotlar:
#     natija.append(tuple[::-1])

# print(natija)

# ----------------------------------------------------

# malumotlar = [(1,2),(3,4),(8,9)]
# n1 = []
# n2 = []
# for i in malumotlar:
#     print(i[0], i[1])
#     n1.append(i[0])
#     n2.append(i[1])
# print([tuple(n1), tuple(n2)])

# ---------------------------------------

# malumotlar = [
#     (0, 2, 0, 0),
#     (0, 3, 2, 2),
#     (1, 3, 2, 4, 3),
#     (4, 1, 2, 4)
# ]

# natija = []

# for tuple_ in malumotlar:
#     yangi_tuple = []

#     for son in tuple_:
#         yangi_tuple.append(tuple_.count(son))

#     natija.append(tuple(yangi_tuple))

# print(natija)

# ------------------------------------------------------

# lst = [(0,2,0,0),(0,3,2,2),(1,3,2,4,3),(4,1,2,4)]
# new = []
# for i in lst:
#     temp = []
#     for x in i:
#         temp.append(i.count(x))

#         new.append(tuple(temp))
# print(new)        

# ---------------------------------------------------------

# lst = []
# for i in range(int(input("Nechta son kiritmoqchisiz: "))):
#     lst.append(input())
# print(f"soni {len(lst)}\nOhirgisi {lst[-1]}\nTeskarisi: {lst[::-1]}")

# ---------------------------------------------------------------

