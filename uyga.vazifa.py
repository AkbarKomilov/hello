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
   