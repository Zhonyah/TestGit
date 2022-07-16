#!/usr/bin/env python
# coding: utf-8

# In[29]:

def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        return False

def menu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")

def menuSel():
    userSelected = int(input(">>"))
    return userSelected

def vatCalculate(totalPrice):
        vat = 7
        result = totalPrice + (totalPrice * vat / 100)
        return result
def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculate(price1 + price2)

if login() == True:
    menu()
    a = menuSel()
    if a == 1:
        totalPrice = int(input("Input Your Price : "))
        print(vatCalculate(totalPrice))
    elif a == 2:
        print(priceCalculate())
    else:
        print("Please select number 1 and 2 only.")
else:
    print("รหัสของคุณไม่ถูกต้อง")
# In[ ]: