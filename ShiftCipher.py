shift = input("Enter number to shift by: ")
message = input("Enter the message you would like to encrypt: ")
newMessage = ""
numbers = "1234567890"
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for x in range (len(message)):
    if message[x].isalpha():
        location = alphabet.find(message[x])
        location1 = location + int(shift)
        if location < 26 and location1 > 25:
            location1 = location1 % 26
        elif location > 25 and location1 > 51:
            location1 = location1 % 26 + 26
        elif location < 26 and location1 < 0:
            location1 = location1 % 26
            location1 = 25 - location1
        elif location > 25 and location1 < 26:
            location1 = location1 % 26
            location1 = 51 - location1
        newMessage = newMessage + alphabet[location1]
    else:
        location = numbers.find(message[x])
        location1 = location + int(shift)
        if location1 > 9:
            location1 = location1 % 10
        if location1 < 0:
            location1 = location1 % 10
            location1 = 9 - location1
        newMessage = newMessage + numbers[location]
print(newMessage)