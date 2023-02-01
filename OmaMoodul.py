from operator import truediv
from pickle import FALSE, TRUE
from unittest import TextTestRunner


def pikkus(ikood:str)->bool:
"""Funktsioon tagastab True, kui pikkus on 11 sümbolid
:param str ikood: Inimese isikukood 
: rtype: bool 
"""
if len(ikood)==11:
    flag=True 
else:
    flag=False
return flag
