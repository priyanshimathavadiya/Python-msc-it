"""missing roll number should be from 1 to N find missing roll number with out sorting """
# rolls = [1, 2, 4, 5, 6]
# N = 6
# total = N * (N + 1) //2
# missing = total - sum(rolls)
# print("Missing roll number:", missing)

n = int(input("Enter total number of students: "))

roll = []

i = 0
while i < n - 1:      #jo ek  number missing hase to aena mate n-1 use kari ne loop karisu
    roll.append(int(input("Enter roll number: ")))  # append use thay chhe last ma add karva mate list na andar
    #1,2,4,5,6 che to 1+2+3+4+5+6 = 21 jo aema thi jetla missing hase ae aai hase and aene divide by 2 karsu to answer mali jasee
    i = i+1

expected_sum = n * (n + 1)  // 2 
# ahiya kem nu thay che ke n X n+1 (ae ek  ek step agad vadhva mate use thase) jo // use na kariye to answer 17 aave che ae divede nathi karta total number ne 

actual_sum = sum(roll)

missing = expected_sum - actual_sum

print("Missing Roll Number =", missing)