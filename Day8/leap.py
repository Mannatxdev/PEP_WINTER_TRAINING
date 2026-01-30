### LEAP YEAR ###

# n = int(input("Enter the num btw 1900 and 100000:" ))
# if (n%4==0 and n%100!=0) or (n%400==0):
#     print(True)
# else:
#     print(False)
    


n = [
    [4, 3, 2, 1, 3, 4]
]

t = len(n)

for nums in n:
    n = len(nums)
    c = 0

    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                c += 1

    if c == 1:
        print("No")
    else:
        print("Yes")