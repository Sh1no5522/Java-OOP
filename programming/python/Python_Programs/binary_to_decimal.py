def reverse_string(s):
    reversed_str = ""
    for i in s:
        reversed_str = i + reversed_str
    return reversed_str
def binary_array_to_number(arr):
    arr.reverse()
    a = 1
    b = 0
    for i in range(len(arr)):
        for j in range(i):
            a *= 2
        if(arr[i] == 1):
            b += a
        a = 1
    arr.reverse()
    return b
lists = list(map(int, input("Enter list of numbers in binary: ").split()))
g = binary_array_to_number(lists)
h = ""

for i in range(len(lists)):
    h += str(lists[i])
print(f"binary number:{h} is equal to {g} in decimal")