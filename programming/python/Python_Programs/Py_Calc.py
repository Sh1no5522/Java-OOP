a = input("Enter an operation: ")
b = " "
d = " "
c = 0
for i in a:
    if(i == "+" or i == "-" or i == "*" or i == "/"):
        break
    b += i
b = int(b)
for i in range(c+1,len(a)):
    if(a[i] == "*" and a[i+1] == "*"):
        c = i+1
        break
    elif(a[i] == "+" or a[i] == "-" or a[i] == "*" or a[i] == "/"):
        c = i
        break
for i in range(c+1,len(a)):
    d += a[i]
d = int(d)
for i in range(len(a)):
    if(a[i] == "+"):
        print(int(b) + int(d))
        break
    elif(a[i] == "-"):
        print(int(b) - int(d))
        break
    elif(a[i] == "*" and a[i+1] == "*"):
        print(int(b) ** int(d))
        break
    elif(a[i] == "*"):
        print(int(b) * int(d))
        break
    elif(a[i] == "/"):
        print(round(float(b) / float(d), 2))
        break