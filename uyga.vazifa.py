# 1-masala

def majority_element(nums: list) -> int:
  if not nums:
    return -1

  eng_kop = nums[0]
  for x in nums:
    if nums.count(x) > nums.count(eng_kop):
      eng_kop = x

  return eng_kop


print(majority_element([2, 2, 1, 1, 1, 2, 2]))


# 2-masala


def search_by_genre(cinema: list, genre: str) -> list:
    natija = []
    for film in cinema:
        if film["genre"] == genre:
            natija.append(film)
    return natija


if __name__ == "__main__":
    cinema = [
        {"title": "Avatar", "genre": "Fantastika", "price": 40000},
        {"title": "Sherlock", "genre": "Detektiv", "price": 30000},
        {"title": "Oq yo‘l", "genre": "Drama", "price": 25000},
        {"title": "Dune", "genre": "Fantastika", "price": 35000}
    ]

    print(search_by_genre(cinema, "Fantastika"))
   
    
    print(search_by_genre(cinema, "Drama"))

    
    print(search_by_genre(cinema, "Komediya"))


#    3-masala


def merge_unique_ids(active_users: list, new_users: list) -> list:

    return list(set(active_users + new_users))


if __name__ == "__main__":
    active_users = ['U1001', 'U1002', 'U1003', 'U1004', 'U1001']
    new_users = ['U1003', 'U1005', 'U1006', 'U1002', 'U1007']
    print(merge_unique_ids(active_users, new_users))


# 4-masala

def sorted_by_price(products: list) -> list:

    return sorted(products, key=lambda x: int(x[1]), reverse=True)


if __name__ == "__main__":
    products = [
        ('Olma', '12000', '50'),
        ('Banan', '8000', '100'),
        ('Gilos', '15000', '70'),
        ('Apelsin', '9000', '80'),
        ('Anor', '30000', '20'),
        ('Uzum', '20000', '40'),
        ('Tarvuz', '25000', '15'),
        ('Shaftoli', '18000', '60'),
        ('Qovun', '40000', '25'),
        ('Qulupnay', '35000', '10')
    ]
    print(sorted_by_price(products))

# 4-masala


def are_numbers_ascending(text: str) -> bool:

    numbers = [int(word) for word in text.split() if word.isdigit()]
    

    for i in range(len(numbers) - 1):
        if numbers[i] >= numbers[i + 1]:
            return False
    return True


if __name__ == "__main__":
    print(are_numbers_ascending("1 qutida 5 ta yashil, 9 ta qizil, 12 ta sariq to’p bor edi"))  # True
    print(are_numbers_ascending("musobaqada 5 ga 5 ko’rinishida o’yinlar o’tkazildi"))           # False
    print(are_numbers_ascending("26 o’quvchidan 3 tasi 5 baxo oldi"))                            # False
