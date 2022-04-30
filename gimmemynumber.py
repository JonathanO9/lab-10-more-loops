userstring = input("Gimmy a number greater than 100 plz..")
usernum = int(userstring)

while usernum <= 100:
    print(str(usernum) + " this number is less than and equal to 100, dummy. Try again. I've got all day")
    userstring = input("Gimmy a number greater than 100 please...")
    usernum = int(userstring)

print(str(usernum) + " us greater than 100! Good work.")