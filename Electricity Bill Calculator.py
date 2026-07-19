unit=int(input("Enter Your unit:"))
if unit <= 100:
  bill= unit*1.5
elif unit<=200:
  bill= (100*1.5) + (unit-100)*2.5
elif unit<=300:
  bill= (100*1.5) + (100*2.5) + (unit-200)*4
elif unit>300:
  bill= (100*1.5) + (100*2.5) + (100*4) + (unit-300)*6
else:
  print("Enter Valid Unit.")

print("Your total bill is:", bill, "rs")









unit=int(input("Enter Your unit:"))

if unit <= 100:
  bill= unit*1.5
elif unit<=200:
  bill= (100*1.5) + (unit-100)*2.5
elif unit<=300:
  bill= (100*1.5) + (100*2.5) + (unit-200)*4
elif unit>300:
  bill= (100*1.5) + (100*2.5) + (100*4) + (unit-300)*6
else:
  print("Enter Valid Unit.")


total_bill= bill+50
print("Your total bill is:", total_bill, "rs")











if unit <= 100:
  bill= unit*1.5
elif unit<=200:
  bill= (100*1.5) + (unit-100)*2.5
elif unit<=300:
  bill= (100*1.5) + (100*2.5) + (unit-200)*4
elif unit>300:
  bill= (100*1.5) + (100*2.5) + (100*4) + (unit-300)*6
else:
  print("Enter Valid Unit.")

print("Your orignal bill is:",bill,"Rs")

if bill>=1000:
  discount= (bill*5)/100
  new_bill= bill-discount
  print("Your discouted bill is:", new_bill, "Rs")
  total_bill = new_bill + 50
  print("Your Sub total:", total_bill ,"Rs")


else:
  totalBill=bill + 50
  print("your sub total is:", totalBill, "Rs")












unit=int(input("Enter Your unit:"))

if unit <= 100:
  bill= unit*1.5
elif unit<=200:
  bill= (100*1.5) + (unit-100)*2.5
elif unit<=300:
  bill= (100*1.5) + (100*2.5) + (unit-200)*4
elif unit>300:
  bill= (100*1.5) + (100*2.5) + (100*4) + (unit-300)*6
else:
  print("Enter Valid Unit.")

print("Your orignal bill is:",bill,"Rs")

if bill>=1000:
  discount= (bill*5)/100
  new_bill= bill-discount
  print("Your discouted bill is:", new_bill, "Rs")
  total_bill = new_bill + 50
  print("Your Sub total:", total_bill ,"Rs")


else:
  totalBill=bill + 50
  print("your sub total is:", totalBill, "Rs")



print("----------Your Bill Breakdwon----------")
if unit <= 100:
  print(unit,"*1.5 + 50(fixed charge)=", totalBill, "Rs")
elif unit<=200:
  print("(100*1.5) + (",unit,"-100)*2.5+ 50(fixed charge)=", totalBill,"Rs")
elif unit<=300:
  print("(100*1.5) + (100*2.5) + (",unit,"-200)*4 + 50(fixed charge)=", totalBill, "rs")
elif unit>300:
  print("(100*1.5) + (100*2.5) + (100*4) + (",unit,"-300)*6 + 50(fixed charge) -", discount,"(5% discount)=", total_bill, "Rs")
else:
  print("Enter Valid Unit.")










