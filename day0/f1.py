phoneNo = ["131", "132", "133", "134", "135", "136", "137", "138", "139", "180", "188", "189"]
pn = "13111113456"
if pn.isdigit() == True and len(pn) == 11:
    if pn[0:3] in phoneNo:
        print("This is a legal phonenum!")
else:
    print("This is a illegal phonenum!")
