shift = input("Enter key to shift by: ")
message = input("Enter the message you would like to encrypt: ")
newMessage = ""
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
a = 0
for x in range (len(message)):
    if message[x] != " ":
        if message[x].isalpha():
            location = alphabet.find(message[x])
            location1 = location + alphabet.find(shift[a])
            if location < 26 and location1 > 25:
                location1 = location1 % 26
            elif location > 25 and location1 > 51:
                location1 = location1 % 26 + 26
            newMessage = newMessage + alphabet[location1]
            if a == len(shift)-1:
                a = 0
            else:
                a+=1
        else:
            location = numbers.find(message[x])
            location1 = location + alphabet.find(shift[a])
            if location1 > 9:
                location1 = location1 % 10
            newMessage = newMessage + numbers[location1]
            if a == len(shift) - 1:
                a = 0
            else:
                a += 1
    else:
        newMessage = newMessage + " "
print(newMessage)