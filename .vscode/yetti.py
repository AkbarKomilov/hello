
# narxlar = [10000, 25000, 5000]
# yangi_narxlar = list(map(lambda narx: narx * 1.12, narxlar))
# print(yangi_narxlar)

# ----------------------------------------------------------------

# email = ["ALi ,ali@gmail.com", "Vali, vali@123@gmail.ru", "Aziza, aziza@ouylook.com"]
# email = list(map(lambda x: x.split(" ")[1], email))
# print(email)

# ----------------------------------------------------------------

# menyu = [("Burger", False), ("Salad", True), ("Soup", True), ("Steak", False)]
# vegetarian = list(map(lambda x: x[0], filter(lambda x: x[1] == True, menyu)))
# print(vegetarian)

# -----------------------------------------------------------------------

# baho = [55, 60, 75, 90, 45]
# katta = list(filter(lambda x: x>=60,baho))
# print(katta)

# --------------------------------------------------------------------

# raqam = ["+998901234567", "+375291234567", "+998991112233", "0901234567"]
# kodi = list(filter(lambda x: x[:4] == "+998", raqam))
# print(kodi)

# ------------------------------------------------------------------------

# natija = list(map(lambda x: f"{str(x)[:-3]},000 so'm", [15000, 23000, 5000, 125000]))
# print(natija)

# ----------------------------------------------------------------------

# natija = list(filter(lambda x: x[1]=="IT", [("Ali", "IT", "Vali", "HR"), ("Aziza", "IT"), ("Nodir", "Finance")]))
# natija = list(map(lambda x: x[0], natija))
# print(natija)

# ------------------------------------------------------------------------------

# mahsulotlar = [("Olma", 10000), ("Bana", 12000), ("uzum", 15000)]
# yangi_narx = list(map(lambda x: (x[0], int(x[1] * 0.9)), mahsulotlar))
# print(yangi_narx)

# ------------------------------------------------------------------

# matn = "Python dasturlash tili juda kuchli va sodda"
# sozlar = matn.split()
# uzum_sozlar = list(filter(lambda x: len(x) > 5, sozlar))
# print(uzum_sozlar)

# ----------------------------------------------------------------------

# import lib

# a = [("Olma", 10000), ("Banan", 12000), ("uzum", 15000)]
# natija = lib.Increase(a)
# print(natija)

# ----------------------------------------------------------

