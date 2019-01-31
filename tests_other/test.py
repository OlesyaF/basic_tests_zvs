import random

list1 = [num for num in range(10)]
print("list1: ", list1)
i = 0
list2 = []
while i < 10:
    list2.append(str(random.choice(list1)))
    i = i + 1
print("list2: ", list2)
phone = ""
for i in list2:
    phone = phone + str(i)
print("phone: ", phone)
phone_mask = "+7 (" + str(list2[0]) + str(list2[1]) + str(list2[2]) + ") " + str(list2[3]) + str(list2[4]) + str(
     list2[5]) + "-" + str(list2[6]) + str(list2[7]) + "-" + str(list2[8]) + str(list2[9])
print("phone_mask: ", phone_mask)


# list2.insert(1, "+7 (")
# list2.insert(5, ") ")
# list2.insert(9, "-")
# list2.insert(12, "-")
# print("list2: ", list2)
# phone_mask2 = str(list2)
# print("phone_mask2: ", phone_mask2)
# locator = "//input[@value='" + phone_mask1 + "']"
# print("locator: ", locator)
