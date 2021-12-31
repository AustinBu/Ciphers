shift = input("Enter amount of rows: ")
message = input("Enter the message you would like to encrypt: ")
arr = []
a = 1
b = 0
c = 1
newMessage = ""
for x in range(int(shift)):
    arr.append([])
for y in range(len(message)):
    arr[b].append(message[y])
    if b > int(shift) - 2 and c == 1:
        a = -1
        c-=1
    elif b > int(shift) - 2 and c ==0:
        a = 0
        c+=1
    elif b < 1 and c == 1:
        a = 1
        c-=1
    elif b < 1 and c ==0:
        a = 0
        c+=1
    b += a
for x in range(int(shift)):
    print (arr[x])