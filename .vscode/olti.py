# def count(a:str):
#     new = {}
#     for harf in a:
#         if harf not in new:
#             new[harf] = 1
#         else:
#             new[harf] += 1
#     print(new)

# count(a=input())

# ---------------------------------------------

# def uzgargan_son(k, n):
#     print(k + n)

# uzgargan_son("9", "6532")
    
# ------------------------------------

# def swap(satr):
#   for i in satr.split():
 
#     if len(i) > 1:
#       print(i[-1] + i[1:-1] + i[0], end=" ")
#     else:
#       print(i, end=" ")


# satr = input("satr kiriting: ")
# swap(satr)

# ------------------------------------------------


# def plus_dct(d1:dict, d2:dict):
#     for i in d1:
#         if i not in d2:
#             d2[i] =  d1[i]
#         else:
#             d2[i] += d1[i]

#     return d2


# d1 = {"a": 100, "b": 200, "c": 300}
# d2 = {"a": 300, "b": 200, "d": 400}
# print(plus_dct(d1, d2))


# ---------------------------------------------------------

# def get_gmail(a:list):
#     ntj = []
#     for i in a:
#         ntj.append(i.split("@")[-1])

#     return list(set(ntj)) 

# lst = ["user@gmail.com", "user2@mail.ru", "user3@gmail.com"]
# print(get_gmail(lst))   


# -----------------------------------------------------------------


# fanlar = ["Math", "physics", "math", "biology", "math", "physics"]
# natija = {}

# for fan in set(fanlar): 
#     natija[fan] = fanlar.count(fan)

# print(natija)


# -----------------------------------------------------------------


# talaba = {"ism": "Ali", "yosh": 19, "fan": "python"}

# kalit = input("kalit nomini kiriting (masalan: ism, yosh, fan):")

# if kalit in talaba:
#     print(f"{kalit}: {talaba[kalit]}")
# else:
#     print("bunday kalit mavjud emas")    


# -------------------------------------------------------------


# kiritish = input("Sonlarni vergul bilan kiriting: ")


# sonlar = kiritish.split(",")

# yigindi = 0

# for x in sonlar:
#   son = int(x)  
#   if son % 2 == 0:  
#     yigindi += son  

# print(f"Juft sonlar yig'indisi: {yigindi}")


# ------------------------------------------------------------------


