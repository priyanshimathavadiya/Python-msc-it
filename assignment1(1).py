"""display only those numbers that appersconsetively more than once"""


# i = 0
# while i < num:
#     list1.append(int(input("Enter number: ")))
#     i = i + 1 #this is for add list

# i = 0

# while i < num - 1:
#     if list1[i] == list1[i + 1]:
#         print(list1[i]) # for finding duplicate 

#         while i < num - 1 and list1[i] == list1[i + 1]:
#             i = i + 1
#     else:
#         i = i + 1 #this is for remove duplicates
num = [1,2,2,3,4,4,4,5]
dup = []
for i in num:
    if num.count(i) > 1 and i not in dup:#AND condition use for split tow condition 
        dup.append(i)#use for add in last in list
print(dup)

        