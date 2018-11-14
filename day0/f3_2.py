phone = "  13911010345   "
phone = phone.strip()
if len(phone) == 11 and phone.isdigit() == True and \
   (phone[:3] == "138" or phone[:3] == "139" or phone[:3] == "135"):
    print("this phonenumber is legal")
else:
    print("this phonenumber is illegal")
