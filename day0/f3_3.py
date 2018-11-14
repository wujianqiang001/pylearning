phone = "  135110103452   "
phone = phone.strip()
pstart = ["131","132","133","134","135","136","137","138","139"]
if len(phone) == 11 and phone.isdigit() == True and phone[:3] in pstart:
    print("this phonenumber is legal")
else:
    print("this phonenumber is illegal")
