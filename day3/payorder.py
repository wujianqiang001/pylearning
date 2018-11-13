import requests
header = {"Referer": "http://api.iamsaonian.com/index.php?m=Api&c=Bianli&a=cart_show&shop_id=31&uuid=941e1aaaba585b952b62c14a3a175a61&login_token=98bb0bbdcf422b90ec4d85efd07aa423"}
url = "http://api.iamsaonian.com/index.php?m=Api&c=Bianli&a=buy&pay_type=1&building_id=654&name=%E5%90%B4%E5%BB%BA%E5%BC%BA&tel=13811010345&room=r&notes=1&shop_id=31&uuid=941e1aaaba585b952b62c14a3a175a61&login_token=98bb0bbdcf422b90ec4d85efd07aa423"
url = "http://api.iamsaonian.com/index.php?m=Api&c=Bianli&a=cart_add&uuid=941e1aaaba585b952b62c14a3a175a61&login_token=40882d26122e53f6e91641b14f9a4b9a&goods_num=100&goods_id=1194&shop_id=1"
r = requests.get(url,headers=header)
print(r.json())
