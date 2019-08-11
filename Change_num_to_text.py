print(">> Progeam Change number to Text <<")
num = int(input("Enter integer number : "))
print(f"Number : {num}")
snum = ""

for i in range(len(str(num))) :
    n = num % 10
    if n == 0 :
        snum =  "Zero " + snum
    elif n == 1 :
        snum = "One " + snum
    elif n == 2 :
        snum = "Two " + snum
    elif n == 3 :
        snum = "Three " + snum
    elif n == 4 :
        snum = "Four " + snum
    elif n == 5 :
        snum = "Five " + snum
    elif n == 6 :
        snum = "Six " + snum
    elif n == 7 :
        snum = "Seven " + snum
    elif n == 8 :
        snum = "Eight " + snum
    elif n == 9 :
        snum = "Nine " + snum
    num = num // 10
    
print("Text :",snum)
print("Exit Program")
