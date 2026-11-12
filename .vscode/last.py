# import json

# with open("test.json", "r") as ptr:
#     data = json.load(ptr)

#     for shaxs in data:
#         if "Matematika" in shaxs["subjects"]:
#             print(shaxs["name"], shaxs["second"])


# ------------------------------------------------
# import json

# with open("test.json", "r") as ptr:
#     data = json.load(ptr)

#     jami = 0
#     for shaxs in data:
#         jami += shaxs["narx"] * shaxs["son"]

#     print("Jami summa:", jami)


# ----------------------------------------------------
# import json

# with open("test.json", "r") as ptr:
#     shaharlar = json.load(ptr)


#     eng_katta = shaharlar[0]

#     for shahar in shaharlar:
#         if shahar["aholi"] > eng_katta["aholi"]:
#             eng_katta = shahar

#     print(f"Eng ko'p aholiga ega shahar: {eng_katta['nom']} ({eng_katta['aholi']}"
#         " kishi)")


# ----------------------------------------------


# import json

# with open(".vscode/data.json") as ptr:
#   data = json.load(ptr)
#   for i in data["students"]:
#     print(f"{i['name']} : {sum(i['grades']) // len(i['grades'])}")


# ---------------------------------------------------

