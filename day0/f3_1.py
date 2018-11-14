phone = "13811010345"
if len(phone) == 11 and phone.isdigit() == True and phone[:3] == "138":
    print("this phonenumber is legal")
else:
    print("this phonenumber is illegal")
