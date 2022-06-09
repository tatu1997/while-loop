atm_card=input("inser atm card")
if atm_card=="right side" or atm_card=="RIGHT SIDE":
  language=input("enter language")
  if language=="hindi" or language=="english":
    pin=int(input("enter pin"))
    if pin>=1000 and pin<=9999:
     type_option=input("enter transaction option")
     if type_option=="withdraw" or type_option=="WITHDRAW":
       amount_type=input("enter amount type")
       key_name=input("enter ok")
       amount=int(input("enter amount"))
       if amount>=500 or amount<=20000 and amount%500==0:
           a=amount//20000
           b=amount%20000
           c=b//500
           d=b%500
           print("notes of 2000=",a, "notes of 500=",c)
           amount_recept=input("enter amount_recept")
           if amount_recept=="yes" or amount_recept=="no":
               print("money_recept")
           else:
               print("thank you for the transaction")
     elif type_option=="balance enquiry" or type_option=="BALANCE":
          amount_type=input("enter account_type")
          account_no=int(input("enter account no"))
          key_name=input("enter ok")
          print("balance checking succesfull")
          if key_name=="ok" or key_name=="OK":
            print("thank you succesfull enquiry")
          else:
             print("invalid enquiry")
     elif type_option=="deposit" or type_option=="DEPOSIT":
       account_no=int(input("enter account_no"))
       if account_no>=100000000000 and account_no<=999999999999:
         bill_amount=int(input("enter bill_amount"))
         if bill_amount>=1 and bill_amount<=100000000000:
           key_name=input("enter key_name")
           if key_name=="ok" or key_name=="OK":
            print("succesfull")
           else:
             print("not successfull")
     elif type_option=="bill pay" and type_option=="BILL PAY":
       account_no=int(input("enter account no"))
       if account_no>=1100000000000 and account_no<=999999999999:
         bill_id=int(input("enter bill id number"))
         if bill_id>=100000000000 and bill_id<=999999999999:
           press_key=input("enter press_key")
           if press_key=="ok" and press_key=="OK":
             print("bill transaction complet")
           else:
             print("press the ok botton") 
  