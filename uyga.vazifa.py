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

