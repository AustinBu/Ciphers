import math
message = input("Enter the message you would like to encrypt: ")
arr = []
a = 1
b = 0
c = -1
d = 0
f = 0
g = b
passed1 = True
passed2 = False
for i in range(math.ceil(math.sqrt(len(message)))):
    arr.append(['x'] * (math.ceil(math.sqrt(len(message)))))
e = len(arr) - 1
for z in range(len(message)):
    if passed1 == False:
        passed2 = True
    elif passed2 == False:
        passed1 = True
    arr[b][f] = message[z]
    g = b
    if g == e and passed1:
        for y in range(len(arr) - (d + 1)):
            if z == len(message) - 1:
                print(arr)
                exit()
            z += 1
            f += 1
            if z == len(message) - 1:
                arr[b][f] = message[z]
                print(arr)
                exit()
            arr[b][f] = message[z]
        a = -1
        e -= 1
        passed1 = False
    elif g == d and passed2:
        for x in range(len(arr) - (d + 2)):
            if z == len(message) - 1:
                print(arr)
                exit()
            z += 1
            f -= 1
            if z > len(message) - 1:
                arr[b][f] = message[z]
                print(arr)
                exit()
            arr[b][f] = message[z]
        a = 1
        d += 1
        passed2 = False
    b += a
for i in range(math.ceil(math.sqrt(len(message)))):
    print(arr[i])