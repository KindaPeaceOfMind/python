'''
Циклы
'''
# while 
print("Numbers < 10 (while):") 
i = 0 
while (i<10): 
    print(i, end=" ")  # print in one line 
    i += 1 
print("\n") 

# for 
print("Numbers < 10 (for):") 
for i in range(0,10): 
    print(i, end=" ") 
else: 
    print("\nThe next number is 10\n") 

# break 
sum_val = 0  # renamed from 'sum' to avoid shadowing built-in
for i in range(0,100): 
    if i > 10: 
        print("\nWe reached the end, final sum: ", sum_val) 
        break 
    sum_val += i 

# continue 
i = 0 
while i<=15: 
    if i % 3 == 0: 
        i += 1 
        continue 
    print(i, end=" ") 
    i += 1 
print("\n") 

# pass 
print("Let's print numbers again!") 
for i in range(0,10): 
    pass 
    print(i, end=" ") 
print("\n\n")

# ===== ЗАДАНИЕ 5 =====
print("Numbers divisible by 7 (while):")
i = 0
while i <= 500:
    if i % 7 == 0:
        print(i, end=" ")
    i += 1
else:
    print("\nAll numbers were printed!")

print("\nNumbers divisible by 7 (for):")
for i in range(0, 501):
    if i % 7 == 0:
        print(i, end=" ")
else:
    print("\nAll numbers were printed!")

# ===== ЗАДАНИЕ 6 =====
print("\nModified while loop (skip multiples of 14, stop at 300):")
i = 0
while i <= 500:
    if i > 300:
        break
    if i % 14 == 0 and i != 0:
        i += 1
        continue
    if i % 7 == 0:
        print(i, end=" ")
    i += 1
else:
    print("\nAll numbers were printed!")

print("\n\nModified for loop (skip multiples of 14, stop at 300):")
for i in range(0, 501):
    if i > 300:
        break
    if i % 14 == 0 and i != 0:
        continue
    if i % 7 == 0:
        print(i, end=" ")
else:
    print("\nAll numbers were printed!")

# ===== ЗАДАНИЕ 7 =====
print("\n\nDiagonal matrix (while):")
row = 0
while row < 4:
    col = 0
    while col < 4:
        if row == col:
            print(row + 1, end=" ")
        else:
            print(0, end=" ")
        col += 1
    print()
    row += 1

print("\nDiagonal matrix (for):")
for i in range(4):
    for j in range(4):
        if i == j:
            print(i + 1, end=" ")
        else:
            print(0, end=" ")
    print()