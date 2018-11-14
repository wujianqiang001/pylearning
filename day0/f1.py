Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> phone = "13811111111"
>>> print(phone)
13811111111
>>> 
>>> print(type(phone))
<class 'str'>
>>> 
>>> print(dir(phone))
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
>>> help(phone.upper)
Help on built-in function upper:

upper(...) method of builtins.str instance
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

>>> 
>>> print(phone.upper())
13811111111
>>> 
>>> 
>>> 
>>> s = "hello world"
>>> print(s)
hello world
>>> print(s.upper())
HELLO WORLD
>>> 
>>> 
>>> print(phone)
13811111111
>>> 
>>> 
>>> phone = "13811111111"
>>> phone1 = "a1381111111"
>>> print(phone.isdigit())
True
>>> print(phone1.isdigit())
False
>>> 
>>> print(phone)
13811111111
>>> print(len(phone))
11
>>> 
>>> 
>>> p = "hello"
>>> print(len(p))
5
>>> 
>>> p1 = "hello "
>>> print(len(p1))
6
>>> 
>>> 
>>> 
>>> phone = "1381111111"
>>> print(type(phone))
<class 'str'>
>>> print(dir(phone))
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> print(help(phone.isdigit))
Help on built-in function isdigit:

isdigit(...) method of builtins.str instance
    S.isdigit() -> bool
    
    Return True if all characters in S are digits
    and there is at least one character in S, False otherwise.

None
>>> print(phone.isdigit())
True
>>> print(len(phone))
10
>>> 
>>> 
