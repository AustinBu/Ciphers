message = input("Enter the encrypted message: ")
newMessage = ""
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
for y in range(1,26):
    for x in range (len(message)):
        if message[x] != " ":
            if message[x].isalpha():
                location = alphabet.find(message[x])
                location1 = location + y
                if location < 26 and location1 > 25:
                    location1 = location1 % 26
                elif location > 25 and location1 > 51:
                    location1 = location1 & 26 + 26
                newMessage = newMessage + alphabet[abs(location1)]
            else:
                location = numbers.find(message[x])
                location1 = location + y
                if location1 > 9:
                    location1 = location1 % 10
                newMessage = newMessage + numbers[abs(location1)]
        else:
            newMessage = newMessage + " "
    print(newMessage)
    newMessage = ""